import { AlertCircle, Info } from "lucide-react";
import AnalysisForm from "../components/AnalysisForm";
import ApiKeyInput from "../components/ApiKeyInput";
import type { AnalysisRequest } from "../types";

interface AnalyzePageProps {
  onSubmit: (request: AnalysisRequest) => void;
  isLoading: boolean;
  error: string | null;
}

export default function AnalyzePage({
  onSubmit,
  isLoading,
  error,
}: AnalyzePageProps) {
  return (
    <div className="animate-fade-in mx-auto max-w-2xl px-4 py-10">
      {/* Page Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-extrabold tracking-tight text-secondary-900 dark:text-white">
          Analyze Your Part
        </h1>
        <p className="mt-2 text-[15px] leading-relaxed text-secondary-500 dark:text-secondary-400">
          Describe the composite part you want to build. The AI agent will
          generate a complete manufacturing plan including material selection,
          laminate design, process recommendation, and cost estimate.
        </p>
      </div>

      {/* API Key Input */}
      <ApiKeyInput />

      {/* Info Box */}
      <div className="mb-6 flex gap-3 rounded-2xl border border-primary-100 bg-primary-50/50 px-5 py-4 dark:border-primary-800/40 dark:bg-primary-900/10">
        <Info
          size={18}
          className="mt-0.5 flex-shrink-0 text-primary-500 dark:text-primary-400"
        />
        <div className="text-[13px] text-primary-700/80 dark:text-primary-300/80">
          <p className="font-semibold text-primary-700 dark:text-primary-300">How it works</p>
          <ol className="mt-1.5 list-inside list-decimal space-y-1">
            <li>Describe your part geometry and intended use</li>
            <li>Optionally upload a reference photo</li>
            <li>
              The AI analyses your requirements against our composites knowledge
              base
            </li>
            <li>
              You receive a complete manufacturing plan with materials, process,
              stacking sequence, and cost estimate
            </li>
          </ol>
        </div>
      </div>

      {/* Error Display */}
      {error && (
        <div className="mb-6 flex gap-3 rounded-2xl border border-red-200/60 bg-red-50/50 px-5 py-4 dark:border-red-800/40 dark:bg-red-900/10">
          <AlertCircle
            size={18}
            className="mt-0.5 flex-shrink-0 text-red-500 dark:text-red-400"
          />
          <div className="text-sm text-red-700 dark:text-red-300">
            <p className="font-semibold">Analysis Failed</p>
            <p className="mt-0.5 text-[13px] text-red-600/80 dark:text-red-300/80">{error}</p>
          </div>
        </div>
      )}

      {/* Form Card */}
      <div className="rounded-2xl border border-secondary-100 bg-white p-6 shadow-sm dark:border-secondary-700/60 dark:bg-secondary-800/50">
        <AnalysisForm onSubmit={onSubmit} isLoading={isLoading} />
      </div>

      {/* Disclaimer */}
      <p className="mt-6 text-center text-[11px] text-secondary-300 dark:text-secondary-600">
        This tool provides preliminary design guidance only. Always verify with
        a qualified composites engineer.
      </p>
    </div>
  );
}
