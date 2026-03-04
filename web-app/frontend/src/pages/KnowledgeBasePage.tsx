import { useState, useCallback } from "react";
import ReactMarkdown from "react-markdown";
import {
  Search,
  BookOpen,
  Layers,
  Factory,
  FlaskConical,
  Monitor,
  Wrench,
  Atom,
  Loader2,
  Tag,
  ExternalLink,
  AlertCircle,
  ChevronRight,
  Pencil,
  X,
  ArrowLeft,
} from "lucide-react";
import { searchKnowledge, searchMaterials, getArticle, ApiError } from "../api/client";
import FeedbackButton from "../components/FeedbackButton";
import type {
  Page,
  SearchResult,
  MaterialRecord,
} from "../types";

// ---------------------------------------------------------------------------
// Quick-link section data
// ---------------------------------------------------------------------------

interface SectionLink {
  icon: React.ReactNode;
  title: string;
  description: string;
  searchQuery: string;
}

const sections: SectionLink[] = [
  {
    icon: <BookOpen size={22} />,
    title: "Fundamentals",
    description:
      "Fibres, resins, laminates, and failure modes explained simply.",
    searchQuery: "composites fundamentals fibres resins laminates",
  },
  {
    icon: <Layers size={22} />,
    title: "Design Rules",
    description:
      "Stacking sequences, ply drop-offs, splices, zone design, and DFM.",
    searchQuery: "stacking sequences ply drop-off design rules",
  },
  {
    icon: <Factory size={22} />,
    title: "Manufacturing",
    description:
      "Wet layup, vacuum bagging, infusion, prepreg, AFP, and common defects.",
    searchQuery: "manufacturing process wet layup vacuum bagging infusion prepreg",
  },
  {
    icon: <FlaskConical size={22} />,
    title: "Structural Analysis",
    description:
      "Panel sizing, failure criteria, buckling, and sandwich structures.",
    searchQuery: "structural analysis failure criteria buckling sandwich",
  },
  {
    icon: <Monitor size={22} />,
    title: "CATIA Workflows",
    description:
      "Ply creation, zone management, stacking, flat patterns, and ply books.",
    searchQuery: "CATIA ply creation zone stacking flat pattern",
  },
  {
    icon: <Wrench size={22} />,
    title: "Free Tools",
    description:
      "AddStack, eLamX2, CompositesAI, and other open resources.",
    searchQuery: "free tools AddStack eLamX2 composites calculator",
  },
];

// ---------------------------------------------------------------------------
// Difficulty badge colours
// ---------------------------------------------------------------------------

function difficultyColor(difficulty: string): string {
  switch (difficulty) {
    case "beginner":
      return "bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400";
    case "intermediate":
      return "bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400";
    case "advanced":
      return "bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400";
    default:
      return "bg-secondary-100 text-secondary-600 dark:bg-secondary-700 dark:text-secondary-400";
  }
}

function categoryColor(_category: string): string {
  return "bg-primary-100 text-primary-700 dark:bg-primary-900/30 dark:text-primary-300";
}

// ---------------------------------------------------------------------------
// Sub-components
// ---------------------------------------------------------------------------

function SearchResultCard({
  result,
  onOpenArticle,
}: {
  result: SearchResult;
  onOpenArticle: (dir: string, file: string) => void;
}) {
  const githubUrl = result.url
    ? `https://github.com/addcomposites/composites-design-guide/blob/master/${result.url}`
    : undefined;

  return (
    <button
      type="button"
      onClick={() => {
        if (result.dir && result.file) {
          onOpenArticle(result.dir, result.file);
        }
      }}
      className="group block w-full cursor-pointer rounded-2xl border border-secondary-100 bg-white p-5 text-left transition-all duration-200 hover:-translate-y-0.5 hover:border-primary-200/60 hover:shadow-lg hover:shadow-primary-500/5 dark:border-secondary-700/60 dark:bg-secondary-800/50 dark:hover:border-primary-700/40"
    >
      <div className="mb-2.5 flex flex-wrap items-center gap-2">
        {result.category && (
          <span
            className={`rounded-full px-2.5 py-0.5 text-[11px] font-medium ${categoryColor(result.category)}`}
          >
            {result.category}
          </span>
        )}
        {result.difficulty && (
          <span
            className={`rounded-full px-2.5 py-0.5 text-[11px] font-medium ${difficultyColor(result.difficulty)}`}
          >
            {result.difficulty}
          </span>
        )}
        <span className="ml-auto text-[11px] font-medium text-secondary-300 dark:text-secondary-600">
          {result.score.toFixed(0)}% match
        </span>
      </div>

      <h3 className="text-[15px] font-semibold text-secondary-900 group-hover:text-primary-700 dark:text-white dark:group-hover:text-primary-400">
        {result.title}
      </h3>

      <p className="mt-1.5 text-[13px] leading-relaxed text-secondary-500 dark:text-secondary-400">
        {result.snippet}
      </p>

      {result.tags.length > 0 && (
        <div className="mt-3 flex flex-wrap gap-1.5">
          {result.tags.map((tag) => (
            <span
              key={tag}
              className="inline-flex items-center gap-0.5 rounded-full bg-secondary-50 px-2 py-0.5 text-[10px] font-medium text-secondary-400 ring-1 ring-secondary-100 dark:bg-secondary-700/30 dark:text-secondary-500 dark:ring-secondary-700/50"
            >
              <Tag size={9} />
              {tag}
            </span>
          ))}
        </div>
      )}

      <div className="mt-3 flex items-center gap-3">
        <span className="inline-flex items-center gap-1 text-[11px] font-medium text-primary-600 dark:text-primary-400">
          <BookOpen size={10} />
          Read article
        </span>
        {githubUrl && (
          <span
            onClick={(e) => {
              e.stopPropagation();
              window.open(githubUrl, "_blank", "noopener,noreferrer");
            }}
            className="inline-flex items-center gap-1 text-[11px] font-medium text-secondary-400 opacity-0 transition-all group-hover:opacity-100 hover:text-primary-600 dark:text-secondary-500 dark:hover:text-primary-400"
          >
            <ExternalLink size={10} />
            GitHub
          </span>
        )}
        {result.url && (
          <span
            onClick={(e) => {
              e.stopPropagation();
              window.open(
                `https://github.com/addcomposites/composites-design-guide/edit/master/${result.url}`,
                "_blank",
                "noopener,noreferrer"
              );
            }}
            className="inline-flex items-center gap-1 text-[11px] font-medium text-secondary-400 opacity-0 transition-all group-hover:opacity-100 hover:text-primary-600 dark:text-secondary-500 dark:hover:text-primary-400"
          >
            <Pencil size={10} />
            Improve
          </span>
        )}
      </div>
    </button>
  );
}

// ---------------------------------------------------------------------------
// Article viewer overlay
// ---------------------------------------------------------------------------

function ArticleViewer({
  title,
  content,
  onClose,
}: {
  title: string;
  content: string;
  onClose: () => void;
}) {
  // Strip YAML front matter for display
  let body = content;
  if (body.startsWith("---")) {
    const parts = body.split("---", 3);
    if (parts.length >= 3) {
      body = parts.slice(2).join("---").trim();
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center overflow-y-auto bg-black/40 backdrop-blur-sm">
      <div className="relative mx-4 my-8 w-full max-w-3xl rounded-2xl border border-secondary-200 bg-white shadow-2xl dark:border-secondary-700 dark:bg-secondary-900">
        {/* Header */}
        <div className="sticky top-0 z-10 flex items-center gap-3 rounded-t-2xl border-b border-secondary-100 bg-white/95 px-6 py-4 backdrop-blur-sm dark:border-secondary-700 dark:bg-secondary-900/95">
          <button
            onClick={onClose}
            className="flex h-8 w-8 items-center justify-center rounded-lg text-secondary-400 transition-colors hover:bg-secondary-100 hover:text-secondary-700 dark:hover:bg-secondary-800 dark:hover:text-secondary-200"
          >
            <ArrowLeft size={18} />
          </button>
          <h2 className="flex-1 truncate text-lg font-bold text-secondary-900 dark:text-white">
            {title}
          </h2>
          <button
            onClick={onClose}
            className="flex h-8 w-8 items-center justify-center rounded-lg text-secondary-400 transition-colors hover:bg-secondary-100 hover:text-secondary-700 dark:hover:bg-secondary-800 dark:hover:text-secondary-200"
          >
            <X size={18} />
          </button>
        </div>

        {/* Article content */}
        <div className="prose prose-sm prose-secondary max-w-none px-6 py-6 dark:prose-invert prose-headings:text-secondary-900 prose-p:text-secondary-600 prose-a:text-primary-600 prose-strong:text-secondary-800 dark:prose-headings:text-white dark:prose-p:text-secondary-300 dark:prose-a:text-primary-400 dark:prose-strong:text-secondary-200">
          <ReactMarkdown>{body}</ReactMarkdown>
        </div>
      </div>
    </div>
  );
}

function MaterialCard({ material }: { material: MaterialRecord }) {
  // Map from actual API response structure (nested properties, resin_family, cost_usd_per_kg)
  const props = (material as Record<string, unknown>).properties as
    | Record<string, number>
    | undefined;
  const resin =
    (material as Record<string, unknown>).resin_family as string | undefined;
  const costRange = (material as Record<string, unknown>).cost_usd_per_kg as
    | { low: number; high: number }
    | undefined;
  const form = (material as Record<string, unknown>).form as string | undefined;

  return (
    <div className="rounded-2xl border border-secondary-100 bg-white p-5 transition-all duration-200 hover:-translate-y-0.5 hover:border-primary-200/60 hover:shadow-lg hover:shadow-primary-500/5 dark:border-secondary-700/60 dark:bg-secondary-800/50 dark:hover:border-primary-700/40">
      <h3 className="mb-1 text-sm font-semibold text-secondary-900 dark:text-white">
        {material.name}
      </h3>
      {form && (
        <p className="mb-3 text-[11px] font-medium text-primary-600 dark:text-primary-400">
          {form}
        </p>
      )}

      <div className="grid grid-cols-2 gap-x-4 gap-y-1.5 text-[13px]">
        <div className="text-secondary-500 dark:text-secondary-400">
          Fibre
        </div>
        <div className="font-medium text-secondary-700 dark:text-secondary-300">
          {material.fibre_type}
        </div>

        <div className="text-secondary-500 dark:text-secondary-400">
          Resin
        </div>
        <div className="font-medium text-secondary-700 dark:text-secondary-300">
          {resin ?? "—"}
        </div>

        <div className="text-secondary-500 dark:text-secondary-400">
          E1
        </div>
        <div className="font-medium text-secondary-700 dark:text-secondary-300">
          {props?.E1_GPa ?? "—"} GPa
        </div>

        <div className="text-secondary-500 dark:text-secondary-400">
          E2
        </div>
        <div className="font-medium text-secondary-700 dark:text-secondary-300">
          {props?.E2_GPa ?? "—"} GPa
        </div>

        <div className="text-secondary-500 dark:text-secondary-400">
          Tensile
        </div>
        <div className="font-medium text-secondary-700 dark:text-secondary-300">
          {props?.Xt_MPa ?? "—"} MPa
        </div>

        <div className="text-secondary-500 dark:text-secondary-400">
          Compressive
        </div>
        <div className="font-medium text-secondary-700 dark:text-secondary-300">
          {props?.Xc_MPa ?? "—"} MPa
        </div>

        <div className="text-secondary-500 dark:text-secondary-400">
          Cost
        </div>
        <div className="font-medium text-secondary-700 dark:text-secondary-300">
          {costRange
            ? `$${costRange.low}–$${costRange.high}/kg`
            : "—"}
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Main page
// ---------------------------------------------------------------------------

interface KnowledgeBasePageProps {
  onNavigate: (page: Page) => void;
}

export default function KnowledgeBasePage({ onNavigate }: KnowledgeBasePageProps) {
  // Knowledge search state
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  const [isSearching, setIsSearching] = useState(false);
  const [searchError, setSearchError] = useState<string | null>(null);
  const [hasSearched, setHasSearched] = useState(false);

  // Article viewer state
  const [articleOpen, setArticleOpen] = useState(false);
  const [articleTitle, setArticleTitle] = useState("");
  const [articleContent, setArticleContent] = useState("");
  const [articleLoading, setArticleLoading] = useState(false);

  // Materials browser state
  const [materialQuery, setMaterialQuery] = useState("");
  const [materials, setMaterials] = useState<MaterialRecord[]>([]);
  const [isMaterialLoading, setIsMaterialLoading] = useState(false);
  const [materialError, setMaterialError] = useState<string | null>(null);
  const [hasMaterialSearched, setHasMaterialSearched] = useState(false);

  // --------------------------------------------------
  // Knowledge search handler
  // --------------------------------------------------

  const handleSearch = useCallback(
    async (query?: string) => {
      const q = (query ?? searchQuery).trim();
      if (!q) return;

      // When triggered by a section click, update the input field to match
      if (query) {
        setSearchQuery(q);
      }

      setIsSearching(true);
      setSearchError(null);
      setHasSearched(true);

      try {
        const response = await searchKnowledge(q, 10);
        setSearchResults(response.results);
      } catch (err) {
        if (err instanceof ApiError) {
          setSearchError(err.detail);
        } else if (err instanceof Error) {
          setSearchError(err.message);
        } else {
          setSearchError("An unexpected error occurred. Please try again.");
        }
        setSearchResults([]);
      } finally {
        setIsSearching(false);
      }
    },
    [searchQuery]
  );

  const handleSearchSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      handleSearch();
    },
    [handleSearch]
  );

  const handleSectionClick = useCallback(
    (query: string) => {
      setSearchQuery(query);
      handleSearch(query);
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
    [handleSearch]
  );

  // --------------------------------------------------
  // Materials search handler
  // --------------------------------------------------

  const handleMaterialSearch = useCallback(async () => {
    const q = materialQuery.trim();
    if (!q) return;

    setIsMaterialLoading(true);
    setMaterialError(null);
    setHasMaterialSearched(true);

    try {
      const response = await searchMaterials(q);
      setMaterials(response.materials);
    } catch (err) {
      if (err instanceof ApiError) {
        setMaterialError(err.detail);
      } else if (err instanceof Error) {
        setMaterialError(err.message);
      } else {
        setMaterialError("An unexpected error occurred. Please try again.");
      }
      setMaterials([]);
    } finally {
      setIsMaterialLoading(false);
    }
  }, [materialQuery]);

  const handleMaterialSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      handleMaterialSearch();
    },
    [handleMaterialSearch]
  );

  // --------------------------------------------------
  // Article viewer handler
  // --------------------------------------------------

  const handleOpenArticle = useCallback(async (dir: string, file: string) => {
    setArticleLoading(true);
    setArticleOpen(true);
    try {
      const article = await getArticle(dir, file);
      setArticleTitle(article.title);
      setArticleContent(article.content);
    } catch {
      setArticleTitle("Error");
      setArticleContent("Failed to load article. Please try again.");
    } finally {
      setArticleLoading(false);
    }
  }, []);

  const handleCloseArticle = useCallback(() => {
    setArticleOpen(false);
    setArticleTitle("");
    setArticleContent("");
  }, []);

  // Suppress unused variable warning
  void onNavigate;

  // --------------------------------------------------
  // Render
  // --------------------------------------------------

  return (
    <div className="animate-fade-in">
      {/* --------------------------------------------------------- */}
      {/* Hero / Search Section                                     */}
      {/* --------------------------------------------------------- */}
      <section className="bg-mesh bg-grid px-4 py-14 dark:bg-secondary-800/50">
        <div className="mx-auto max-w-3xl text-center">
          <h1 className="text-3xl font-extrabold tracking-tight text-secondary-900 sm:text-4xl dark:text-white">
            Knowledge Base
          </h1>
          <p className="mt-2 text-[15px] text-secondary-500 dark:text-secondary-400">
            Search our open-source composites design guide. 56 articles
            covering fibres, resins, manufacturing, analysis, and more.
          </p>

          {/* Search Form */}
          <form
            onSubmit={handleSearchSubmit}
            className="mx-auto mt-7 flex max-w-xl gap-2"
          >
            <div className="relative flex-1">
              <Search
                size={16}
                className="absolute left-3.5 top-1/2 -translate-y-1/2 text-secondary-300 dark:text-secondary-500"
              />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search topics, e.g. &quot;vacuum bagging&quot; or &quot;ply drop-off&quot;"
                className="w-full rounded-full border border-secondary-200 bg-white/80 py-2.5 pl-10 pr-4 text-sm text-secondary-900 shadow-sm backdrop-blur-sm placeholder:text-secondary-400 focus:border-primary-400 focus:outline-none focus:ring-2 focus:ring-primary-500/20 dark:border-secondary-600 dark:bg-secondary-800/80 dark:text-white dark:placeholder:text-secondary-500 dark:focus:border-primary-400 dark:focus:ring-primary-400/20"
              />
            </div>
            <button
              type="submit"
              disabled={isSearching || !searchQuery.trim()}
              className="flex items-center gap-1.5 rounded-full bg-gradient-to-r from-primary-700 to-primary-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition-all hover:shadow-md hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-50 dark:from-primary-600 dark:to-primary-500"
            >
              {isSearching ? (
                <Loader2 size={16} className="animate-spin" />
              ) : (
                <Search size={16} />
              )}
              Search
            </button>
          </form>
        </div>
      </section>

      {/* --------------------------------------------------------- */}
      {/* Search Results                                            */}
      {/* --------------------------------------------------------- */}
      {hasSearched && (
        <section className="mx-auto max-w-3xl px-4 py-8">
          <h2 className="mb-4 text-lg font-bold text-secondary-900 dark:text-white">
            Search Results
            {!isSearching && (
              <span className="ml-2 text-sm font-normal text-secondary-500 dark:text-secondary-400">
                ({searchResults.length} found)
              </span>
            )}
          </h2>

          {searchError && (
            <div className="mb-4 flex gap-3 rounded-lg border border-red-200 bg-red-50 px-4 py-3 dark:border-red-800 dark:bg-red-900/20">
              <AlertCircle
                size={18}
                className="mt-0.5 flex-shrink-0 text-red-600 dark:text-red-400"
              />
              <p className="text-sm text-red-700 dark:text-red-300">
                {searchError}
              </p>
            </div>
          )}

          {isSearching && (
            <div className="flex items-center justify-center py-12">
              <Loader2
                size={28}
                className="animate-spin text-primary-600 dark:text-primary-400"
              />
            </div>
          )}

          {!isSearching && !searchError && searchResults.length === 0 && (
            <p className="py-8 text-center text-sm text-secondary-500 dark:text-secondary-400">
              No results found. Try different keywords.
            </p>
          )}

          {!isSearching && searchResults.length > 0 && (
            <div className="space-y-3">
              {searchResults.map((result, idx) => (
                <SearchResultCard key={`${result.url}-${idx}`} result={result} onOpenArticle={handleOpenArticle} />
              ))}
              <FeedbackButton context="knowledge-search" />
            </div>
          )}
        </section>
      )}

      {/* --------------------------------------------------------- */}
      {/* Quick Link Sections                                       */}
      {/* --------------------------------------------------------- */}
      <section className="mx-auto max-w-5xl px-4 py-16">
        <div className="mb-8 text-center">
          <h2 className="text-2xl font-bold tracking-tight text-secondary-900 dark:text-white">
            Browse by Topic
          </h2>
          <p className="mt-2 text-sm text-secondary-500 dark:text-secondary-400">
            Click any topic to search related articles
          </p>
        </div>
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {sections.map((section) => (
            <button
              key={section.title}
              onClick={() => handleSectionClick(section.searchQuery)}
              className="group flex items-start gap-3 rounded-2xl border border-secondary-100 bg-white p-5 text-left transition-all duration-200 hover:-translate-y-0.5 hover:border-primary-200/60 hover:shadow-lg hover:shadow-primary-500/5 dark:border-secondary-700/60 dark:bg-secondary-800/50 dark:hover:border-primary-700/40"
            >
              <div className="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-xl bg-gradient-to-br from-primary-50 to-primary-100 text-primary-600 ring-1 ring-primary-200/40 transition-transform group-hover:scale-110 dark:from-primary-900/30 dark:to-primary-800/20 dark:text-primary-400 dark:ring-primary-700/30">
                {section.icon}
              </div>
              <div className="flex-1">
                <h3 className="text-sm font-semibold text-secondary-900 dark:text-white">
                  {section.title}
                </h3>
                <p className="mt-0.5 text-[13px] leading-relaxed text-secondary-500 dark:text-secondary-400">
                  {section.description}
                </p>
              </div>
              <ChevronRight
                size={16}
                className="mt-1 flex-shrink-0 text-secondary-200 transition-all group-hover:translate-x-0.5 group-hover:text-primary-500 dark:text-secondary-700 dark:group-hover:text-primary-400"
              />
            </button>
          ))}
        </div>
      </section>

      {/* --------------------------------------------------------- */}
      {/* Materials Browser                                         */}
      {/* --------------------------------------------------------- */}
      <section className="relative overflow-hidden px-4 py-16">
        <div className="absolute inset-0 bg-gradient-to-b from-secondary-50/80 to-white dark:from-secondary-800/30 dark:to-secondary-900" />
        <div className="relative z-10 mx-auto max-w-5xl">
          <div className="mb-8 text-center">
            <h2 className="text-2xl font-bold tracking-tight text-secondary-900 dark:text-white">
              Materials Browser
            </h2>
            <p className="mt-2 text-sm text-secondary-500 dark:text-secondary-400">
              Search the composites material database by name, fibre type, or
              resin system.
            </p>
          </div>

          {/* Materials search form */}
          <form
            onSubmit={handleMaterialSubmit}
            className="mx-auto mb-8 flex max-w-xl gap-2"
          >
            <div className="relative flex-1">
              <Atom
                size={16}
                className="absolute left-3.5 top-1/2 -translate-y-1/2 text-secondary-300 dark:text-secondary-500"
              />
              <input
                type="text"
                value={materialQuery}
                onChange={(e) => setMaterialQuery(e.target.value)}
                placeholder="e.g. &quot;carbon epoxy&quot; or &quot;glass&quot;"
                className="w-full rounded-full border border-secondary-200 bg-white/80 py-2.5 pl-10 pr-4 text-sm text-secondary-900 shadow-sm backdrop-blur-sm placeholder:text-secondary-400 focus:border-primary-400 focus:outline-none focus:ring-2 focus:ring-primary-500/20 dark:border-secondary-600 dark:bg-secondary-800/80 dark:text-white dark:placeholder:text-secondary-500 dark:focus:border-primary-400 dark:focus:ring-primary-400/20"
              />
            </div>
            <button
              type="submit"
              disabled={isMaterialLoading || !materialQuery.trim()}
              className="flex items-center gap-1.5 rounded-full bg-gradient-to-r from-primary-700 to-primary-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition-all hover:shadow-md hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-50 dark:from-primary-600 dark:to-primary-500"
            >
              {isMaterialLoading ? (
                <Loader2 size={16} className="animate-spin" />
              ) : (
                <Search size={16} />
              )}
              Search
            </button>
          </form>

          {/* Material error */}
          {materialError && (
            <div className="mx-auto mb-4 flex max-w-xl gap-3 rounded-lg border border-red-200 bg-red-50 px-4 py-3 dark:border-red-800 dark:bg-red-900/20">
              <AlertCircle
                size={18}
                className="mt-0.5 flex-shrink-0 text-red-600 dark:text-red-400"
              />
              <p className="text-sm text-red-700 dark:text-red-300">
                {materialError}
              </p>
            </div>
          )}

          {/* Material loading */}
          {isMaterialLoading && (
            <div className="flex items-center justify-center py-12">
              <Loader2
                size={28}
                className="animate-spin text-primary-600 dark:text-primary-400"
              />
            </div>
          )}

          {/* Material results */}
          {hasMaterialSearched &&
            !isMaterialLoading &&
            !materialError &&
            materials.length === 0 && (
              <p className="py-8 text-center text-sm text-secondary-500 dark:text-secondary-400">
                No materials found. Try a different search term.
              </p>
            )}

          {!isMaterialLoading && materials.length > 0 && (
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {materials.map((material, idx) => (
                <MaterialCard key={`${material.name}-${idx}`} material={material} />
              ))}
            </div>
          )}
        </div>
      </section>

      {/* --------------------------------------------------------- */}
      {/* External links footer                                     */}
      {/* --------------------------------------------------------- */}
      <section className="mx-auto max-w-3xl px-4 py-14 text-center">
        <p className="text-sm text-secondary-400 dark:text-secondary-500">
          The full knowledge base is open source and available on GitHub.
        </p>
        <a
          href="https://github.com/addcomposites/composites-design-guide"
          target="_blank"
          rel="noopener noreferrer"
          className="mt-3 inline-flex items-center gap-1.5 text-sm font-medium text-primary-600 transition-colors hover:text-primary-700 dark:text-primary-400 dark:hover:text-primary-300"
        >
          <ExternalLink size={14} />
          View on GitHub
        </a>
      </section>

      {/* --------------------------------------------------------- */}
      {/* Article viewer overlay                                     */}
      {/* --------------------------------------------------------- */}
      {articleOpen && (
        articleLoading ? (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm">
            <Loader2
              size={36}
              className="animate-spin text-white"
            />
          </div>
        ) : (
          <ArticleViewer
            title={articleTitle}
            content={articleContent}
            onClose={handleCloseArticle}
          />
        )
      )}
    </div>
  );
}
