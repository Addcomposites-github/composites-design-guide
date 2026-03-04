import type {
  AnalysisRequest,
  AnalysisResponse,
  MaterialResponse,
  ProcessRecommendationRequest,
  ProcessRecommendationResponse,
  CostEstimateRequest,
  CostEstimateResponse,
  SearchResponse,
  StackingCheckRequest,
  StackingCheckResponse,
} from "../types";

const BASE_URL = import.meta.env.VITE_API_URL || "";

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

class ApiError extends Error {
  status: number;
  detail: string;

  constructor(status: number, detail: string) {
    super(`API Error ${status}: ${detail}`);
    this.name = "ApiError";
    this.status = status;
    this.detail = detail;
  }
}

async function request<T>(
  path: string,
  options: RequestInit = {}
): Promise<T> {
  const url = `${BASE_URL}${path}`;

  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(options.headers as Record<string, string> | undefined),
  };

  const response = await fetch(url, {
    ...options,
    headers,
  });

  if (!response.ok) {
    let detail = response.statusText;
    try {
      const body = await response.json();
      detail = body.detail || body.message || JSON.stringify(body);
    } catch {
      // use statusText
    }
    throw new ApiError(response.status, detail);
  }

  return response.json() as Promise<T>;
}

// ---------------------------------------------------------------------------
// API Functions
// ---------------------------------------------------------------------------

/**
 * Submit a part for full analysis (Photo-to-Plan).
 * POST /api/analyze
 */
export async function analyzePartAsync(
  req: AnalysisRequest,
  apiKey?: string | null
): Promise<AnalysisResponse> {
  const extraHeaders: Record<string, string> = {};
  if (apiKey) {
    extraHeaders["X-Anthropic-Key"] = apiKey;
  }
  return request<AnalysisResponse>("/api/analyze", {
    method: "POST",
    body: JSON.stringify(req),
    headers: extraHeaders,
  });
}

/**
 * Search the material database.
 * GET /api/materials?query=...
 */
export async function searchMaterials(
  query: string
): Promise<MaterialResponse> {
  const params = new URLSearchParams({ query });
  return request<MaterialResponse>(`/api/materials?${params.toString()}`);
}

/**
 * Get ranked process recommendations.
 * POST /api/processes/recommend
 */
export async function recommendProcesses(
  req: ProcessRecommendationRequest
): Promise<ProcessRecommendationResponse> {
  return request<ProcessRecommendationResponse>(
    "/api/processes/recommend",
    {
      method: "POST",
      body: JSON.stringify(req),
    }
  );
}

/**
 * Estimate per-part manufacturing cost.
 * POST /api/estimate-cost
 */
export async function estimateCost(
  req: CostEstimateRequest
): Promise<CostEstimateResponse> {
  return request<CostEstimateResponse>("/api/estimate-cost", {
    method: "POST",
    body: JSON.stringify(req),
  });
}

/**
 * Search the composites knowledge base.
 * GET /api/search?query=...&top_n=...
 */
export async function searchKnowledge(
  query: string,
  topN: number = 5
): Promise<SearchResponse> {
  const params = new URLSearchParams({
    query,
    top_n: String(topN),
  });
  return request<SearchResponse>(`/api/search?${params.toString()}`);
}

/**
 * Verify a stacking sequence against laminate design rules.
 * POST /api/check-stacking
 */
export async function checkStacking(
  angles: number[],
  maxConsecutive: number = 4
): Promise<StackingCheckResponse> {
  const body: StackingCheckRequest = {
    angles,
    max_consecutive: maxConsecutive,
  };
  return request<StackingCheckResponse>("/api/check-stacking", {
    method: "POST",
    body: JSON.stringify(body),
  });
}

/**
 * Fetch a single knowledge base article by directory and filename.
 * GET /api/article/{dir}/{filename}
 */
export async function getArticle(
  dir: string,
  filename: string
): Promise<{ title: string; directory: string; filename: string; content: string }> {
  return request(`/api/article/${encodeURIComponent(dir)}/${encodeURIComponent(filename)}`);
}

export { ApiError };
