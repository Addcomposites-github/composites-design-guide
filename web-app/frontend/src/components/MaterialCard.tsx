import { Atom } from "lucide-react";

interface MaterialCardProps {
  name: string;
  fibreType: string;
  properties: {
    label: string;
    value: string | number;
    unit?: string;
  }[];
  costRange?: string;
}

export default function MaterialCard({
  name,
  fibreType,
  properties,
  costRange,
}: MaterialCardProps) {
  return (
    <div className="rounded-lg border border-secondary-200 bg-white p-4 dark:border-secondary-700 dark:bg-secondary-800">
      {/* Header */}
      <div className="flex items-center gap-2">
        <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-amber-50 text-amber-600 dark:bg-amber-900/30 dark:text-amber-400">
          <Atom size={18} />
        </div>
        <div>
          <h3 className="text-sm font-semibold text-secondary-900 dark:text-white">
            {name}
          </h3>
          <p className="text-xs text-secondary-500 dark:text-secondary-400">
            {fibreType}
          </p>
        </div>
      </div>

      {/* Properties Table */}
      <table className="mt-3 w-full text-xs">
        <tbody>
          {properties.map((prop, i) => (
            <tr
              key={i}
              className={
                i % 2 === 0
                  ? "bg-secondary-50 dark:bg-secondary-800/50"
                  : "bg-white dark:bg-secondary-800"
              }
            >
              <td className="px-2 py-1.5 text-secondary-600 dark:text-secondary-400">
                {prop.label}
              </td>
              <td className="px-2 py-1.5 text-right font-medium text-secondary-900 dark:text-white">
                {prop.value}
                {prop.unit && (
                  <span className="ml-0.5 text-secondary-500 dark:text-secondary-400">
                    {prop.unit}
                  </span>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Cost Range */}
      {costRange && (
        <div className="mt-3 rounded bg-secondary-50 px-2 py-1.5 text-center text-xs dark:bg-secondary-700">
          <span className="text-secondary-500 dark:text-secondary-400">
            Cost range:{" "}
          </span>
          <span className="font-medium text-secondary-900 dark:text-white">
            {costRange}
          </span>
        </div>
      )}
    </div>
  );
}
