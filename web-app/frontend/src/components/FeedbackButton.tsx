import { useState } from "react";
import { ThumbsUp, ThumbsDown, Send, ExternalLink } from "lucide-react";

interface FeedbackButtonProps {
  context: string;
}

export default function FeedbackButton({ context }: FeedbackButtonProps) {
  const [feedbackType, setFeedbackType] = useState<
    "positive" | "negative" | null
  >(null);
  const [comment, setComment] = useState("");
  const [submitted, setSubmitted] = useState(false);

  function handleThumbsUp() {
    setFeedbackType("positive");
    setSubmitted(false);
  }

  function handleThumbsDown() {
    setFeedbackType("negative");
    setSubmitted(false);
  }

  function handleSubmit() {
    const type = feedbackType === "positive" ? "Positive" : "Negative";
    const title = encodeURIComponent(
      `[Feedback] ${type}: ${context.slice(0, 50)}`
    );
    const body = encodeURIComponent(
      `**Feedback type:** ${type}\n**Context:** ${context}\n**Comment:** ${comment || "(no comment)"}\n\n---\n_Submitted via OpenComposites feedback widget_`
    );
    const url = `https://github.com/addcomposites/composites-design-guide/issues/new?title=${title}&body=${body}&labels=feedback`;
    window.open(url, "_blank", "noopener,noreferrer");
    setSubmitted(true);
  }

  if (submitted) {
    return (
      <div className="mt-6 flex items-center gap-2 text-xs text-secondary-500 dark:text-secondary-400">
        <ThumbsUp size={14} className="text-green-500" />
        Thanks for your feedback!
      </div>
    );
  }

  return (
    <div className="mt-6">
      <div className="flex items-center gap-3">
        <span className="text-xs text-secondary-500 dark:text-secondary-400">
          Was this helpful?
        </span>
        <button
          onClick={handleThumbsUp}
          className={`rounded p-1.5 transition-colors ${
            feedbackType === "positive"
              ? "bg-green-100 text-green-600 dark:bg-green-900/30 dark:text-green-400"
              : "text-secondary-400 hover:bg-secondary-100 hover:text-secondary-600 dark:text-secondary-500 dark:hover:bg-secondary-700 dark:hover:text-secondary-300"
          }`}
          aria-label="Thumbs up"
        >
          <ThumbsUp size={16} />
        </button>
        <button
          onClick={handleThumbsDown}
          className={`rounded p-1.5 transition-colors ${
            feedbackType === "negative"
              ? "bg-red-100 text-red-600 dark:bg-red-900/30 dark:text-red-400"
              : "text-secondary-400 hover:bg-secondary-100 hover:text-secondary-600 dark:text-secondary-500 dark:hover:bg-secondary-700 dark:hover:text-secondary-300"
          }`}
          aria-label="Thumbs down"
        >
          <ThumbsDown size={16} />
        </button>
      </div>

      {feedbackType === "negative" && (
        <div className="mt-3 space-y-2">
          <textarea
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            placeholder="What could be improved?"
            rows={3}
            className="w-full rounded-lg border border-secondary-300 bg-white px-3 py-2 text-xs text-secondary-900 placeholder:text-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-1 focus:ring-primary-500 dark:border-secondary-600 dark:bg-secondary-800 dark:text-white dark:placeholder:text-secondary-500 dark:focus:border-primary-400 dark:focus:ring-primary-400"
          />
          <button
            onClick={handleSubmit}
            className="inline-flex items-center gap-1.5 rounded-lg bg-primary-800 px-3 py-1.5 text-xs font-semibold text-white transition-colors hover:bg-primary-700 dark:bg-primary-700 dark:hover:bg-primary-600"
          >
            <Send size={12} />
            Submit Feedback
            <ExternalLink size={10} />
          </button>
        </div>
      )}

      {feedbackType === "positive" && (
        <div className="mt-3">
          <button
            onClick={handleSubmit}
            className="inline-flex items-center gap-1.5 rounded-lg bg-primary-800 px-3 py-1.5 text-xs font-semibold text-white transition-colors hover:bg-primary-700 dark:bg-primary-700 dark:hover:bg-primary-600"
          >
            <Send size={12} />
            Submit Feedback
            <ExternalLink size={10} />
          </button>
        </div>
      )}
    </div>
  );
}
