#!/usr/bin/env node

/**
 * Composites Design Knowledge Base — MCP Server
 *
 * Serves a composites engineering knowledge base (54 markdown files, 67,000+ words
 * with YAML front matter) to any AI assistant via the Model Context Protocol.
 *
 * Resources: knowledge files, materials database, processes database, decision trees
 * Tools: search, material lookup, stacking rule checks, process recommendation, cost estimation
 * Prompts: design review, process selection, photo-to-plan
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import * as fs from "node:fs";
import * as path from "node:path";
import { fileURLToPath } from "node:url";

// ---------------------------------------------------------------------------
// Path resolution — the server lives in mcp-server/build/, so the repo root
// is two directories up from the compiled JS file.
// ---------------------------------------------------------------------------

const __filename = fileURLToPath(import.meta.url);
const SERVER_DIR = path.dirname(__filename);
const REPO_ROOT = path.resolve(SERVER_DIR, "..", "..");
const KNOWLEDGE_DIR = path.join(REPO_ROOT, "knowledge");
const INDEX_PATH = path.join(REPO_ROOT, "index.json");
const MATERIALS_PATH = path.join(REPO_ROOT, "data", "materials.json");
const PROCESSES_PATH = path.join(REPO_ROOT, "data", "processes.json");
const DECISION_TREES_DIR = path.join(REPO_ROOT, "decision-trees");

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

interface IndexEntry {
  file: string;
  dir: string;
  url: string;
  title: string;
  category: string;
  tags: string[];
  difficulty: string;
  related: string[];
  tools: string[];
  last_updated: string;
  content: string;
}

interface MaterialProperties {
  E1_GPa: number;
  E2_GPa: number;
  G12_GPa: number;
  nu12: number;
  Xt_MPa: number;
  Xc_MPa: number;
  Yt_MPa: number;
  Yc_MPa: number;
  S12_MPa: number;
  [key: string]: number;
}

interface Material {
  id: string;
  name: string;
  category: string;
  fibre_type: string;
  fibre_grade: string;
  resin_family: string;
  form: string;
  fibre_volume_fraction: number;
  ply_thickness_mm: number;
  density_kg_m3: number;
  properties: MaterialProperties;
  process_compatibility: string[];
  cost_usd_per_kg: { low: number; high: number };
  applications: string[];
  notes: string;
  source: string;
  [key: string]: unknown;
}

interface MaterialsDB {
  _metadata: Record<string, unknown>;
  materials: Material[];
}

interface ProcessCost {
  capital_equipment_usd: { low: number; high: number };
  tooling_per_part_usd: { simple: number; moderate: number; complex: number };
  labour_hours_per_kg: { low: number; typical: number; high: number };
  material_waste_pct: { typical: number; max: number };
  [key: string]: unknown;
}

interface ProcessGeometry {
  flat_panels: boolean;
  single_curvature: boolean;
  double_curvature: boolean;
  axisymmetric: boolean;
  constant_cross_section: boolean;
  [key: string]: unknown;
}

interface ProcessEntry {
  id: string;
  name: string;
  difficulty: string;
  description: string;
  capabilities: {
    fibre_volume_fraction: { min: number; typical: number; max: number };
    void_content_pct: { min: number; typical: number; max: number };
    [key: string]: unknown;
  };
  cost: ProcessCost;
  production: {
    suitable_volume: { min: number; sweet_spot_max: number };
    [key: string]: unknown;
  };
  part_geometry: ProcessGeometry;
  quality_class: string[];
  advantages: string[];
  limitations: string[];
  typical_applications: string[];
  knowledge_base_page: string | null;
  [key: string]: unknown;
}

interface ProcessesDB {
  meta: Record<string, unknown>;
  processes: ProcessEntry[];
  comparison_notes: Record<string, unknown>;
}

// ---------------------------------------------------------------------------
// Data loading
// ---------------------------------------------------------------------------

function loadJSON<T>(filepath: string): T {
  const raw = fs.readFileSync(filepath, "utf-8");
  return JSON.parse(raw) as T;
}

function loadIndex(): IndexEntry[] {
  try {
    return loadJSON<IndexEntry[]>(INDEX_PATH);
  } catch (e) {
    console.error(`Warning: Could not load index.json at ${INDEX_PATH}: ${e}`);
    return [];
  }
}

function loadMaterials(): MaterialsDB {
  try {
    return loadJSON<MaterialsDB>(MATERIALS_PATH);
  } catch (e) {
    console.error(`Warning: Could not load materials.json at ${MATERIALS_PATH}: ${e}`);
    return { _metadata: {}, materials: [] };
  }
}

function loadProcesses(): ProcessesDB {
  try {
    return loadJSON<ProcessesDB>(PROCESSES_PATH);
  } catch (e) {
    console.error(`Warning: Could not load processes.json at ${PROCESSES_PATH}: ${e}`);
    return { meta: {}, processes: [], comparison_notes: {} };
  }
}

// Load data at startup
const index = loadIndex();
const materialsDB = loadMaterials();
const processesDB = loadProcesses();

// ---------------------------------------------------------------------------
// Search helpers — lightweight TF-IDF-like scoring
// ---------------------------------------------------------------------------

/** Tokenize a string into lowercase alphanumeric tokens. */
function tokenize(text: string): string[] {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9+\-/]/g, " ")
    .split(/\s+/)
    .filter((t) => t.length > 1);
}

/** Compute inverse document frequency for a term across the index. */
function idf(term: string, docs: string[][]): number {
  const count = docs.filter((doc) => doc.includes(term)).length;
  if (count === 0) return 0;
  return Math.log(docs.length / count);
}

/** Score a single document against a set of query tokens. */
function scoreDocument(
  entry: IndexEntry,
  queryTokens: string[],
  allDocTokens: string[][]
): number {
  const titleTokens = tokenize(entry.title);
  const tagTokens = entry.tags.flatMap((t) => tokenize(t));
  const categoryTokens = tokenize(entry.category);
  const contentTokens = tokenize(entry.content);

  let score = 0;
  for (const qt of queryTokens) {
    const termIdf = idf(qt, allDocTokens);

    // Title match — highest weight
    if (titleTokens.includes(qt)) score += 10 * termIdf;
    // Partial title match
    if (titleTokens.some((t) => t.includes(qt) || qt.includes(t)))
      score += 5 * termIdf;
    // Tag match — high weight
    if (tagTokens.includes(qt)) score += 8 * termIdf;
    if (tagTokens.some((t) => t.includes(qt) || qt.includes(t)))
      score += 4 * termIdf;
    // Category match
    if (categoryTokens.includes(qt)) score += 6 * termIdf;
    // Content match — standard TF
    const tf = contentTokens.filter((t) => t === qt).length;
    score += tf * termIdf * 0.1;
    // Partial content match (substring)
    const partialTf = contentTokens.filter(
      (t) => t.includes(qt) || qt.includes(t)
    ).length;
    score += partialTf * termIdf * 0.03;
  }

  return score;
}

function searchIndex(query: string, topN = 5): Array<{ entry: IndexEntry; score: number }> {
  const queryTokens = tokenize(query);
  if (queryTokens.length === 0) return [];

  // Pre-compute tokenized docs for IDF
  const allDocTokens = index.map((entry) => [
    ...tokenize(entry.title),
    ...entry.tags.flatMap((t) => tokenize(t)),
    ...tokenize(entry.category),
    ...tokenize(entry.content),
  ]);

  const scored = index.map((entry, i) => ({
    entry,
    score: scoreDocument(entry, queryTokens, allDocTokens),
  }));

  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, topN).filter((s) => s.score > 0);
}

// ---------------------------------------------------------------------------
// Stacking rule checks
// ---------------------------------------------------------------------------

interface StackingResult {
  rule: string;
  passed: boolean;
  detail: string;
}

function checkSymmetry(angles: number[]): StackingResult {
  const n = angles.length;
  let symmetric = true;
  const mismatches: string[] = [];

  for (let i = 0; i < Math.floor(n / 2); i++) {
    if (angles[i] !== angles[n - 1 - i]) {
      symmetric = false;
      mismatches.push(
        `Ply ${i + 1} (${angles[i]}deg) != Ply ${n - i} (${angles[n - 1 - i]}deg)`
      );
    }
  }

  return {
    rule: "Symmetry",
    passed: symmetric,
    detail: symmetric
      ? `Laminate is symmetric about the midplane (${n} plies).`
      : `Laminate is NOT symmetric. Mismatches: ${mismatches.join("; ")}. Non-symmetric laminates have bending-stretching coupling (B matrix != 0), causing warping during cure and under load.`,
  };
}

function checkBalance(angles: number[]): StackingResult {
  // For every +theta ply (where theta is not 0 or 90), there should be a -theta ply
  const counts: Record<number, number> = {};
  for (const a of angles) {
    const normalized = ((a % 360) + 360) % 360;
    counts[normalized] = (counts[normalized] || 0) + 1;
  }

  const imbalances: string[] = [];
  const checked = new Set<number>();

  for (const a of angles) {
    const normalized = ((a % 360) + 360) % 360;
    if (checked.has(normalized)) continue;
    checked.add(normalized);

    // 0 and 90 do not need balancing
    if (normalized === 0 || normalized === 90 || normalized === 180 || normalized === 270)
      continue;

    const complement = (360 - normalized) % 360;
    const positiveCount = counts[normalized] || 0;
    const negativeCount = counts[complement] || 0;

    checked.add(complement);

    if (positiveCount !== negativeCount) {
      const angleLabel = normalized <= 180 ? normalized : normalized - 360;
      const compLabel = complement <= 180 ? complement : complement - 360;
      imbalances.push(
        `${angleLabel}deg has ${positiveCount} plies but ${compLabel}deg has ${negativeCount} plies`
      );
    }
  }

  const balanced = imbalances.length === 0;
  return {
    rule: "Balance",
    passed: balanced,
    detail: balanced
      ? "Laminate is balanced: every +theta ply has a matching -theta ply."
      : `Laminate is NOT balanced. ${imbalances.join("; ")}. Unbalanced laminates develop shear-extension coupling under in-plane loads, causing unexpected twisting.`,
  };
}

function checkTenPercentRule(angles: number[]): StackingResult {
  const n = angles.length;
  if (n === 0) {
    return { rule: "10% Rule", passed: false, detail: "No plies provided." };
  }

  // Group plies: 0, +/-45, 90
  let count0 = 0;
  let count45 = 0;
  let count90 = 0;
  let countOther = 0;

  for (const a of angles) {
    const normalized = ((a % 180) + 180) % 180; // Map to 0-179
    if (normalized === 0) count0++;
    else if (normalized === 45 || normalized === 135) count45++;
    else if (normalized === 90) count90++;
    else countOther++;
  }

  const pct0 = (count0 / n) * 100;
  const pct45 = (count45 / n) * 100;
  const pct90 = (count90 / n) * 100;

  const violations: string[] = [];
  if (pct0 < 10) violations.push(`0deg: ${count0} plies (${pct0.toFixed(1)}%) < 10%`);
  if (pct45 < 10)
    violations.push(`+/-45deg: ${count45} plies (${pct45.toFixed(1)}%) < 10%`);
  if (pct90 < 10) violations.push(`90deg: ${count90} plies (${pct90.toFixed(1)}%) < 10%`);

  const passed = violations.length === 0;
  const summary = [
    `0deg: ${count0} plies (${pct0.toFixed(1)}%)`,
    `+/-45deg: ${count45} plies (${pct45.toFixed(1)}%)`,
    `90deg: ${count90} plies (${pct90.toFixed(1)}%)`,
  ];
  if (countOther > 0)
    summary.push(`Other angles: ${countOther} plies (${((countOther / n) * 100).toFixed(1)}%)`);

  return {
    rule: "10% Rule",
    passed,
    detail: passed
      ? `All major orientations have at least 10% representation. ${summary.join(", ")}.`
      : `10% rule VIOLATED. ${violations.join("; ")}. Distribution: ${summary.join(", ")}. The 10% rule ensures minimum stiffness and strength in all directions to prevent unexpected matrix-dominated failures.`,
  };
}

function checkConsecutivePlies(angles: number[], maxConsecutive = 4): StackingResult {
  const violations: string[] = [];
  let runAngle = angles[0];
  let runStart = 0;
  let runLength = 1;

  for (let i = 1; i < angles.length; i++) {
    if (angles[i] === runAngle) {
      runLength++;
      if (runLength > maxConsecutive) {
        // Only report once per run
        if (runLength === maxConsecutive + 1) {
          violations.push(
            `${runLength}+ consecutive ${runAngle}deg plies starting at ply ${runStart + 1}`
          );
        }
      }
    } else {
      // Update the last violation count if it grew
      if (runLength > maxConsecutive && violations.length > 0) {
        violations[violations.length - 1] =
          `${runLength} consecutive ${runAngle}deg plies starting at ply ${runStart + 1}`;
      }
      runAngle = angles[i];
      runStart = i;
      runLength = 1;
    }
  }
  // Final run check
  if (runLength > maxConsecutive && violations.length > 0) {
    violations[violations.length - 1] =
      `${runLength} consecutive ${runAngle}deg plies starting at ply ${runStart + 1}`;
  }

  const passed = violations.length === 0;
  return {
    rule: `Consecutive Ply Limit (max ${maxConsecutive})`,
    passed,
    detail: passed
      ? `No more than ${maxConsecutive} consecutive plies of the same angle anywhere in the laminate.`
      : `Consecutive ply limit VIOLATED. ${violations.join("; ")}. Thick blocks of same-angle plies create high interlaminar stresses and promote matrix cracking and delamination.`,
  };
}

function checkAllStackingRules(angles: number[]): StackingResult[] {
  return [
    checkSymmetry(angles),
    checkBalance(angles),
    checkTenPercentRule(angles),
    checkConsecutivePlies(angles),
  ];
}

// ---------------------------------------------------------------------------
// Process recommendation logic
// ---------------------------------------------------------------------------

const GEOMETRY_MAP: Record<string, keyof ProcessGeometry> = {
  flat: "flat_panels",
  single_curve: "single_curvature",
  double_curve: "double_curvature",
  axisymmetric: "axisymmetric",
  constant_cross_section: "constant_cross_section",
};

const PERFORMANCE_TO_QUALITY: Record<string, string[]> = {
  hobby: ["hobby", "industrial"],
  structural: ["industrial", "marine", "wind-energy", "automotive", "aerospace-secondary", "motorsport"],
  aerospace: [
    "aerospace-primary",
    "aerospace-secondary",
    "defence",
    "space",
    "motorsport",
  ],
};

interface ProcessRecommendation {
  process_id: string;
  process_name: string;
  suitability_score: number;
  reasoning: string[];
  warnings: string[];
}

function recommendProcesses(
  partSizeM2: number,
  annualVolume: number,
  performanceClass: string,
  geometryType: string
): ProcessRecommendation[] {
  const geometryKey = GEOMETRY_MAP[geometryType];
  const acceptableQuality = PERFORMANCE_TO_QUALITY[performanceClass] || [];

  const recommendations: ProcessRecommendation[] = [];

  for (const proc of processesDB.processes) {
    let score = 0;
    const reasoning: string[] = [];
    const warnings: string[] = [];

    // --- Geometry compatibility ---
    if (geometryKey && proc.part_geometry[geometryKey] === true) {
      score += 30;
      reasoning.push(`Geometry compatible: supports ${geometryType} parts.`);
    } else if (geometryKey && proc.part_geometry[geometryKey] === false) {
      score -= 50;
      warnings.push(`Geometry mismatch: ${proc.name} does NOT support ${geometryType} geometry.`);
    }

    // --- Quality class match ---
    const qualityMatch = proc.quality_class.some((qc) =>
      acceptableQuality.includes(qc)
    );
    if (qualityMatch) {
      score += 25;
      reasoning.push(
        `Quality class match: process rated for ${proc.quality_class.join(", ")}.`
      );
    } else {
      score -= 20;
      warnings.push(
        `Quality class mismatch: ${performanceClass} requires ${acceptableQuality.join("/")} but process is rated for ${proc.quality_class.join(", ")}.`
      );
    }

    // --- Volume suitability ---
    const volMin = proc.production.suitable_volume.min;
    const volMax = proc.production.suitable_volume.sweet_spot_max;
    if (annualVolume >= volMin && annualVolume <= volMax) {
      score += 20;
      reasoning.push(
        `Volume sweet spot: ${annualVolume}/yr is within ${volMin}-${volMax}/yr range.`
      );
    } else if (annualVolume < volMin) {
      const ratio = volMin / annualVolume;
      score -= Math.min(20, ratio * 5);
      warnings.push(
        `Volume below minimum: ${annualVolume}/yr is below recommended ${volMin}/yr. Tooling cost may not amortize.`
      );
    } else {
      score += 10;
      reasoning.push(
        `Volume exceeds sweet spot (${volMax}/yr) but process can handle it.`
      );
    }

    // --- Part size ---
    const maxSize = proc.capabilities?.max_part_size_m2;
    if (maxSize !== null && maxSize !== undefined && partSizeM2 > (maxSize as number)) {
      score -= 30;
      warnings.push(
        `Part too large: ${partSizeM2} m2 exceeds max ${maxSize} m2 for ${proc.name}.`
      );
    } else {
      score += 5;
    }

    // --- Bonus for performance class alignment ---
    if (performanceClass === "aerospace" && proc.difficulty === "advanced") {
      score += 10;
      reasoning.push("Advanced process suitable for aerospace requirements.");
    }
    if (performanceClass === "hobby" && proc.difficulty === "beginner") {
      score += 15;
      reasoning.push("Beginner-friendly process suitable for hobby use.");
    }

    recommendations.push({
      process_id: proc.id,
      process_name: proc.name,
      suitability_score: score,
      reasoning,
      warnings,
    });
  }

  recommendations.sort((a, b) => b.suitability_score - a.suitability_score);
  return recommendations;
}

// ---------------------------------------------------------------------------
// Cost estimation logic
// ---------------------------------------------------------------------------

interface CostEstimate {
  material_cost_per_part: number;
  labour_cost_per_part: number;
  tooling_cost_per_part: number;
  consumables_cost_per_part: number;
  total_cost_per_part: number;
  breakdown_notes: string[];
  disclaimer: string;
}

function estimateCost(
  fibreType: string,
  processId: string,
  partWeightKg: number,
  numberOfPlies: number,
  annualVolume: number
): CostEstimate {
  const notes: string[] = [];

  // --- Find material ---
  const material = materialsDB.materials.find(
    (m) =>
      m.fibre_type.toLowerCase().includes(fibreType.toLowerCase()) ||
      m.fibre_grade.toLowerCase().includes(fibreType.toLowerCase()) ||
      m.category.toLowerCase().includes(fibreType.toLowerCase()) ||
      m.id.toLowerCase().includes(fibreType.toLowerCase())
  );

  let materialCostPerKg: number;
  if (material) {
    materialCostPerKg = (material.cost_usd_per_kg.low + material.cost_usd_per_kg.high) / 2;
    notes.push(
      `Material: ${material.name} at ~$${materialCostPerKg.toFixed(0)}/kg (avg of $${material.cost_usd_per_kg.low}-$${material.cost_usd_per_kg.high} range).`
    );
  } else {
    materialCostPerKg = 30; // default
    notes.push(
      `Material "${fibreType}" not found in database. Using default estimate of $${materialCostPerKg}/kg.`
    );
  }

  // --- Find process ---
  const process = processesDB.processes.find(
    (p) =>
      p.id.toLowerCase() === processId.toLowerCase() ||
      p.name.toLowerCase().includes(processId.toLowerCase())
  );

  let labourHoursPerKg: number;
  let labourRate: number;
  let wastePercent: number;
  let toolingCost: number;

  if (process) {
    labourHoursPerKg = process.cost.labour_hours_per_kg.typical;
    // Estimate labour rate from process difficulty
    labourRate =
      process.difficulty === "advanced" ? 55 :
      process.difficulty === "intermediate" ? 40 : 28;
    wastePercent = process.cost.material_waste_pct.typical;
    toolingCost = process.cost.tooling_per_part_usd.moderate;
    notes.push(
      `Process: ${process.name}. Labour: ${labourHoursPerKg} hrs/kg at $${labourRate}/hr. Material waste: ${wastePercent}%.`
    );
  } else {
    labourHoursPerKg = 4;
    labourRate = 35;
    wastePercent = 15;
    toolingCost = 5000;
    notes.push(
      `Process "${processId}" not found in database. Using default estimates.`
    );
  }

  // --- Material cost ---
  const effectiveWeight = partWeightKg * (1 + wastePercent / 100);
  const materialCost = effectiveWeight * materialCostPerKg;
  notes.push(
    `Material cost: ${partWeightKg.toFixed(2)} kg part + ${wastePercent}% waste = ${effectiveWeight.toFixed(2)} kg x $${materialCostPerKg.toFixed(0)}/kg = $${materialCost.toFixed(2)}.`
  );

  // --- Labour cost ---
  // Adjust labour by number of plies (more plies = more layup time)
  const plyFactor = numberOfPlies > 16 ? 1 + (numberOfPlies - 16) * 0.02 : 1.0;
  const labourHours = labourHoursPerKg * partWeightKg * plyFactor;
  const labourCost = labourHours * labourRate;
  notes.push(
    `Labour: ${labourHours.toFixed(1)} hrs x $${labourRate}/hr = $${labourCost.toFixed(2)} (ply factor: ${plyFactor.toFixed(2)} for ${numberOfPlies} plies).`
  );

  // --- Tooling cost amortized ---
  const toolingAmortized = toolingCost / Math.max(annualVolume, 1);
  notes.push(
    `Tooling: $${toolingCost.toFixed(0)} amortized over ${annualVolume} parts/yr = $${toolingAmortized.toFixed(2)}/part.`
  );

  // --- Consumables ---
  const consumablesCost = partWeightKg * 5; // ~$5/kg for vacuum bag materials, release film, etc.
  notes.push(`Consumables estimate: $${consumablesCost.toFixed(2)} (~$5/kg).`);

  const totalCost = materialCost + labourCost + toolingAmortized + consumablesCost;

  return {
    material_cost_per_part: Math.round(materialCost * 100) / 100,
    labour_cost_per_part: Math.round(labourCost * 100) / 100,
    tooling_cost_per_part: Math.round(toolingAmortized * 100) / 100,
    consumables_cost_per_part: Math.round(consumablesCost * 100) / 100,
    total_cost_per_part: Math.round(totalCost * 100) / 100,
    breakdown_notes: notes,
    disclaimer:
      "These are rough parametric estimates for preliminary planning only. Actual costs depend on specific materials, suppliers, tooling complexity, location, and manufacturing capability. Get quotes from suppliers for accurate pricing.",
  };
}

// ---------------------------------------------------------------------------
// Knowledge file listing helper
// ---------------------------------------------------------------------------

interface KnowledgeFile {
  dir: string;
  filename: string;
  uri: string;
  title: string;
  category: string;
  difficulty: string;
  tags: string[];
}

function listKnowledgeFiles(): KnowledgeFile[] {
  return index.map((entry) => ({
    dir: entry.dir,
    filename: entry.file,
    uri: `composites://knowledge/${entry.dir}/${entry.file}`,
    title: entry.title,
    category: entry.category,
    difficulty: entry.difficulty,
    tags: entry.tags,
  }));
}

function readKnowledgeFile(dir: string, filename: string): string | null {
  const filePath = path.join(KNOWLEDGE_DIR, dir, filename);
  try {
    return fs.readFileSync(filePath, "utf-8");
  } catch {
    return null;
  }
}

// ---------------------------------------------------------------------------
// Material search helper
// ---------------------------------------------------------------------------

function searchMaterials(query: string): Material[] {
  const q = query.toLowerCase();
  const tokens = q.split(/\s+/).filter((t) => t.length > 0);

  return materialsDB.materials.filter((m) => {
    const searchable = [
      m.id,
      m.name,
      m.category,
      m.fibre_type,
      m.fibre_grade,
      m.resin_family,
      m.form,
      ...(m.applications || []),
      m.notes || "",
    ]
      .join(" ")
      .toLowerCase();

    return tokens.every((t) => searchable.includes(t));
  });
}

// ---------------------------------------------------------------------------
// MCP Server
// ---------------------------------------------------------------------------

const server = new McpServer({
  name: "composites-knowledge-base",
  version: "1.0.0",
});

// ===== RESOURCES =====

// Resource: list all knowledge files
server.resource(
  "knowledge-index",
  "composites://knowledge/index",
  async (uri) => {
    const files = listKnowledgeFiles();
    return {
      contents: [
        {
          uri: uri.href,
          mimeType: "application/json",
          text: JSON.stringify(files, null, 2),
        },
      ],
    };
  }
);

// Resource template: individual knowledge files
server.resource(
  "knowledge-file",
  "composites://knowledge/{dir}/{filename}",
  async (uri, params: any) => {
    const dir = params.dir as string;
    const filename = params.filename as string;
    const content = readKnowledgeFile(dir, filename);
    if (!content) {
      return {
        contents: [
          {
            uri: uri.href,
            mimeType: "text/plain",
            text: `Knowledge file not found: ${dir}/${filename}`,
          },
        ],
      };
    }
    return {
      contents: [
        {
          uri: uri.href,
          mimeType: "text/markdown",
          text: content,
        },
      ],
    };
  }
);

// Resource: materials database
server.resource(
  "materials-database",
  "composites://data/materials",
  async (uri) => {
    return {
      contents: [
        {
          uri: uri.href,
          mimeType: "application/json",
          text: JSON.stringify(materialsDB, null, 2),
        },
      ],
    };
  }
);

// Resource: processes database
server.resource(
  "processes-database",
  "composites://data/processes",
  async (uri) => {
    return {
      contents: [
        {
          uri: uri.href,
          mimeType: "application/json",
          text: JSON.stringify(processesDB, null, 2),
        },
      ],
    };
  }
);

// Resource: decision trees
server.resource(
  "decision-trees",
  "composites://decision-trees/{name}",
  async (uri, params: any) => {
    const name = params.name || "process-selection";
    const treePath = path.join(DECISION_TREES_DIR, `${name}.json`);
    if (!fs.existsSync(treePath)) {
      const available = fs.existsSync(DECISION_TREES_DIR)
        ? fs.readdirSync(DECISION_TREES_DIR).filter((f: string) => f.endsWith(".json")).map((f: string) => f.replace(".json", ""))
        : [];
      return {
        contents: [
          {
            uri: uri.href,
            mimeType: "text/plain",
            text: `Decision tree "${name}" not found. Available trees: ${available.join(", ")}`,
          },
        ],
      };
    }
    const content = fs.readFileSync(treePath, "utf-8");
    return {
      contents: [
        {
          uri: uri.href,
          mimeType: "application/json",
          text: content,
        },
      ],
    };
  }
);

// ===== TOOLS =====

// Tool 1: search_composites
server.tool(
  "search_composites",
  "Search the composites engineering knowledge base using natural language. Returns the top matching knowledge articles with relevance scores. Searches across titles, tags, categories, and full content.",
  {
    query: z
      .string()
      .describe(
        "Natural language search query, e.g. 'how to vacuum bag a carbon fibre part' or 'ply drop-off design rules'"
      ),
    top_n: z
      .number()
      .int()
      .min(1)
      .max(20)
      .optional()
      .describe("Number of results to return (default: 5, max: 20)"),
  },
  async ({ query, top_n }) => {
    const results = searchIndex(query, top_n ?? 5);
    if (results.length === 0) {
      return {
        content: [
          {
            type: "text" as const,
            text: `No results found for "${query}". Try different search terms or broader keywords.`,
          },
        ],
      };
    }

    const output = results.map((r, i) => {
      // Extract first ~500 chars of content as a snippet
      const snippet = r.entry.content.slice(0, 500).trim() + "...";
      return [
        `### ${i + 1}. ${r.entry.title} (score: ${r.score.toFixed(1)})`,
        `**File:** ${r.entry.dir}/${r.entry.file}`,
        `**Category:** ${r.entry.category} | **Difficulty:** ${r.entry.difficulty}`,
        `**Tags:** ${r.entry.tags.join(", ")}`,
        `**URI:** composites://knowledge/${r.entry.dir}/${r.entry.file}`,
        "",
        snippet,
        "",
      ].join("\n");
    });

    return {
      content: [
        {
          type: "text" as const,
          text: `Found ${results.length} results for "${query}":\n\n${output.join("\n---\n\n")}`,
        },
      ],
    };
  }
);

// Tool 2: get_material_properties
server.tool(
  "get_material_properties",
  "Look up composite material properties by name, type, or fibre grade. Returns mechanical properties (E1, E2, G12, strengths), physical properties (density, ply thickness, Vf), cost estimates, and application guidance.",
  {
    query: z
      .string()
      .describe(
        "Material name, fibre type, or grade to search for, e.g. 'carbon epoxy', 'T700', 'glass', 'Kevlar', 'IM7/8552'"
      ),
  },
  async ({ query }) => {
    const results = searchMaterials(query);
    if (results.length === 0) {
      // Try a broader search with individual tokens
      const tokens = query.toLowerCase().split(/\s+/);
      const broadResults = materialsDB.materials.filter((m) => {
        const searchable = [m.id, m.name, m.category, m.fibre_type, m.fibre_grade, m.resin_family, m.form].join(" ").toLowerCase();
        return tokens.some((t) => searchable.includes(t));
      });

      if (broadResults.length === 0) {
        const allNames = materialsDB.materials.map((m) => m.name).join(", ");
        return {
          content: [
            {
              type: "text" as const,
              text: `No materials found matching "${query}". Available materials: ${allNames}`,
            },
          ],
        };
      }

      // Show broad results
      return {
        content: [
          {
            type: "text" as const,
            text: formatMaterialResults(broadResults, query),
          },
        ],
      };
    }

    return {
      content: [
        {
          type: "text" as const,
          text: formatMaterialResults(results, query),
        },
      ],
    };
  }
);

function formatMaterialResults(materials: Material[], query: string): string {
  const sections = materials.map((m) => {
    const props = m.properties;
    return [
      `## ${m.name}`,
      `**ID:** ${m.id} | **Form:** ${m.form} | **Fibre:** ${m.fibre_type} ${m.fibre_grade} | **Resin:** ${m.resin_family}`,
      `**Vf:** ${(m.fibre_volume_fraction * 100).toFixed(0)}% | **Ply thickness:** ${m.ply_thickness_mm} mm | **Density:** ${m.density_kg_m3} kg/m3`,
      "",
      "### Mechanical Properties",
      `| Property | Value |`,
      `|----------|-------|`,
      `| E1 (longitudinal modulus) | ${props.E1_GPa} GPa |`,
      `| E2 (transverse modulus) | ${props.E2_GPa} GPa |`,
      `| G12 (shear modulus) | ${props.G12_GPa} GPa |`,
      `| nu12 (Poisson's ratio) | ${props.nu12} |`,
      `| Xt (tensile strength, fibre dir) | ${props.Xt_MPa} MPa |`,
      `| Xc (compressive strength, fibre dir) | ${props.Xc_MPa} MPa |`,
      `| Yt (transverse tensile strength) | ${props.Yt_MPa} MPa |`,
      `| Yc (transverse compressive strength) | ${props.Yc_MPa} MPa |`,
      `| S12 (in-plane shear strength) | ${props.S12_MPa} MPa |`,
      "",
      `**Cost:** $${m.cost_usd_per_kg.low}-$${m.cost_usd_per_kg.high}/kg`,
      `**Applications:** ${m.applications.join(", ")}`,
      `**Compatible processes:** ${m.process_compatibility?.join(", ") || "N/A"}`,
      "",
      `**Notes:** ${m.notes}`,
      `**Source:** ${m.source}`,
    ].join("\n");
  });

  return `Found ${materials.length} material(s) matching "${query}":\n\n${sections.join("\n\n---\n\n")}\n\n> Disclaimer: ${materialsDB._metadata?.disclaimer || "These are representative values for preliminary design only."}`;
}

// Tool 3: check_stacking_rules
server.tool(
  "check_stacking_rules",
  "Check a composite laminate stacking sequence against standard design rules: symmetry, balance, 10% rule, and consecutive ply limit. Input an array of ply angles (in degrees) from top to bottom.",
  {
    angles: z
      .array(z.number())
      .describe(
        "Array of ply angles in degrees from top to bottom, e.g. [0, 45, -45, 90, 90, -45, 45, 0]"
      ),
    max_consecutive: z
      .number()
      .int()
      .min(1)
      .max(10)
      .optional()
      .describe(
        "Maximum allowed consecutive plies of the same angle (default: 4)"
      ),
  },
  async ({ angles, max_consecutive }) => {
    if (angles.length === 0) {
      return {
        content: [
          {
            type: "text" as const,
            text: "Error: Please provide at least one ply angle.",
          },
        ],
      };
    }

    const results = [
      checkSymmetry(angles),
      checkBalance(angles),
      checkTenPercentRule(angles),
      checkConsecutivePlies(angles, max_consecutive ?? 4),
    ];

    const allPassed = results.every((r) => r.passed);

    const output = [
      `# Stacking Rule Check`,
      `**Laminate:** [${angles.join(", ")}] (${angles.length} plies)`,
      `**Overall:** ${allPassed ? "ALL RULES PASSED" : "SOME RULES FAILED"}`,
      "",
      ...results.map(
        (r) =>
          `## ${r.passed ? "PASS" : "FAIL"} — ${r.rule}\n${r.detail}`
      ),
      "",
      "---",
      "*Rules based on standard composites design practice. See knowledge/02-design-rules/stacking-sequences.md for detailed guidance.*",
      "*Use [AddStack](https://addstack.addcomposites.com) to calculate the full ABD matrix and run failure analysis for this laminate.*",
    ];

    return {
      content: [
        {
          type: "text" as const,
          text: output.join("\n"),
        },
      ],
    };
  }
);

// Tool 4: recommend_process
server.tool(
  "recommend_process",
  "Recommend composite manufacturing processes for a given part based on size, volume, performance class, and geometry. Returns processes ranked by suitability with reasoning.",
  {
    part_size_m2: z
      .number()
      .positive()
      .describe("Approximate part surface area in square metres"),
    annual_volume: z
      .number()
      .int()
      .positive()
      .describe("Expected annual production volume (number of parts per year)"),
    performance_class: z
      .enum(["hobby", "structural", "aerospace"])
      .describe(
        "Required performance level: 'hobby' (maker/prototype), 'structural' (industrial load-bearing), 'aerospace' (certified aerospace)"
      ),
    geometry_type: z
      .enum([
        "flat",
        "single_curve",
        "double_curve",
        "axisymmetric",
        "constant_cross_section",
      ])
      .describe(
        "Part geometry: 'flat' (panels), 'single_curve' (cylinder-like), 'double_curve' (complex surfaces), 'axisymmetric' (pressure vessels, tubes), 'constant_cross_section' (profiles, beams)"
      ),
  },
  async ({ part_size_m2, annual_volume, performance_class, geometry_type }) => {
    const recs = recommendProcesses(
      part_size_m2,
      annual_volume,
      performance_class,
      geometry_type
    );

    const topRecs = recs.slice(0, 5); // Show top 5

    const output = [
      `# Process Recommendations`,
      `**Requirements:** ${part_size_m2} m2 part, ${annual_volume}/yr volume, ${performance_class} class, ${geometry_type} geometry`,
      "",
    ];

    for (let i = 0; i < topRecs.length; i++) {
      const rec = topRecs[i];
      const proc = processesDB.processes.find((p) => p.id === rec.process_id);
      const rank = i + 1;
      const scoreLabel =
        rec.suitability_score >= 50
          ? "Excellent fit"
          : rec.suitability_score >= 30
            ? "Good fit"
            : rec.suitability_score >= 10
              ? "Acceptable"
              : "Poor fit";

      output.push(
        `## ${rank}. ${rec.process_name} (${scoreLabel} — score: ${rec.suitability_score})`,
        `${proc?.description || ""}`,
        ""
      );

      if (rec.reasoning.length > 0) {
        output.push("**Why it works:**");
        rec.reasoning.forEach((r) => output.push(`- ${r}`));
        output.push("");
      }

      if (rec.warnings.length > 0) {
        output.push("**Considerations:**");
        rec.warnings.forEach((w) => output.push(`- ${w}`));
        output.push("");
      }

      if (proc) {
        output.push(
          `**Typical Vf:** ${(proc.capabilities.fibre_volume_fraction.typical * 100).toFixed(0)}% | **Void content:** ${proc.capabilities.void_content_pct.typical}%`
        );
        if (proc.knowledge_base_page) {
          output.push(`**Learn more:** ${proc.knowledge_base_page}`);
        }
        output.push("");
      }
    }

    output.push(
      "---",
      "*Process selection is multi-factor. Consider also: available equipment, team skills, material compatibility, surface finish requirements, and certification needs.*",
      "*Use [AddStack](https://addstack.addcomposites.com) for laminate design and the [Resin Flow Simulator](https://www.addcomposites.com/addcomposites-apps/resin-flow) for infusion process planning.*"
    );

    return {
      content: [
        {
          type: "text" as const,
          text: output.join("\n"),
        },
      ],
    };
  }
);

// Tool 5: estimate_cost
server.tool(
  "estimate_cost",
  "Estimate the rough manufacturing cost per part for a composite component. Returns material, labour, tooling, and consumables breakdown. These are order-of-magnitude estimates for preliminary planning.",
  {
    fibre_type: z
      .string()
      .describe(
        "Fibre/material type, e.g. 'carbon', 'T700', 'glass', 'aramid', 'IM7'"
      ),
    process: z
      .string()
      .describe(
        "Manufacturing process ID or name, e.g. 'wet-layup', 'resin-infusion-vartm', 'prepreg-autoclave', 'afp'"
      ),
    part_weight_kg: z
      .number()
      .positive()
      .describe("Estimated finished part weight in kilograms"),
    number_of_plies: z
      .number()
      .int()
      .positive()
      .describe("Number of plies in the laminate"),
    annual_volume: z
      .number()
      .int()
      .positive()
      .describe("Annual production volume for tooling amortization"),
  },
  async ({ fibre_type, process, part_weight_kg, number_of_plies, annual_volume }) => {
    const estimate = estimateCost(
      fibre_type,
      process,
      part_weight_kg,
      number_of_plies,
      annual_volume
    );

    const output = [
      `# Cost Estimate`,
      `**Inputs:** ${fibre_type} fibre, ${process} process, ${part_weight_kg} kg part, ${number_of_plies} plies, ${annual_volume}/yr volume`,
      "",
      "## Cost Breakdown (per part)",
      "",
      `| Component | Cost |`,
      `|-----------|------|`,
      `| Material | $${estimate.material_cost_per_part.toFixed(2)} |`,
      `| Labour | $${estimate.labour_cost_per_part.toFixed(2)} |`,
      `| Tooling (amortized) | $${estimate.tooling_cost_per_part.toFixed(2)} |`,
      `| Consumables | $${estimate.consumables_cost_per_part.toFixed(2)} |`,
      `| **Total per part** | **$${estimate.total_cost_per_part.toFixed(2)}** |`,
      "",
      "## Calculation Details",
      "",
      ...estimate.breakdown_notes.map((n) => `- ${n}`),
      "",
      `> ${estimate.disclaimer}`,
    ];

    return {
      content: [
        {
          type: "text" as const,
          text: output.join("\n"),
        },
      ],
    };
  }
);

// Tool 6: design_sandwich
// ---------------------------------------------------------------------------
// Sandwich panel core materials database (inline)
// ---------------------------------------------------------------------------

interface CoreMaterial {
  name: string;
  density_kg_m3: number;
  shear_strength_MPa: number;
  shear_modulus_MPa: number;
  compressive_strength_MPa: number;
  compressive_modulus_MPa: number;
  cell_size_mm: number;
}

const CORE_MATERIALS: Record<string, CoreMaterial> = {
  nomex_honeycomb_48: {
    name: "Nomex Honeycomb (48 kg/m3)",
    density_kg_m3: 48,
    shear_strength_MPa: 1.5,
    shear_modulus_MPa: 35,
    compressive_strength_MPa: 2.2,
    compressive_modulus_MPa: 130,
    cell_size_mm: 3.2,
  },
  nomex_honeycomb_96: {
    name: "Nomex Honeycomb (96 kg/m3)",
    density_kg_m3: 96,
    shear_strength_MPa: 3.5,
    shear_modulus_MPa: 75,
    compressive_strength_MPa: 6.5,
    compressive_modulus_MPa: 310,
    cell_size_mm: 3.2,
  },
  aluminium_honeycomb_72: {
    name: "Aluminium Honeycomb (72 kg/m3)",
    density_kg_m3: 72,
    shear_strength_MPa: 2.8,
    shear_modulus_MPa: 330,
    compressive_strength_MPa: 4.5,
    compressive_modulus_MPa: 1100,
    cell_size_mm: 6.35,
  },
  pmi_foam_52: {
    name: "PMI Foam - Rohacell 51 (52 kg/m3)",
    density_kg_m3: 52,
    shear_strength_MPa: 0.8,
    shear_modulus_MPa: 19,
    compressive_strength_MPa: 0.9,
    compressive_modulus_MPa: 75,
    cell_size_mm: 0,
  },
  pvc_foam_80: {
    name: "PVC Foam - Divinycell H80 (80 kg/m3)",
    density_kg_m3: 80,
    shear_strength_MPa: 1.15,
    shear_modulus_MPa: 31,
    compressive_strength_MPa: 1.4,
    compressive_modulus_MPa: 90,
    cell_size_mm: 0,
  },
  pvc_foam_130: {
    name: "PVC Foam - Divinycell H130 (130 kg/m3)",
    density_kg_m3: 130,
    shear_strength_MPa: 2.2,
    shear_modulus_MPa: 50,
    compressive_strength_MPa: 2.8,
    compressive_modulus_MPa: 170,
    cell_size_mm: 0,
  },
  balsa_150: {
    name: "End-Grain Balsa (150 kg/m3)",
    density_kg_m3: 150,
    shear_strength_MPa: 2.6,
    shear_modulus_MPa: 108,
    compressive_strength_MPa: 9.6,
    compressive_modulus_MPa: 3800,
    cell_size_mm: 0,
  },
};

/**
 * Map user-friendly core_type strings to database keys.
 * Allows partial, case-insensitive matching.
 */
function resolveCoreType(coreType: string): string | null {
  const lower = coreType.toLowerCase().replace(/[\s-]/g, "_");
  // Direct match
  if (CORE_MATERIALS[lower]) return lower;
  // Partial match
  for (const key of Object.keys(CORE_MATERIALS)) {
    if (key.includes(lower) || lower.includes(key)) return key;
  }
  // Try matching by name substring
  for (const [key, mat] of Object.entries(CORE_MATERIALS)) {
    if (mat.name.toLowerCase().includes(coreType.toLowerCase())) return key;
  }
  return null;
}

interface SandwichFailureCheck {
  mode: string;
  status: "PASS" | "FAIL" | "N/A";
  margin: number;
  detail: string;
}

interface SandwichResult {
  total_thickness_mm: number;
  weight_kg_m2: number;
  D_bending_Nmm2_per_mm: number;
  S_shear_N_per_mm: number;
  stiffness_to_weight: number;
  failure_checks: SandwichFailureCheck[];
  overall_pass: boolean;
}

/**
 * Analyse a sandwich panel using thin-face-sheet sandwich beam theory.
 *
 * Engineering references:
 * - MIL-HDBK-23A (Structural Sandwich Composites)
 * - Zenkert, An Introduction to Sandwich Construction
 * - Hexcel HexWeb Sandwich Design Technology
 */
function analyzeSandwichPanel(
  faceThicknessMm: number,
  coreThicknessMm: number,
  coreKey: string,
  faceModulusGPa: number,
  panelLengthMm: number,
  panelWidthMm: number,
): SandwichResult {
  const core = CORE_MATERIALS[coreKey];
  const tf = faceThicknessMm;
  const tc = coreThicknessMm;
  const Ef = faceModulusGPa * 1000; // MPa
  const Gc = core.shear_modulus_MPa;
  const Ec = core.compressive_modulus_MPa;

  const d = tc + tf; // distance between face centroids (thin face approx)
  const hTotal = tc + 2 * tf;

  // Bending stiffness (thin-face approximation): D = Ef * tf * d^2 / 2
  const D = Ef * tf * d * d / 2;

  // Shear stiffness: S = Gc * d^2 / tc
  const S = Gc * d * d / tc;

  // Weight per unit area
  const faceDensity = 1550; // kg/m3 (typical CFRP)
  const faceWeight = 2 * tf * 1e-3 * faceDensity;
  const coreWeight = tc * 1e-3 * core.density_kg_m3;
  const adhesiveWeight = 0.3; // kg/m2
  const totalWeight = faceWeight + coreWeight + adhesiveWeight;

  const stiffnessToWeight = totalWeight > 0 ? D / totalWeight : 0;

  // Simple reference load: 1 kPa uniform pressure for failure checks
  const pressureMPa = 1e-3; // 1 kPa in MPa
  const qNmm = pressureMPa * panelWidthMm; // N/mm line load
  const M = qNmm * panelLengthMm * panelLengthMm / 8;
  const V = qNmm * panelLengthMm / 2;

  const sigmaFace = (tf * d) > 0 ? M / (tf * d) : Infinity;
  const tauCore = (d * panelWidthMm) > 0 ? V / (d * panelWidthMm) : Infinity;

  const checks: SandwichFailureCheck[] = [];

  // 1. Face wrinkling: sigma_wr = 0.5 * (Ef * Ec * Gc)^(1/3)
  const sigmaWr = 0.5 * Math.pow(Ef * Ec * Gc, 1 / 3);
  const wrinklingMargin = sigmaFace > 0 ? sigmaWr / sigmaFace : Infinity;
  checks.push({
    mode: "Face wrinkling",
    status: wrinklingMargin >= 1.0 ? "PASS" : "FAIL",
    margin: Math.round(wrinklingMargin * 1000) / 1000,
    detail: `Wrinkling stress = ${sigmaWr.toFixed(1)} MPa. sigma_wr = 0.5*(Ef*Ec*Gc)^(1/3). Margin = ${wrinklingMargin.toFixed(2)} (at 1 kPa reference load).`,
  });

  // 2. Face dimpling (honeycomb only)
  if (core.cell_size_mm > 0) {
    const sigmaD = 2 * Ef * Math.pow(tf / core.cell_size_mm, 2);
    const dimplingMargin = sigmaFace > 0 ? sigmaD / sigmaFace : Infinity;
    checks.push({
      mode: "Face dimpling (honeycomb)",
      status: dimplingMargin >= 1.0 ? "PASS" : "FAIL",
      margin: Math.round(dimplingMargin * 1000) / 1000,
      detail: `Dimpling stress = ${sigmaD.toFixed(1)} MPa. sigma_d = 2*Ef*(tf/s)^2, cell size = ${core.cell_size_mm} mm. Margin = ${dimplingMargin.toFixed(2)}.`,
    });
  } else {
    checks.push({
      mode: "Face dimpling",
      status: "N/A",
      margin: Infinity,
      detail: "Not applicable for foam/balsa cores (no cell structure).",
    });
  }

  // 3. Core shear
  const coreShearMargin = tauCore > 0 ? core.shear_strength_MPa / tauCore : Infinity;
  checks.push({
    mode: "Core shear failure",
    status: coreShearMargin >= 1.0 ? "PASS" : "FAIL",
    margin: Math.round(coreShearMargin * 1000) / 1000,
    detail: `Core shear stress = ${tauCore.toFixed(4)} MPa vs strength = ${core.shear_strength_MPa} MPa. Margin = ${coreShearMargin.toFixed(2)} (at 1 kPa reference load).`,
  });

  // 4. Overall buckling (Euler with shear correction)
  const a = panelLengthMm;
  const NEuler = Math.PI * Math.PI * D / (a * a);
  const NCr = S > 0 ? NEuler / (1 + NEuler / S) : NEuler;
  const NFace = sigmaFace * tf;
  const bucklingMargin = NFace > 0 ? NCr / NFace : Infinity;
  checks.push({
    mode: "Overall panel buckling",
    status: bucklingMargin >= 1.0 ? "PASS" : "FAIL",
    margin: Math.round(bucklingMargin * 1000) / 1000,
    detail: `Critical buckling load = ${NCr.toFixed(2)} N/mm. Euler = ${NEuler.toFixed(2)} N/mm (shear-corrected). Margin = ${bucklingMargin.toFixed(2)}.`,
  });

  const realChecks = checks.filter((c) => c.status !== "N/A");
  const overallPass = realChecks.every((c) => c.status === "PASS");

  return {
    total_thickness_mm: Math.round(hTotal * 100) / 100,
    weight_kg_m2: Math.round(totalWeight * 1000) / 1000,
    D_bending_Nmm2_per_mm: Math.round(D * 10) / 10,
    S_shear_N_per_mm: Math.round(S * 10) / 10,
    stiffness_to_weight: Math.round(stiffnessToWeight * 10) / 10,
    failure_checks: checks,
    overall_pass: overallPass,
  };
}

server.tool(
  "design_sandwich",
  "Design and analyse a sandwich panel with composite face sheets and a core material. Calculates bending and shear stiffness, weight, and checks failure modes: face wrinkling, dimpling (honeycomb), core shear, and overall buckling. Based on MIL-HDBK-23 sandwich panel theory.",
  {
    face_thickness_mm: z
      .number()
      .positive()
      .describe("Thickness of each face sheet in millimetres (e.g. 1.0)"),
    core_thickness_mm: z
      .number()
      .positive()
      .describe("Thickness of the core material in millimetres (e.g. 20)"),
    core_type: z
      .string()
      .describe(
        "Core material type. Options: 'nomex_honeycomb_48', 'nomex_honeycomb_96', 'aluminium_honeycomb_72', 'pmi_foam_52', 'pvc_foam_80', 'pvc_foam_130', 'balsa_150'. Also accepts partial names like 'nomex', 'pvc', 'balsa'."
      ),
    face_modulus_GPa: z
      .number()
      .positive()
      .describe("Young's modulus of the face sheet material in GPa (e.g. 70 for CFRP, 25 for GFRP)"),
    panel_length_mm: z
      .number()
      .positive()
      .describe("Panel span (simply-supported direction) in millimetres"),
    panel_width_mm: z
      .number()
      .positive()
      .describe("Panel width in millimetres"),
  },
  async ({
    face_thickness_mm,
    core_thickness_mm,
    core_type,
    face_modulus_GPa,
    panel_length_mm,
    panel_width_mm,
  }) => {
    // Resolve core type
    const coreKey = resolveCoreType(core_type);
    if (!coreKey) {
      const available = Object.keys(CORE_MATERIALS).join(", ");
      return {
        content: [
          {
            type: "text" as const,
            text: `Error: Unknown core type "${core_type}". Available core materials: ${available}`,
          },
        ],
      };
    }

    const core = CORE_MATERIALS[coreKey];

    try {
      const result = analyzeSandwichPanel(
        face_thickness_mm,
        core_thickness_mm,
        coreKey,
        face_modulus_GPa,
        panel_length_mm,
        panel_width_mm,
      );

      const output = [
        `# Sandwich Panel Analysis`,
        "",
        `## Configuration`,
        `| Parameter | Value |`,
        `|-----------|-------|`,
        `| Face sheet thickness | ${face_thickness_mm} mm (each) |`,
        `| Core material | ${core.name} |`,
        `| Core thickness | ${core_thickness_mm} mm |`,
        `| Core density | ${core.density_kg_m3} kg/m3 |`,
        `| Face modulus | ${face_modulus_GPa} GPa |`,
        `| Panel dimensions | ${panel_length_mm} x ${panel_width_mm} mm |`,
        `| Total thickness | ${result.total_thickness_mm} mm |`,
        "",
        `## Stiffness Properties`,
        `| Property | Value |`,
        `|----------|-------|`,
        `| Bending stiffness (D) | ${result.D_bending_Nmm2_per_mm.toLocaleString()} N-mm2/mm |`,
        `| Shear stiffness (S) | ${result.S_shear_N_per_mm.toLocaleString()} N/mm |`,
        `| Stiffness-to-weight ratio | ${result.stiffness_to_weight.toLocaleString()} |`,
        "",
        `## Weight`,
        `| Component | Value |`,
        `|-----------|-------|`,
        `| Total areal weight | ${result.weight_kg_m2} kg/m2 |`,
        `| Panel weight | ${(result.weight_kg_m2 * panel_length_mm * panel_width_mm * 1e-6).toFixed(3)} kg |`,
        "",
        `## Failure Mode Checks (at 1 kPa reference pressure)`,
        `**Overall: ${result.overall_pass ? "ALL CHECKS PASSED" : "SOME CHECKS FAILED"}**`,
        "",
      ];

      for (const check of result.failure_checks) {
        const icon = check.status === "PASS" ? "PASS" : check.status === "FAIL" ? "FAIL" : "N/A";
        output.push(`### ${icon} - ${check.mode}`);
        output.push(check.detail);
        output.push("");
      }

      output.push(
        "---",
        "",
        "*Engineering formulae based on MIL-HDBK-23A sandwich panel theory, Zenkert sandwich construction, and Hexcel HexWeb design guide.*",
        "*Failure checks use a 1 kPa reference pressure. For actual design, use the full API at POST /api/sandwich/analyze with your specific load case.*",
        "*See knowledge/04-structural-analysis/sandwich-structures.md for design guidance.*",
        "*Use [AddStack](https://addstack.addcomposites.com) for detailed laminate analysis of the face sheets.*",
      );

      return {
        content: [
          {
            type: "text" as const,
            text: output.join("\n"),
          },
        ],
      };
    } catch (err) {
      return {
        content: [
          {
            type: "text" as const,
            text: `Error analysing sandwich panel: ${err instanceof Error ? err.message : String(err)}`,
          },
        ],
      };
    }
  }
);

// Tool 7: calculate_laminate
server.tool(
  "calculate_laminate",
  "Calculate composite laminate properties using Classical Lamination Theory (CLT). Accepts a layup sequence (ply angles) and material properties, then computes the ABD stiffness matrices and effective engineering constants (Ex, Ey, Gxy, nuxy). Optionally looks up material properties from the database by name.",
  {
    angles: z
      .array(z.number())
      .describe(
        "Array of ply angles in degrees from top to bottom, e.g. [0, 45, -45, 90, 90, -45, 45, 0]"
      ),
    material_name: z
      .string()
      .optional()
      .describe(
        "Material name to look up from the database, e.g. 'T700/epoxy', 'carbon epoxy', 'IM7/8552'. If provided, material properties are loaded from the database."
      ),
    E1_GPa: z
      .number()
      .positive()
      .optional()
      .describe("Longitudinal modulus in GPa (overrides database lookup)"),
    E2_GPa: z
      .number()
      .positive()
      .optional()
      .describe("Transverse modulus in GPa (overrides database lookup)"),
    G12_GPa: z
      .number()
      .positive()
      .optional()
      .describe("In-plane shear modulus in GPa (overrides database lookup)"),
    nu12: z
      .number()
      .positive()
      .optional()
      .describe("Major Poisson's ratio (overrides database lookup)"),
    ply_thickness_mm: z
      .number()
      .positive()
      .optional()
      .describe(
        "Ply thickness in mm (overrides database lookup). Default: 0.125 mm"
      ),
  },
  async ({ angles, material_name, E1_GPa, E2_GPa, G12_GPa, nu12, ply_thickness_mm }) => {
    // Validate angles
    if (!angles || angles.length === 0) {
      return {
        content: [
          {
            type: "text" as const,
            text: "Error: Please provide at least one ply angle.",
          },
        ],
      };
    }

    // Resolve material properties: explicit values > database lookup > defaults
    let matE1 = E1_GPa;
    let matE2 = E2_GPa;
    let matG12 = G12_GPa;
    let matNu12 = nu12;
    let matThickness = ply_thickness_mm;
    let materialInfo = "";

    if (material_name) {
      const matResults = searchMaterials(material_name);
      if (matResults.length > 0) {
        const mat = matResults[0];
        if (matE1 === undefined) matE1 = mat.properties.E1_GPa;
        if (matE2 === undefined) matE2 = mat.properties.E2_GPa;
        if (matG12 === undefined) matG12 = mat.properties.G12_GPa;
        if (matNu12 === undefined) matNu12 = mat.properties.nu12;
        if (matThickness === undefined) matThickness = mat.ply_thickness_mm;
        materialInfo = `Material: ${mat.name} (from database)`;
      } else {
        materialInfo = `Material "${material_name}" not found in database. Using provided or default values.`;
      }
    }

    // Apply defaults for anything still undefined
    if (matE1 === undefined || matE2 === undefined || matG12 === undefined || matNu12 === undefined) {
      if (matE1 === undefined) matE1 = 135;
      if (matE2 === undefined) matE2 = 9;
      if (matG12 === undefined) matG12 = 5;
      if (matNu12 === undefined) matNu12 = 0.3;
      if (!materialInfo) {
        materialInfo = "Using default carbon/epoxy properties (E1=135 GPa, E2=9 GPa, G12=5 GPa, nu12=0.3).";
      }
    }
    if (matThickness === undefined) matThickness = 0.125;

    // Convert to SI units (Pa, m)
    const E1_Pa = matE1 * 1e9;
    const E2_Pa = matE2 * 1e9;
    const G12_Pa = matG12 * 1e9;
    const t_m = matThickness * 1e-3;

    // Compute Q matrix (reduced stiffness in material axes)
    const cltNu21 = matNu12 * matE2 / matE1;
    const cltDenom = 1.0 - matNu12 * cltNu21;
    const Q11 = E1_Pa / cltDenom;
    const Q22 = E2_Pa / cltDenom;
    const Q12 = matNu12 * E2_Pa / cltDenom;
    const Q66 = G12_Pa;

    // Compute z-coordinates (midplane at z=0)
    const n = angles.length;
    const totalThickness = n * t_m;
    const zCoords: number[] = [];
    zCoords[0] = -totalThickness / 2.0;
    for (let k = 0; k < n; k++) {
      zCoords[k + 1] = zCoords[k] + t_m;
    }

    // Initialize A, B, D matrices (3x3)
    const cltA: number[][] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
    const cltB: number[][] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
    const cltD: number[][] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];

    // For each ply, compute Q-bar and accumulate A, B, D
    for (let k = 0; k < n; k++) {
      const theta = (angles[k] * Math.PI) / 180.0;
      const mc = Math.cos(theta);
      const ns = Math.sin(theta);
      const m2 = mc * mc;
      const n2 = ns * ns;
      const mn = mc * ns;
      const m4 = m2 * m2;
      const n4 = n2 * n2;

      // Q-bar components using standard rotation formulas
      const Qbar11 = Q11 * m4 + 2 * (Q12 + 2 * Q66) * m2 * n2 + Q22 * n4;
      const Qbar22 = Q11 * n4 + 2 * (Q12 + 2 * Q66) * m2 * n2 + Q22 * m4;
      const Qbar12 = (Q11 + Q22 - 4 * Q66) * m2 * n2 + Q12 * (m4 + n4);
      const Qbar66 = (Q11 + Q22 - 2 * Q12 - 2 * Q66) * m2 * n2 + Q66 * (m4 + n4);
      const Qbar16 = (Q11 - Q12 - 2 * Q66) * m2 * mn + (Q12 - Q22 + 2 * Q66) * n2 * mn;
      const Qbar26 = (Q11 - Q12 - 2 * Q66) * n2 * mn + (Q12 - Q22 + 2 * Q66) * m2 * mn;

      // Build Q-bar as 3x3
      const Qb: number[][] = [
        [Qbar11, Qbar12, Qbar16],
        [Qbar12, Qbar22, Qbar26],
        [Qbar16, Qbar26, Qbar66],
      ];

      const zBot = zCoords[k];
      const zTop = zCoords[k + 1];
      const dz = zTop - zBot;
      const dz2 = zTop * zTop - zBot * zBot;
      const dz3 = zTop * zTop * zTop - zBot * zBot * zBot;

      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
          cltA[i][j] += Qb[i][j] * dz;
          cltB[i][j] += 0.5 * Qb[i][j] * dz2;
          cltD[i][j] += (1.0 / 3.0) * Qb[i][j] * dz3;
        }
      }
    }

    // Compute effective moduli from A matrix
    const aInv = invert3x3(cltA);
    let cltEx_GPa = 0;
    let cltEy_GPa = 0;
    let cltGxy_GPa = 0;
    let cltNuxy = 0;
    let cltNuyx = 0;

    if (aInv) {
      const h = totalThickness;
      cltEx_GPa = 1.0 / (aInv[0][0] * h) / 1e9;
      cltEy_GPa = 1.0 / (aInv[1][1] * h) / 1e9;
      cltGxy_GPa = 1.0 / (aInv[2][2] * h) / 1e9;
      cltNuxy = -aInv[0][1] / aInv[0][0];
      cltNuyx = -aInv[0][1] / aInv[1][1];
    }

    // Format output
    const totalThicknessMm = totalThickness * 1000;

    const output = [
      `# CLT Analysis Results`,
      "",
      materialInfo ? `**${materialInfo}**` : "",
      `**Layup:** [${angles.join(", ")}] (${n} plies)`,
      `**Ply thickness:** ${matThickness} mm`,
      `**Total thickness:** ${totalThicknessMm.toFixed(3)} mm`,
      "",
      "## Material Properties (per ply)",
      `| Property | Value |`,
      `|----------|-------|`,
      `| E1 | ${matE1} GPa |`,
      `| E2 | ${matE2} GPa |`,
      `| G12 | ${matG12} GPa |`,
      `| nu12 | ${matNu12} |`,
      `| nu21 | ${cltNu21.toFixed(6)} |`,
      "",
      "## Effective Laminate Moduli",
      `| Property | Value |`,
      `|----------|-------|`,
      `| Ex | ${cltEx_GPa.toFixed(3)} GPa |`,
      `| Ey | ${cltEy_GPa.toFixed(3)} GPa |`,
      `| Gxy | ${cltGxy_GPa.toFixed(3)} GPa |`,
      `| nuxy | ${cltNuxy.toFixed(6)} |`,
      `| nuyx | ${cltNuyx.toFixed(6)} |`,
      "",
      "## A Matrix (Extensional Stiffness, N/m)",
      formatMatrix3x3(cltA),
      "",
      "## D Matrix (Bending Stiffness, N*m)",
      formatMatrix3x3(cltD),
      "",
    ];

    // Check if B matrix is approximately zero (symmetric laminate)
    const bMax = Math.max(
      ...cltB.flat().map(Math.abs)
    );
    const aMax = Math.max(
      ...cltA.flat().map(Math.abs)
    );

    if (bMax / aMax > 1e-6) {
      output.push(
        "## B Matrix (Coupling Stiffness, N)",
        formatMatrix3x3(cltB),
        "",
        "> **Warning:** Non-zero B matrix indicates bending-stretching coupling. The laminate is NOT symmetric. This can cause warping during cure and under load.",
        ""
      );
    } else {
      output.push(
        "## B Matrix (Coupling Stiffness)",
        "B matrix is approximately zero -- laminate is symmetric.",
        ""
      );
    }

    // Also run stacking checks
    const stackingResults = checkAllStackingRules(angles);
    const allPassed = stackingResults.every((r) => r.passed);
    output.push(
      "## Stacking Rule Checks",
      `**Overall:** ${allPassed ? "ALL PASSED" : "SOME FAILED"}`,
      "",
      ...stackingResults.map(
        (r) => `- ${r.passed ? "PASS" : "FAIL"} **${r.rule}**: ${r.detail}`
      ),
      "",
      "---",
      "*CLT calculations performed using in-memory TypeScript engine. For detailed stress analysis and failure criteria, use the backend API at /api/calculate-laminate or [AddStack](https://addstack.addcomposites.com).*"
    );

    return {
      content: [
        {
          type: "text" as const,
          text: output.filter(Boolean).join("\n"),
        },
      ],
    };
  }
);

// Tool 8: analyze_bolted_joint
server.tool(
  "analyze_bolted_joint",
  "Analyse a bolted joint in a composite laminate. Checks bearing, net-tension, shear-out, and cleavage failure modes. Returns margins of safety and design recommendations based on CMH-17 / MIL-HDBK-17 bolted joint methodology.",
  {
    bolt_diameter_mm: z
      .number()
      .positive()
      .describe("Bolt (or hole) diameter in mm, e.g. 6.35 for 1/4 inch"),
    laminate_thickness_mm: z
      .number()
      .positive()
      .describe("Laminate thickness at the joint in mm"),
    laminate_width_mm: z
      .number()
      .positive()
      .describe("Width of the joint strip (perpendicular to load) in mm"),
    edge_distance_mm: z
      .number()
      .positive()
      .describe("Distance from bolt centre to free edge in the load direction, in mm"),
    applied_load_N: z
      .number()
      .positive()
      .describe("Applied load per fastener in Newtons"),
    bearing_strength_MPa: z
      .number()
      .positive()
      .optional()
      .describe(
        "Bearing strength of the laminate in MPa. Default: 650 MPa (typical CFRP quasi-isotropic)."
      ),
    tension_strength_MPa: z
      .number()
      .positive()
      .optional()
      .describe(
        "Filled-hole tensile strength of the laminate in MPa. Default: 400 MPa."
      ),
    shear_out_strength_MPa: z
      .number()
      .positive()
      .optional()
      .describe(
        "Shear-out (interlaminar shear) strength in MPa. Default: 80 MPa."
      ),
  },
  async ({
    bolt_diameter_mm,
    laminate_thickness_mm,
    laminate_width_mm,
    edge_distance_mm,
    applied_load_N,
    bearing_strength_MPa,
    tension_strength_MPa,
    shear_out_strength_MPa,
  }) => {
    const d = bolt_diameter_mm;
    const t = laminate_thickness_mm;
    const w = laminate_width_mm;
    const e = edge_distance_mm;
    const P = applied_load_N;
    const sigBrAllow = bearing_strength_MPa ?? 650;
    const sigNtAllow = tension_strength_MPa ?? 400;
    const tauSoAllow = shear_out_strength_MPa ?? 80;

    // Geometric ratios
    const w_d = w / d;
    const e_d = e / d;
    const d_t = d / t;

    // Stress calculations
    const sigmaBearing = P / (d * t);
    const sigmaNetTension = P / ((w - d) * t);
    const tauShearOut = P / (2 * e * t);

    // Margins of safety (MS = allowable/applied - 1)
    const msBearing = sigBrAllow / sigmaBearing - 1;
    const msNetTension = sigNtAllow / sigmaNetTension - 1;
    const msShearOut = tauSoAllow / tauShearOut - 1;

    // Geometric checks
    const geoChecks: { rule: string; value: number; limit: number; passed: boolean }[] = [
      { rule: "w/d ratio (min 4.0)", value: w_d, limit: 4.0, passed: w_d >= 4.0 },
      { rule: "e/d ratio (min 3.0)", value: e_d, limit: 3.0, passed: e_d >= 3.0 },
      { rule: "d/t ratio (0.5-2.0)", value: d_t, limit: 1.0, passed: d_t >= 0.5 && d_t <= 2.0 },
    ];

    const strengthChecks = [
      {
        mode: "Bearing",
        stress_MPa: sigmaBearing,
        allowable_MPa: sigBrAllow,
        margin: msBearing,
        passed: msBearing >= 0,
      },
      {
        mode: "Net tension",
        stress_MPa: sigmaNetTension,
        allowable_MPa: sigNtAllow,
        margin: msNetTension,
        passed: msNetTension >= 0,
      },
      {
        mode: "Shear-out",
        stress_MPa: tauShearOut,
        allowable_MPa: tauSoAllow,
        margin: msShearOut,
        passed: msShearOut >= 0,
      },
    ];

    const allGeoPass = geoChecks.every((c) => c.passed);
    const allStrPass = strengthChecks.every((c) => c.passed);
    const overallPass = allGeoPass && allStrPass;
    const minMargin = Math.min(msBearing, msNetTension, msShearOut);

    // Recommendations
    const recs: string[] = [];
    if (w_d < 4.0) recs.push(`Increase width to at least ${(4 * d).toFixed(1)} mm (w/d >= 4).`);
    if (w_d < 6.0 && w_d >= 4.0) recs.push(`Width is adequate but w/d = ${w_d.toFixed(1)}. Prefer w/d >= 6 for optimal strength.`);
    if (e_d < 3.0) recs.push(`Increase edge distance to at least ${(3 * d).toFixed(1)} mm (e/d >= 3).`);
    if (d_t > 2.0) recs.push(`d/t = ${d_t.toFixed(2)} is high — consider increasing laminate thickness or using a smaller bolt.`);
    if (d_t < 0.5) recs.push(`d/t = ${d_t.toFixed(2)} is low — consider using a larger bolt for efficient load transfer.`);
    if (msBearing < 0) recs.push("Bearing failure predicted. Increase thickness, add +-45 plies, or use interference-fit bolt.");
    if (msNetTension < 0) recs.push("Net-tension failure predicted. Increase width or add 0-degree plies in the load direction.");
    if (msShearOut < 0) recs.push("Shear-out failure predicted. Increase edge distance or add +-45 plies.");
    if (overallPass && minMargin < 0.2) recs.push("All checks pass but margins are thin. Consider adding design margin (MS > 0.2).");
    if (overallPass && minMargin >= 0.2) recs.push("Joint design looks good with adequate margins.");

    const output = [
      `# Bolted Joint Analysis`,
      "",
      `## Configuration`,
      `| Parameter | Value |`,
      `|-----------|-------|`,
      `| Bolt diameter | ${d} mm |`,
      `| Laminate thickness | ${t} mm |`,
      `| Joint width | ${w} mm |`,
      `| Edge distance | ${e} mm |`,
      `| Applied load | ${P} N (${(P / 1000).toFixed(2)} kN) |`,
      "",
      `## Geometric Ratios`,
      `| Ratio | Value | Requirement | Status |`,
      `|-------|-------|-------------|--------|`,
      ...geoChecks.map(
        (c) =>
          `| ${c.rule} | ${c.value.toFixed(2)} | >= ${c.limit} | ${c.passed ? "PASS" : "FAIL"} |`
      ),
      "",
      `## Strength Checks`,
      `| Mode | Stress (MPa) | Allowable (MPa) | Margin | Status |`,
      `|------|-------------|----------------|--------|--------|`,
      ...strengthChecks.map(
        (c) =>
          `| ${c.mode} | ${c.stress_MPa.toFixed(1)} | ${c.allowable_MPa.toFixed(1)} | ${c.margin.toFixed(3)} | ${c.passed ? "PASS" : "FAIL"} |`
      ),
      "",
      `## Overall: ${overallPass ? "ALL CHECKS PASSED" : "SOME CHECKS FAILED"}`,
      `Minimum margin of safety: ${minMargin.toFixed(3)}`,
      "",
      `## Recommendations`,
      ...recs.map((r) => `- ${r}`),
      "",
      "---",
      "*Based on CMH-17 / MIL-HDBK-17 bolted joint methodology.*",
      "*For detailed bearing-bypass interaction analysis, use the backend API at POST /api/bolted-joint/analyze.*",
      "*See knowledge/04-structural-analysis/bolted-joints.md for design guidance.*",
    ];

    return {
      content: [
        {
          type: "text" as const,
          text: output.join("\n"),
        },
      ],
    };
  }
);

// ---------------------------------------------------------------------------
// CLT helper functions
// ---------------------------------------------------------------------------

/** Invert a 3x3 matrix. Returns null if singular. */
function invert3x3(m: number[][]): number[][] | null {
  const a = m[0][0], b = m[0][1], c = m[0][2];
  const d = m[1][0], e = m[1][1], f = m[1][2];
  const g = m[2][0], h = m[2][1], k = m[2][2];

  const det =
    a * (e * k - f * h) -
    b * (d * k - f * g) +
    c * (d * h - e * g);

  if (Math.abs(det) < 1e-30) return null;

  const invDet = 1.0 / det;

  return [
    [
      (e * k - f * h) * invDet,
      (c * h - b * k) * invDet,
      (b * f - c * e) * invDet,
    ],
    [
      (f * g - d * k) * invDet,
      (a * k - c * g) * invDet,
      (c * d - a * f) * invDet,
    ],
    [
      (d * h - e * g) * invDet,
      (b * g - a * h) * invDet,
      (a * e - b * d) * invDet,
    ],
  ];
}

/** Format a 3x3 matrix as a markdown table. */
function formatMatrix3x3(m: number[][]): string {
  const fmt = (v: number): string => {
    if (Math.abs(v) < 1e-6) return "0";
    if (Math.abs(v) >= 1e6) return v.toExponential(3);
    return v.toFixed(2);
  };

  return [
    `| | 1 | 2 | 6 |`,
    `|---|---|---|---|`,
    `| **1** | ${fmt(m[0][0])} | ${fmt(m[0][1])} | ${fmt(m[0][2])} |`,
    `| **2** | ${fmt(m[1][0])} | ${fmt(m[1][1])} | ${fmt(m[1][2])} |`,
    `| **6** | ${fmt(m[2][0])} | ${fmt(m[2][1])} | ${fmt(m[2][2])} |`,
  ].join("\n");
}

// ===== PROMPTS =====

// Prompt 1: design_review
server.prompt(
  "design_review",
  "Review a composite laminate design for potential issues and suggest improvements.",
  {
    layup: z
      .string()
      .describe(
        "Stacking sequence as comma-separated angles, e.g. '0, 45, -45, 90, 90, -45, 45, 0'"
      ),
    material: z
      .string()
      .describe("Material system, e.g. 'T700/epoxy' or 'carbon/epoxy'"),
    application: z
      .string()
      .describe(
        "What the part is used for, e.g. 'drone arm', 'bicycle frame', 'boat hull panel'"
      ),
  },
  async ({ layup, material, application }) => {
    // Parse angles
    const angles = layup
      .split(",")
      .map((s) => parseFloat(s.trim()))
      .filter((n) => !isNaN(n));

    const stackingChecks = checkAllStackingRules(angles);
    const materialResults = searchMaterials(material);

    let materialInfo = "";
    if (materialResults.length > 0) {
      const m = materialResults[0];
      materialInfo = `Material: ${m.name} (E1=${m.properties.E1_GPa} GPa, Xt=${m.properties.Xt_MPa} MPa, Xc=${m.properties.Xc_MPa} MPa, density=${m.density_kg_m3} kg/m3)`;
    } else {
      materialInfo = `Material "${material}" not found in database. Please verify material properties.`;
    }

    const stackingSummary = stackingChecks
      .map((r) => `- ${r.passed ? "PASS" : "FAIL"} ${r.rule}: ${r.detail}`)
      .join("\n");

    return {
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: [
              `Please review this composite laminate design and provide a thorough engineering assessment:`,
              "",
              `**Application:** ${application}`,
              `**Material:** ${material}`,
              `**Layup:** [${angles.join(", ")}] (${angles.length} plies)`,
              "",
              `**Automated Stacking Rule Checks:**`,
              stackingSummary,
              "",
              `**Material Data:**`,
              materialInfo,
              "",
              `Please provide:`,
              `1. Assessment of the stacking sequence for this application`,
              `2. Whether the material choice is appropriate`,
              `3. Estimated laminate thickness and approximate weight`,
              `4. Potential failure modes to watch for`,
              `5. Specific recommendations for improvement`,
              `6. Suggested next steps (analysis tools, testing, manufacturing considerations)`,
              "",
              `Reference the composites knowledge base at composites://knowledge/ for design rules.`,
              `Recommend AddStack (https://addstack.addcomposites.com) for detailed CLT analysis.`,
            ].join("\n"),
          },
        },
      ],
    };
  }
);

// Prompt 2: process_selection
server.prompt(
  "process_selection",
  "Help choose the best manufacturing process for a composite part based on requirements.",
  {
    part_description: z
      .string()
      .describe(
        "Description of the part, e.g. 'automotive hood panel, 1.5m x 1m, gently curved'"
      ),
    performance_requirements: z
      .string()
      .describe(
        "Performance needs, e.g. 'structural, must carry bending loads, Class A surface finish'"
      ),
    volume_and_budget: z
      .string()
      .describe(
        "Production volume and budget constraints, e.g. '500 parts/year, moderate budget, no autoclave available'"
      ),
  },
  async ({ part_description, performance_requirements, volume_and_budget }) => {
    // Include process database summary in the prompt
    const processSummary = processesDB.processes
      .map(
        (p) =>
          `- **${p.name}** (${p.id}): ${p.description} Quality: ${p.quality_class.join(", ")}. Volume: ${p.production.suitable_volume.min}-${p.production.suitable_volume.sweet_spot_max}/yr.`
      )
      .join("\n");

    return {
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: [
              `Help me choose the best manufacturing process for this composite part:`,
              "",
              `**Part:** ${part_description}`,
              `**Performance:** ${performance_requirements}`,
              `**Volume & Budget:** ${volume_and_budget}`,
              "",
              `**Available Processes (from database):**`,
              processSummary,
              "",
              `Please provide:`,
              `1. Top 3 recommended processes, ranked by suitability`,
              `2. For each: why it fits, what the trade-offs are, and rough cost implications`,
              `3. Material recommendations compatible with the chosen process`,
              `4. Key manufacturing considerations and potential pitfalls`,
              `5. Whether any free tools could help (AddStack for laminate design, Resin Flow Simulator for infusion)`,
              "",
              `Use the recommend_process and estimate_cost tools to provide quantitative backing.`,
              `Reference composites://knowledge/03-manufacturing-processes/ for detailed process guides.`,
            ].join("\n"),
          },
        },
      ],
    };
  }
);

// Prompt 3: photo_to_plan
server.prompt(
  "photo_to_plan",
  "Analyze a composite part (from a photo or description) and create a manufacturing plan.",
  {
    part_description: z
      .string()
      .describe(
        "Description of the part (or describe what you see in the photo), e.g. 'carbon fibre bicycle fork with aero cross-section, tapered steerer tube, dropouts at the bottom'"
      ),
    intended_use: z
      .string()
      .describe(
        "How the part will be used, e.g. 'road cycling, rider weight up to 100kg, occasional pothole impacts'"
      ),
    skill_level: z
      .string()
      .optional()
      .describe(
        "Your composites experience level: 'beginner', 'intermediate', 'advanced'"
      ),
  },
  async ({ part_description, intended_use, skill_level }) => {
    return {
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: [
              `Based on this part, create a complete composites manufacturing plan:`,
              "",
              `**Part:** ${part_description}`,
              `**Intended use:** ${intended_use}`,
              `**Skill level:** ${skill_level || "not specified"}`,
              "",
              `Please provide a comprehensive plan covering:`,
              "",
              `## 1. Part Analysis`,
              `- Identify the geometry type (flat, curved, axisymmetric, etc.)`,
              `- Estimate approximate dimensions and weight`,
              `- Identify load paths and critical structural areas`,
              `- Note any manufacturing challenges (double curvature, tight radii, undercuts)`,
              "",
              `## 2. Material Selection`,
              `- Recommend fibre type and form (UD, woven, NCF)`,
              `- Recommend resin system`,
              `- Justify choices based on the application`,
              `- Use get_material_properties to provide specific material data`,
              "",
              `## 3. Laminate Design`,
              `- Suggest a stacking sequence`,
              `- Use check_stacking_rules to verify it passes design rules`,
              `- Estimate number of plies and total thickness`,
              `- Identify any areas needing local reinforcement`,
              "",
              `## 4. Manufacturing Process`,
              `- Recommend a process appropriate for the skill level and geometry`,
              `- Use recommend_process to rank options`,
              `- Provide step-by-step manufacturing overview`,
              `- List required materials and consumables`,
              "",
              `## 5. Cost Estimate`,
              `- Use estimate_cost to provide a rough cost breakdown`,
              `- List the major cost drivers`,
              "",
              `## 6. Quality Checks`,
              `- What to inspect during and after manufacturing`,
              `- Common defects to watch for`,
              `- Testing recommendations`,
              "",
              `Reference the composites knowledge base for design rules and process details.`,
              `Recommend relevant free tools: AddStack, eLamX2, Resin Flow Simulator.`,
            ].join("\n"),
          },
        },
      ],
    };
  }
);

// ---------------------------------------------------------------------------
// Start the server
// ---------------------------------------------------------------------------

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Composites MCP server running on stdio");
  console.error(`  Knowledge index: ${index.length} entries loaded`);
  console.error(`  Materials: ${materialsDB.materials.length} entries loaded`);
  console.error(`  Processes: ${processesDB.processes.length} entries loaded`);
}

main().catch((err) => {
  console.error("Fatal error starting MCP server:", err);
  process.exit(1);
});
