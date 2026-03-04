import { useState } from "react";
import {
  ChevronDown,
  ChevronRight,
  Download,
  Box,
  Atom,
  Layers,
  Wrench,
  DollarSign,
  ShieldAlert,
} from "lucide-react";
import StackingVisualizer from "./StackingVisualizer";
import CostBreakdownChart from "./CostBreakdownChart";
import ProcessCard from "./ProcessCard";
import MaterialCard from "./MaterialCard";
import type { AnalysisResponse } from "../types";

interface ResultsDisplayProps {
  response: AnalysisResponse;
  onDownloadReport: () => void;
}

// ---------------------------------------------------------------------------
// Collapsible Section
// ---------------------------------------------------------------------------

interface SectionProps {
  title: string;
  icon: React.ReactNode;
  defaultOpen?: boolean;
  children: React.ReactNode;
}

function Section({ title, icon, defaultOpen = true, children }: SectionProps) {
  const [isOpen, setIsOpen] = useState(defaultOpen);

  return (
    <div className="overflow-hidden rounded-lg border border-secondary-200 bg-white dark:border-secondary-700 dark:bg-secondary-800">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex w-full items-center gap-3 px-4 py-3 text-left transition-colors hover:bg-secondary-50 dark:hover:bg-secondary-700/50"
      >
        <span className="text-primary-600 dark:text-primary-400">{icon}</span>
        <span className="flex-1 text-sm font-semibold text-secondary-900 dark:text-white">
          {title}
        </span>
        {isOpen ? (
          <ChevronDown size={18} className="text-secondary-400" />
        ) : (
          <ChevronRight size={18} className="text-secondary-400" />
        )}
      </button>
      {isOpen && (
        <div className="animate-fade-in border-t border-secondary-100 px-4 py-4 dark:border-secondary-700">
          {children}
        </div>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Info Row helper
// ---------------------------------------------------------------------------

function InfoRow({ label, value }: { label: string; value: string }) {
  return (
    <div className="flex items-start gap-2 py-1.5 text-sm">
      <span className="min-w-[120px] flex-shrink-0 text-secondary-500 dark:text-secondary-400">
        {label}
      </span>
      <span className="text-secondary-900 dark:text-white">{value}</span>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Main Component
// ---------------------------------------------------------------------------

export default function ResultsDisplay({
  response,
  onDownloadReport,
}: ResultsDisplayProps) {
  const {
    part_analysis,
    material_recommendation,
    laminate_design,
    manufacturing_plan,
    cost_estimate,
    risk_assessment,
  } = response;

  return (
    <div className="space-y-4">
      {/* Download Banner */}
      <div className="flex items-center justify-between rounded-lg bg-primary-50 px-4 py-3 dark:bg-primary-900/20">
        <div>
          <h2 className="text-sm font-semibold text-primary-900 dark:text-primary-100">
            Analysis Complete
          </h2>
          <p className="text-xs text-primary-700 dark:text-primary-300">
            Review the results below. Download the full report as Markdown.
          </p>
        </div>
        <button
          onClick={onDownloadReport}
          className="flex items-center gap-1.5 rounded-lg bg-primary-800 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-primary-700 dark:bg-primary-700 dark:hover:bg-primary-600"
        >
          <Download size={16} />
          Download Report
        </button>
      </div>

      {/* 1. Part Analysis */}
      <Section
        title="Part Analysis"
        icon={<Box size={18} />}
        defaultOpen={true}
      >
        <div className="divide-y divide-secondary-100 dark:divide-secondary-700">
          {part_analysis.geometry_type && (
            <InfoRow label="Geometry" value={String(part_analysis.geometry_type)} />
          )}
          {part_analysis.dimensions && (
            <InfoRow label="Dimensions" value={String(part_analysis.dimensions)} />
          )}
          {part_analysis.curvature && (
            <InfoRow label="Curvature" value={String(part_analysis.curvature)} />
          )}
          {part_analysis.complexity && (
            <InfoRow label="Complexity" value={String(part_analysis.complexity)} />
          )}
          {part_analysis.load_paths &&
            Array.isArray(part_analysis.load_paths) &&
            part_analysis.load_paths.length > 0 && (
              <div className="py-1.5">
                <span className="text-sm text-secondary-500 dark:text-secondary-400">
                  Load Paths
                </span>
                <ul className="mt-1 space-y-0.5">
                  {part_analysis.load_paths.map((lp, i) => (
                    <li
                      key={i}
                      className="flex items-start gap-1.5 text-sm text-secondary-900 dark:text-white"
                    >
                      <span className="mt-1 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-primary-500" />
                      {lp}
                    </li>
                  ))}
                </ul>
              </div>
            )}
        </div>
      </Section>

      {/* 2. Material Recommendation */}
      <Section
        title="Material Recommendation"
        icon={<Atom size={18} />}
        defaultOpen={true}
      >
        <div className="space-y-4">
          <MaterialCard
            name={
              material_recommendation.fibre_type
                ? `${material_recommendation.fibre_type} / ${material_recommendation.resin_system || "Epoxy"}`
                : "Recommended Material"
            }
            fibreType={String(material_recommendation.fibre_form || material_recommendation.fibre_type || "Woven")}
            properties={[
              ...(material_recommendation.fibre_type
                ? [
                    {
                      label: "Fibre Type",
                      value: String(material_recommendation.fibre_type),
                    },
                  ]
                : []),
              ...(material_recommendation.fibre_form
                ? [
                    {
                      label: "Fibre Form",
                      value: String(material_recommendation.fibre_form),
                    },
                  ]
                : []),
              ...(material_recommendation.resin_system
                ? [
                    {
                      label: "Resin System",
                      value: String(material_recommendation.resin_system),
                    },
                  ]
                : []),
            ]}
          />

          {material_recommendation.reasoning &&
            Array.isArray(material_recommendation.reasoning) &&
            material_recommendation.reasoning.length > 0 && (
              <div>
                <p className="mb-1 text-xs font-medium text-secondary-600 dark:text-secondary-400">
                  Reasoning
                </p>
                <ul className="space-y-1">
                  {material_recommendation.reasoning.map((r, i) => (
                    <li
                      key={i}
                      className="flex items-start gap-1.5 text-sm text-secondary-700 dark:text-secondary-300"
                    >
                      <span className="mt-1 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-emerald-500" />
                      {r}
                    </li>
                  ))}
                </ul>
              </div>
            )}
        </div>
      </Section>

      {/* 3. Laminate Design */}
      <Section
        title="Laminate Design"
        icon={<Layers size={18} />}
        defaultOpen={true}
      >
        <div className="space-y-4">
          <div className="divide-y divide-secondary-100 dark:divide-secondary-700">
            {laminate_design.num_plies && (
              <InfoRow
                label="Number of Plies"
                value={String(laminate_design.num_plies)}
              />
            )}
            {laminate_design.thickness_mm && (
              <InfoRow
                label="Total Thickness"
                value={`${laminate_design.thickness_mm} mm`}
              />
            )}
          </div>

          {/* Stacking Visualizer */}
          {laminate_design.stacking_sequence &&
            Array.isArray(laminate_design.stacking_sequence) &&
            laminate_design.stacking_sequence.length > 0 && (
              <StackingVisualizer
                angles={laminate_design.stacking_sequence}
              />
            )}

          {laminate_design.reinforcements &&
            Array.isArray(laminate_design.reinforcements) &&
            laminate_design.reinforcements.length > 0 && (
              <div>
                <p className="mb-1 text-xs font-medium text-secondary-600 dark:text-secondary-400">
                  Reinforcements
                </p>
                <ul className="space-y-0.5">
                  {laminate_design.reinforcements.map((r, i) => (
                    <li
                      key={i}
                      className="text-sm text-secondary-700 dark:text-secondary-300"
                    >
                      -- {r}
                    </li>
                  ))}
                </ul>
              </div>
            )}
        </div>
      </Section>

      {/* 4. Manufacturing Plan */}
      <Section
        title="Manufacturing Plan"
        icon={<Wrench size={18} />}
        defaultOpen={true}
      >
        <div className="space-y-4">
          {manufacturing_plan.process && (
            <ProcessCard
              processName={String(manufacturing_plan.process)}
              suitabilityScore={0.85}
              reasoning={
                Array.isArray(manufacturing_plan.steps)
                  ? manufacturing_plan.steps.slice(0, 3)
                  : []
              }
              warnings={[]}
            />
          )}

          {/* Steps */}
          {manufacturing_plan.steps &&
            Array.isArray(manufacturing_plan.steps) &&
            manufacturing_plan.steps.length > 0 && (
              <div>
                <p className="mb-2 text-xs font-medium text-secondary-600 dark:text-secondary-400">
                  Manufacturing Steps
                </p>
                <ol className="space-y-2">
                  {manufacturing_plan.steps.map((step, i) => (
                    <li key={i} className="flex items-start gap-3 text-sm">
                      <span className="flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-full bg-primary-100 text-xs font-semibold text-primary-700 dark:bg-primary-900/30 dark:text-primary-400">
                        {i + 1}
                      </span>
                      <span className="text-secondary-700 dark:text-secondary-300">
                        {step}
                      </span>
                    </li>
                  ))}
                </ol>
              </div>
            )}

          {/* Materials List */}
          {manufacturing_plan.materials_list &&
            Array.isArray(manufacturing_plan.materials_list) &&
            manufacturing_plan.materials_list.length > 0 && (
              <div>
                <p className="mb-1 text-xs font-medium text-secondary-600 dark:text-secondary-400">
                  Materials Required
                </p>
                <ul className="grid grid-cols-1 gap-1 sm:grid-cols-2">
                  {manufacturing_plan.materials_list.map((mat, i) => (
                    <li
                      key={i}
                      className="flex items-center gap-1.5 rounded bg-secondary-50 px-2 py-1 text-xs text-secondary-700 dark:bg-secondary-700/50 dark:text-secondary-300"
                    >
                      <span className="h-1.5 w-1.5 rounded-full bg-primary-500" />
                      {mat}
                    </li>
                  ))}
                </ul>
              </div>
            )}

          {/* Consumables */}
          {manufacturing_plan.consumables &&
            Array.isArray(manufacturing_plan.consumables) &&
            manufacturing_plan.consumables.length > 0 && (
              <div>
                <p className="mb-1 text-xs font-medium text-secondary-600 dark:text-secondary-400">
                  Consumables
                </p>
                <ul className="grid grid-cols-1 gap-1 sm:grid-cols-2">
                  {manufacturing_plan.consumables.map((c, i) => (
                    <li
                      key={i}
                      className="flex items-center gap-1.5 rounded bg-secondary-50 px-2 py-1 text-xs text-secondary-700 dark:bg-secondary-700/50 dark:text-secondary-300"
                    >
                      <span className="h-1.5 w-1.5 rounded-full bg-amber-500" />
                      {c}
                    </li>
                  ))}
                </ul>
              </div>
            )}

          {/* Tooling Notes */}
          {manufacturing_plan.tooling_notes && (
            <div className="rounded bg-secondary-50 px-3 py-2 text-sm text-secondary-700 dark:bg-secondary-700/50 dark:text-secondary-300">
              <span className="font-medium">Tooling: </span>
              {manufacturing_plan.tooling_notes}
            </div>
          )}
        </div>
      </Section>

      {/* 5. Cost Estimate */}
      <Section
        title="Cost Estimate"
        icon={<DollarSign size={18} />}
        defaultOpen={true}
      >
        <CostBreakdownChart
          materialCost={cost_estimate.material_cost || 0}
          labourCost={cost_estimate.labour_cost || 0}
          toolingCost={cost_estimate.tooling_cost || 0}
          consumablesCost={cost_estimate.consumables_cost || 0}
          totalCost={cost_estimate.total_cost || 0}
          notes={
            Array.isArray(cost_estimate.breakdown_notes)
              ? cost_estimate.breakdown_notes
              : []
          }
        />
      </Section>

      {/* 6. Risk Assessment */}
      <Section
        title="Risk Assessment"
        icon={<ShieldAlert size={18} />}
        defaultOpen={false}
      >
        <div className="space-y-4">
          {/* Failure Modes */}
          {risk_assessment.failure_modes &&
            Array.isArray(risk_assessment.failure_modes) &&
            risk_assessment.failure_modes.length > 0 && (
              <div>
                <p className="mb-1 text-xs font-medium text-red-600 dark:text-red-400">
                  Potential Failure Modes
                </p>
                <ul className="space-y-1">
                  {risk_assessment.failure_modes.map((fm, i) => (
                    <li
                      key={i}
                      className="flex items-start gap-1.5 text-sm text-secondary-700 dark:text-secondary-300"
                    >
                      <span className="mt-1 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-red-500" />
                      {fm}
                    </li>
                  ))}
                </ul>
              </div>
            )}

          {/* Inspection Points */}
          {risk_assessment.inspection_points &&
            Array.isArray(risk_assessment.inspection_points) &&
            risk_assessment.inspection_points.length > 0 && (
              <div>
                <p className="mb-1 text-xs font-medium text-amber-600 dark:text-amber-400">
                  Inspection Points
                </p>
                <ul className="space-y-1">
                  {risk_assessment.inspection_points.map((ip, i) => (
                    <li
                      key={i}
                      className="flex items-start gap-1.5 text-sm text-secondary-700 dark:text-secondary-300"
                    >
                      <span className="mt-1 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-amber-500" />
                      {ip}
                    </li>
                  ))}
                </ul>
              </div>
            )}

          {/* Safety Factors */}
          {risk_assessment.safety_factors && (
            <div className="rounded bg-secondary-50 px-3 py-2 text-sm dark:bg-secondary-700/50">
              <span className="font-medium text-secondary-700 dark:text-secondary-300">
                Safety Factors:{" "}
              </span>
              <span className="text-secondary-600 dark:text-secondary-400">
                {risk_assessment.safety_factors}
              </span>
            </div>
          )}

          {/* Common Defects */}
          {risk_assessment.common_defects &&
            Array.isArray(risk_assessment.common_defects) &&
            risk_assessment.common_defects.length > 0 && (
              <div>
                <p className="mb-1 text-xs font-medium text-secondary-600 dark:text-secondary-400">
                  Common Defects to Watch For
                </p>
                <ul className="space-y-1">
                  {risk_assessment.common_defects.map((cd, i) => (
                    <li
                      key={i}
                      className="flex items-start gap-1.5 text-sm text-secondary-700 dark:text-secondary-300"
                    >
                      <span className="mt-1 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-secondary-400" />
                      {cd}
                    </li>
                  ))}
                </ul>
              </div>
            )}
        </div>
      </Section>

      {/* Disclaimer */}
      <p className="text-center text-xs text-secondary-400 dark:text-secondary-500">
        This tool provides preliminary design guidance only. Always verify with a
        qualified composites engineer.
      </p>
    </div>
  );
}
