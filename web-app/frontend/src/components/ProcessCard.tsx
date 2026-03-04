import { Factory, AlertTriangle, ExternalLink } from "lucide-react";

interface ProcessCardProps {
  processName: string;
  suitabilityScore: number;
  reasoning: string[];
  warnings: string[];
  knowledgeBaseLink?: string;
}

function scoreColor(score: number): string {
  if (score >= 0.8) return "text-emerald-600 dark:text-emerald-400";
  if (score >= 0.5) return "text-amber-600 dark:text-amber-400";
  return "text-red-600 dark:text-red-400";
}

function barColor(score: number): string {
  if (score >= 0.8) return "bg-emerald-500";
  if (score >= 0.5) return "bg-amber-500";
  return "bg-red-500";
}

export default function ProcessCard({
  processName,
  suitabilityScore,
  reasoning,
  warnings,
  knowledgeBaseLink,
}: ProcessCardProps) {
  const percentage = Math.round(suitabilityScore * 100);

  return (
    <div className="rounded-lg border border-secondary-200 bg-white p-4 transition-shadow hover:shadow-md dark:border-secondary-700 dark:bg-secondary-800">
      {/* Header */}
      <div className="flex items-start justify-between">
        <div className="flex items-center gap-2">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary-50 text-primary-700 dark:bg-primary-900/30 dark:text-primary-400">
            <Factory size={18} />
          </div>
          <h3 className="text-sm font-semibold text-secondary-900 dark:text-white">
            {processName}
          </h3>
        </div>
        <span className={`text-sm font-bold ${scoreColor(suitabilityScore)}`}>
          {percentage}%
        </span>
      </div>

      {/* Suitability Bar */}
      <div className="mt-3">
        <div className="flex items-center justify-between text-xs text-secondary-500 dark:text-secondary-400">
          <span>Suitability</span>
          <span>{percentage}%</span>
        </div>
        <div className="mt-1 h-2 overflow-hidden rounded-full bg-secondary-100 dark:bg-secondary-700">
          <div
            className={`h-full rounded-full transition-all ${barColor(suitabilityScore)}`}
            style={{ width: `${percentage}%` }}
          />
        </div>
      </div>

      {/* Reasoning */}
      {reasoning.length > 0 && (
        <ul className="mt-3 space-y-1">
          {reasoning.map((reason, i) => (
            <li
              key={i}
              className="flex gap-1.5 text-xs text-secondary-600 dark:text-secondary-400"
            >
              <span className="mt-0.5 flex-shrink-0 text-emerald-500">+</span>
              {reason}
            </li>
          ))}
        </ul>
      )}

      {/* Warnings */}
      {warnings.length > 0 && (
        <div className="mt-3 space-y-1">
          {warnings.map((warning, i) => (
            <div
              key={i}
              className="flex items-start gap-1.5 text-xs text-amber-700 dark:text-amber-400"
            >
              <AlertTriangle
                size={12}
                className="mt-0.5 flex-shrink-0"
              />
              {warning}
            </div>
          ))}
        </div>
      )}

      {/* Knowledge Base Link */}
      {knowledgeBaseLink && (
        <a
          href={knowledgeBaseLink}
          target="_blank"
          rel="noopener noreferrer"
          className="mt-3 inline-flex items-center gap-1 text-xs font-medium text-primary-600 transition-colors hover:text-primary-800 dark:text-primary-400 dark:hover:text-primary-300"
        >
          <ExternalLink size={12} />
          Read more in knowledge base
        </a>
      )}
    </div>
  );
}
