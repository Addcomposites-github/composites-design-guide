import { useState, useEffect } from "react";
import { Key, Check, X, ExternalLink, ChevronDown, ChevronRight } from "lucide-react";

const STORAGE_KEY = "anthropic_api_key";

export default function ApiKeyInput() {
  const [isExpanded, setIsExpanded] = useState(false);
  const [apiKey, setApiKey] = useState("");
  const [hasSavedKey, setHasSavedKey] = useState(false);

  useEffect(() => {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      setHasSavedKey(true);
      setApiKey(stored);
    }
  }, []);

  function handleSave() {
    const trimmed = apiKey.trim();
    if (!trimmed) return;
    localStorage.setItem(STORAGE_KEY, trimmed);
    setHasSavedKey(true);
  }

  function handleClear() {
    localStorage.removeItem(STORAGE_KEY);
    setApiKey("");
    setHasSavedKey(false);
  }

  return (
    <div className="mb-6 rounded-2xl border border-secondary-100 bg-white shadow-sm dark:border-secondary-700/60 dark:bg-secondary-800/50">
      {/* Collapsible Header */}
      <button
        type="button"
        onClick={() => setIsExpanded(!isExpanded)}
        className="flex w-full items-center gap-3 px-4 py-3 text-left"
      >
        <Key
          size={18}
          className="flex-shrink-0 text-primary-600 dark:text-primary-400"
        />
        <span className="flex-1 text-sm font-medium text-secondary-900 dark:text-white">
          API Key Required for AI Analysis
        </span>
        {hasSavedKey && (
          <span className="flex items-center gap-1 text-xs font-medium text-green-600 dark:text-green-400">
            <Check size={14} />
            Saved
          </span>
        )}
        {isExpanded ? (
          <ChevronDown
            size={16}
            className="flex-shrink-0 text-secondary-400 dark:text-secondary-500"
          />
        ) : (
          <ChevronRight
            size={16}
            className="flex-shrink-0 text-secondary-400 dark:text-secondary-500"
          />
        )}
      </button>

      {/* Expanded Content */}
      {isExpanded && (
        <div className="border-t border-secondary-100 px-4 py-4 dark:border-secondary-700/60">
          <p className="mb-3 text-xs text-secondary-600 dark:text-secondary-400">
            Enter your Anthropic API key to use the AI analysis feature. Your key
            is stored in your browser only and never sent to our servers for
            storage.
          </p>

          <div className="mb-3 flex gap-2">
            <input
              type="password"
              value={apiKey}
              onChange={(e) => {
                setApiKey(e.target.value);
                setHasSavedKey(false);
              }}
              placeholder="sk-ant-..."
              className="flex-1 rounded-xl border border-secondary-200 bg-white px-3.5 py-2 text-sm text-secondary-900 placeholder-secondary-400 transition-colors focus:border-primary-400 focus:outline-none focus:ring-2 focus:ring-primary-500/20 dark:border-secondary-600 dark:bg-secondary-800 dark:text-white dark:placeholder-secondary-500 dark:focus:border-primary-400"
            />
            <button
              type="button"
              onClick={handleSave}
              disabled={!apiKey.trim()}
              className="rounded-xl bg-gradient-to-r from-primary-700 to-primary-600 px-4 py-2 text-sm font-medium text-white shadow-sm transition-all hover:shadow-md hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-50 dark:from-primary-600 dark:to-primary-500"
            >
              Save
            </button>
            {hasSavedKey && (
              <button
                type="button"
                onClick={handleClear}
                className="rounded-xl border border-secondary-200 px-3 py-2 text-sm font-medium text-secondary-500 transition-colors hover:bg-secondary-50 dark:border-secondary-600 dark:text-secondary-400 dark:hover:bg-secondary-700"
              >
                <X size={16} />
              </button>
            )}
          </div>

          <a
            href="https://console.anthropic.com/"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1 text-xs font-medium text-primary-600 hover:text-primary-700 dark:text-primary-400 dark:hover:text-primary-300"
          >
            Get an API key from Anthropic
            <ExternalLink size={12} />
          </a>
        </div>
      )}
    </div>
  );
}
