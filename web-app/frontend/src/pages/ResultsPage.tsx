import { ArrowLeft, RotateCcw } from "lucide-react";
import ResultsDisplay from "../components/ResultsDisplay";
import FeedbackButton from "../components/FeedbackButton";
import type { AnalysisResponse, Page } from "../types";

interface ResultsPageProps {
  response: AnalysisResponse;
  onNavigate: (page: Page) => void;
}

export default function ResultsPage({
  response,
  onNavigate,
}: ResultsPageProps) {
  function handleDownloadReport() {
    const markdown = response.report_markdown;
    if (!markdown) return;

    const blob = new Blob([markdown], { type: "text/markdown;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "composites-manufacturing-plan.md";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }

  return (
    <div className="animate-fade-in mx-auto max-w-3xl px-4 py-8">
      {/* Navigation */}
      <div className="mb-6 flex items-center justify-between">
        <button
          onClick={() => onNavigate("analyze")}
          className="flex items-center gap-1.5 text-sm text-secondary-600 transition-colors hover:text-secondary-900 dark:text-secondary-400 dark:hover:text-white"
        >
          <ArrowLeft size={16} />
          Back to Analysis
        </button>
        <button
          onClick={() => onNavigate("analyze")}
          className="flex items-center gap-1.5 rounded-lg border border-secondary-300 bg-white px-3 py-2 text-sm font-medium text-secondary-700 transition-colors hover:bg-secondary-50 dark:border-secondary-600 dark:bg-secondary-800 dark:text-secondary-300 dark:hover:bg-secondary-700"
        >
          <RotateCcw size={14} />
          Start New Analysis
        </button>
      </div>

      {/* Results */}
      <ResultsDisplay
        response={response}
        onDownloadReport={handleDownloadReport}
      />

      <FeedbackButton context="analysis-results" />
    </div>
  );
}
