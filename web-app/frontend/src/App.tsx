import { useState, useCallback } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomePage from "./pages/HomePage";
import AnalyzePage from "./pages/AnalyzePage";
import ResultsPage from "./pages/ResultsPage";
import KnowledgeBasePage from "./pages/KnowledgeBasePage";
import { analyzePartAsync, ApiError } from "./api/client";
import type { Page, AnalysisRequest, AnalysisResponse } from "./types";

export default function App() {
  const [currentPage, setCurrentPage] = useState<Page>("home");
  const [analysisResponse, setAnalysisResponse] =
    useState<AnalysisResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const navigate = useCallback((page: Page) => {
    setCurrentPage(page);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, []);

  const handleAnalysisSubmit = useCallback(
    async (request: AnalysisRequest) => {
      setIsLoading(true);
      setError(null);

      try {
        const apiKey = localStorage.getItem("anthropic_api_key");
        const response = await analyzePartAsync(request, apiKey);
        setAnalysisResponse(response);
        navigate("results");
      } catch (err) {
        if (err instanceof ApiError) {
          setError(err.detail);
        } else if (err instanceof Error) {
          setError(err.message);
        } else {
          setError("An unexpected error occurred. Please try again.");
        }
      } finally {
        setIsLoading(false);
      }
    },
    [navigate]
  );

  return (
    <div className="flex min-h-screen flex-col bg-white dark:bg-secondary-900">
      <Header currentPage={currentPage} onNavigate={navigate} />

      <main className="flex-1">
        {currentPage === "home" && <HomePage onNavigate={navigate} />}

        {currentPage === "analyze" && (
          <AnalyzePage
            onSubmit={handleAnalysisSubmit}
            isLoading={isLoading}
            error={error}
          />
        )}

        {currentPage === "knowledge" && (
          <KnowledgeBasePage onNavigate={navigate} />
        )}

        {currentPage === "results" && analysisResponse && (
          <ResultsPage response={analysisResponse} onNavigate={navigate} />
        )}

        {/* Fallback: if on results page but no response, redirect to analyze */}
        {currentPage === "results" && !analysisResponse && (
          <AnalyzePage
            onSubmit={handleAnalysisSubmit}
            isLoading={isLoading}
            error={error}
          />
        )}
      </main>

      <Footer />
    </div>
  );
}
