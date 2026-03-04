import { useState } from "react";
import { Send, Loader2 } from "lucide-react";
import PhotoUpload from "./PhotoUpload";
import type { AnalysisRequest } from "../types";

interface AnalysisFormProps {
  onSubmit: (request: AnalysisRequest) => void;
  isLoading: boolean;
}

export default function AnalysisForm({
  onSubmit,
  isLoading,
}: AnalysisFormProps) {
  const [partDescription, setPartDescription] = useState("");
  const [intendedUse, setIntendedUse] = useState("");
  const [skillLevel, setSkillLevel] = useState<
    "beginner" | "intermediate" | "advanced"
  >("beginner");
  const [photoBase64, setPhotoBase64] = useState<string | null>(null);

  const canSubmit =
    partDescription.trim().length >= 3 &&
    intendedUse.trim().length >= 3 &&
    !isLoading;

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!canSubmit) return;

    onSubmit({
      part_description: partDescription.trim(),
      intended_use: intendedUse.trim(),
      skill_level: skillLevel,
      photo_base64: photoBase64,
    });
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {/* Part Description */}
      <div>
        <label
          htmlFor="partDescription"
          className="mb-1.5 block text-sm font-medium text-secondary-900 dark:text-secondary-100"
        >
          Part Description <span className="text-danger-500">*</span>
        </label>
        <textarea
          id="partDescription"
          rows={3}
          value={partDescription}
          onChange={(e) => setPartDescription(e.target.value)}
          placeholder="e.g. Carbon fibre bicycle fork with aero cross-section, tapered from crown to dropouts"
          className="w-full rounded-xl border border-secondary-200 bg-white px-3.5 py-2.5 text-sm text-secondary-900 placeholder-secondary-400 transition-colors focus:border-primary-400 focus:outline-none focus:ring-2 focus:ring-primary-500/20 dark:border-secondary-600 dark:bg-secondary-800 dark:text-white dark:placeholder-secondary-500 dark:focus:border-primary-400"
          disabled={isLoading}
        />
        <p className="mt-1.5 text-[12px] text-secondary-400 dark:text-secondary-500">
          Describe the geometry, dimensions, and any special features of your
          part.
        </p>
      </div>

      {/* Intended Use */}
      <div>
        <label
          htmlFor="intendedUse"
          className="mb-1.5 block text-sm font-medium text-secondary-900 dark:text-secondary-100"
        >
          Intended Use <span className="text-danger-500">*</span>
        </label>
        <textarea
          id="intendedUse"
          rows={3}
          value={intendedUse}
          onChange={(e) => setIntendedUse(e.target.value)}
          placeholder="e.g. Road cycling, rider weight up to 100 kg, pothole impacts, fatigue over 50,000 km"
          className="w-full rounded-xl border border-secondary-200 bg-white px-3.5 py-2.5 text-sm text-secondary-900 placeholder-secondary-400 transition-colors focus:border-primary-400 focus:outline-none focus:ring-2 focus:ring-primary-500/20 dark:border-secondary-600 dark:bg-secondary-800 dark:text-white dark:placeholder-secondary-500 dark:focus:border-primary-400"
          disabled={isLoading}
        />
        <p className="mt-1.5 text-[12px] text-secondary-400 dark:text-secondary-500">
          How will this part be used? Include key load cases, environment, and
          performance requirements.
        </p>
      </div>

      {/* Skill Level */}
      <div>
        <label
          htmlFor="skillLevel"
          className="mb-1.5 block text-sm font-medium text-secondary-900 dark:text-secondary-100"
        >
          Your Composites Experience
        </label>
        <select
          id="skillLevel"
          value={skillLevel}
          onChange={(e) =>
            setSkillLevel(
              e.target.value as "beginner" | "intermediate" | "advanced"
            )
          }
          className="w-full rounded-xl border border-secondary-200 bg-white px-3.5 py-2.5 text-sm text-secondary-900 transition-colors focus:border-primary-400 focus:outline-none focus:ring-2 focus:ring-primary-500/20 dark:border-secondary-600 dark:bg-secondary-800 dark:text-white dark:focus:border-primary-400"
          disabled={isLoading}
        >
          <option value="beginner">
            Beginner - First time working with composites
          </option>
          <option value="intermediate">
            Intermediate - Have made a few parts
          </option>
          <option value="advanced">
            Advanced - Experienced with multiple processes
          </option>
        </select>
        <p className="mt-1 text-xs text-secondary-500 dark:text-secondary-400">
          This adjusts the detail level of instructions and process
          recommendations.
        </p>
      </div>

      {/* Photo Upload */}
      <div>
        <label className="mb-1.5 block text-sm font-medium text-secondary-900 dark:text-secondary-100">
          Reference Photo{" "}
          <span className="font-normal text-secondary-500 dark:text-secondary-400">
            (optional)
          </span>
        </label>
        <PhotoUpload onPhotoChange={setPhotoBase64} />
        <p className="mt-1 text-xs text-secondary-500 dark:text-secondary-400">
          Upload a photo of the part or a similar reference. This helps the AI
          assess geometry and complexity.
        </p>
      </div>

      {/* Submit */}
      <button
        type="submit"
        disabled={!canSubmit}
        className="flex w-full items-center justify-center gap-2 rounded-full bg-gradient-to-r from-primary-700 to-primary-600 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-primary-500/20 transition-all hover:shadow-xl hover:shadow-primary-500/30 hover:brightness-110 focus:outline-none focus:ring-2 focus:ring-primary-500/50 disabled:cursor-not-allowed disabled:opacity-50 disabled:shadow-none dark:from-primary-600 dark:to-primary-500"
      >
        {isLoading ? (
          <>
            <Loader2 size={18} className="animate-spin" />
            Analyzing Part...
          </>
        ) : (
          <>
            <Send size={18} />
            Generate Manufacturing Plan
          </>
        )}
      </button>
    </form>
  );
}
