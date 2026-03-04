interface StackingVisualizerProps {
  angles: number[];
}

/** Map an angle to a display color. */
function angleColor(angle: number): { bg: string; text: string; label: string } {
  const normalized = ((angle % 360) + 360) % 360;

  if (normalized === 0 || normalized === 180) {
    return {
      bg: "bg-blue-500 dark:bg-blue-600",
      text: "text-white",
      label: "0-deg",
    };
  }
  if (normalized === 90 || normalized === 270) {
    return {
      bg: "bg-red-500 dark:bg-red-600",
      text: "text-white",
      label: "90-deg",
    };
  }
  if (normalized === 45 || normalized === 225) {
    return {
      bg: "bg-emerald-500 dark:bg-emerald-600",
      text: "text-white",
      label: "+45-deg",
    };
  }
  if (normalized === 135 || normalized === 315) {
    // -45 degrees
    return {
      bg: "bg-amber-400 dark:bg-amber-500",
      text: "text-secondary-900",
      label: "-45-deg",
    };
  }
  // any other angle
  return {
    bg: "bg-purple-500 dark:bg-purple-600",
    text: "text-white",
    label: "other",
  };
}

function formatAngle(angle: number): string {
  if (angle > 0) return `+${angle}`;
  return String(angle);
}

export default function StackingVisualizer({
  angles,
}: StackingVisualizerProps) {
  if (!angles || angles.length === 0) {
    return (
      <p className="text-sm text-secondary-500 dark:text-secondary-400">
        No stacking sequence data available.
      </p>
    );
  }

  const midIndex = Math.floor(angles.length / 2);
  const isSymmetric =
    angles.length % 2 === 0 &&
    angles.every(
      (a, i) => a === angles[angles.length - 1 - i]
    );

  return (
    <div className="space-y-3">
      {/* Legend */}
      <div className="flex flex-wrap gap-3 text-xs">
        <span className="flex items-center gap-1">
          <span className="inline-block h-3 w-3 rounded bg-blue-500" /> 0 deg
        </span>
        <span className="flex items-center gap-1">
          <span className="inline-block h-3 w-3 rounded bg-red-500" /> 90 deg
        </span>
        <span className="flex items-center gap-1">
          <span className="inline-block h-3 w-3 rounded bg-emerald-500" /> +45
          deg
        </span>
        <span className="flex items-center gap-1">
          <span className="inline-block h-3 w-3 rounded bg-amber-400" /> -45
          deg
        </span>
        <span className="flex items-center gap-1">
          <span className="inline-block h-3 w-3 rounded bg-purple-500" /> Other
        </span>
      </div>

      {/* Ply Stack */}
      <div className="relative rounded-lg border border-secondary-200 bg-white p-3 dark:border-secondary-700 dark:bg-secondary-800">
        <div className="space-y-0.5">
          {angles.map((angle, index) => {
            const color = angleColor(angle);
            const isMidplane = index === midIndex && isSymmetric;

            return (
              <div key={index}>
                {isMidplane && (
                  <div className="my-1 flex items-center gap-2">
                    <div className="h-px flex-1 bg-secondary-400 dark:bg-secondary-500" />
                    <span className="text-[10px] font-medium uppercase tracking-wide text-secondary-500 dark:text-secondary-400">
                      midplane
                    </span>
                    <div className="h-px flex-1 bg-secondary-400 dark:bg-secondary-500" />
                  </div>
                )}
                <div
                  className={`flex items-center justify-between rounded px-3 py-1.5 ${color.bg} ${color.text}`}
                >
                  <span className="text-xs font-medium">
                    Ply {index + 1}
                  </span>
                  <span className="text-sm font-bold">
                    {formatAngle(angle)} deg
                  </span>
                </div>
              </div>
            );
          })}
        </div>

        {/* Summary */}
        <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1 border-t border-secondary-200 pt-2 text-xs text-secondary-600 dark:border-secondary-700 dark:text-secondary-400">
          <span>
            <strong>{angles.length}</strong> plies total
          </span>
          {isSymmetric && (
            <span className="font-medium text-emerald-600 dark:text-emerald-400">
              Symmetric
            </span>
          )}
          <span>
            Sequence: [{angles.map((a) => `${a}`).join(" / ")}]
          </span>
        </div>
      </div>
    </div>
  );
}
