// ---------------------------------------------------------------------------
// Analysis (Photo-to-Plan)
// ---------------------------------------------------------------------------

export interface AnalysisRequest {
  part_description: string;
  intended_use: string;
  skill_level?: "beginner" | "intermediate" | "advanced";
  photo_base64?: string | null;
}

export interface PartAnalysis {
  geometry_type: string;
  dimensions: string;
  curvature: string;
  complexity: string;
  load_paths: string[];
  [key: string]: unknown;
}

export interface MaterialRecommendation {
  fibre_type: string;
  fibre_form: string;
  resin_system: string;
  reasoning: string[];
  [key: string]: unknown;
}

export interface LaminateDesign {
  stacking_sequence: number[];
  num_plies: number;
  thickness_mm: number;
  reinforcements: string[];
  [key: string]: unknown;
}

export interface ManufacturingPlan {
  process: string;
  steps: string[];
  materials_list: string[];
  consumables: string[];
  tooling_notes: string;
  [key: string]: unknown;
}

export interface CostBreakdown {
  material_cost: number;
  labour_cost: number;
  tooling_cost: number;
  consumables_cost: number;
  total_cost: number;
  breakdown_notes: string[];
  [key: string]: unknown;
}

export interface RiskAssessment {
  failure_modes: string[];
  inspection_points: string[];
  safety_factors: string;
  common_defects: string[];
  [key: string]: unknown;
}

export interface AnalysisResponse {
  part_analysis: PartAnalysis;
  material_recommendation: MaterialRecommendation;
  laminate_design: LaminateDesign;
  manufacturing_plan: ManufacturingPlan;
  cost_estimate: CostBreakdown;
  risk_assessment: RiskAssessment;
  report_markdown: string;
}

// ---------------------------------------------------------------------------
// Materials
// ---------------------------------------------------------------------------

export interface MaterialQuery {
  query: string;
}

export interface MaterialRecord {
  name: string;
  fibre_type: string;
  resin_type: string;
  e1_gpa: number;
  e2_gpa: number;
  tensile_strength_mpa: number;
  compressive_strength_mpa: number;
  cost_per_kg_usd: number;
  [key: string]: unknown;
}

export interface MaterialResponse {
  materials: MaterialRecord[];
  count: number;
}

// ---------------------------------------------------------------------------
// Processes
// ---------------------------------------------------------------------------

export type PerformanceClass = "hobby" | "structural" | "aerospace";
export type GeometryType =
  | "flat"
  | "single_curve"
  | "double_curve"
  | "axisymmetric"
  | "constant_cross_section";

export interface ProcessRecommendationRequest {
  part_size_m2: number;
  annual_volume: number;
  performance_class: PerformanceClass;
  geometry_type: GeometryType;
}

export interface ProcessRecommendation {
  process_name: string;
  suitability_score: number;
  reasoning: string[];
  warnings: string[];
  knowledge_base_link: string;
  [key: string]: unknown;
}

export interface ProcessRecommendationResponse {
  recommendations: ProcessRecommendation[];
}

// ---------------------------------------------------------------------------
// Cost Estimation
// ---------------------------------------------------------------------------

export interface CostEstimateRequest {
  fibre_type: string;
  process: string;
  part_weight_kg: number;
  number_of_plies: number;
  annual_volume: number;
}

export interface CostEstimateResponse {
  material_cost: number;
  labour_cost: number;
  tooling_cost: number;
  consumables_cost: number;
  total_cost: number;
  breakdown_notes: string[];
  disclaimer: string;
}

// ---------------------------------------------------------------------------
// Knowledge Base Search
// ---------------------------------------------------------------------------

export interface SearchRequest {
  query: string;
  top_n?: number;
}

export interface SearchResult {
  title: string;
  file: string;
  dir: string;
  url: string;
  category: string;
  difficulty: string;
  score: number;
  snippet: string;
  tags: string[];
  [key: string]: unknown;
}

export interface SearchResponse {
  results: SearchResult[];
  count: number;
}

// ---------------------------------------------------------------------------
// Stacking Rule Check
// ---------------------------------------------------------------------------

export interface StackingCheckRequest {
  angles: number[];
  max_consecutive?: number;
}

export interface StackingRuleResult {
  rule: string;
  passed: boolean;
  message: string;
  [key: string]: unknown;
}

export interface StackingCheckResponse {
  results: StackingRuleResult[];
  all_passed: boolean;
}

// ---------------------------------------------------------------------------
// App State
// ---------------------------------------------------------------------------

export type Page = "home" | "analyze" | "results" | "knowledge";

export interface AppState {
  currentPage: Page;
  analysisRequest: AnalysisRequest | null;
  analysisResponse: AnalysisResponse | null;
  isLoading: boolean;
  error: string | null;
}
