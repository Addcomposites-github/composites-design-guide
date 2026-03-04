import { DollarSign } from "lucide-react";

interface CostItem {
  label: string;
  value: number;
  color: string;
}

interface CostBreakdownChartProps {
  materialCost: number;
  labourCost: number;
  toolingCost: number;
  consumablesCost: number;
  totalCost: number;
  notes?: string[];
}

function formatUSD(value: number): string {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(value);
}

export default function CostBreakdownChart({
  materialCost,
  labourCost,
  toolingCost,
  consumablesCost,
  totalCost,
  notes,
}: CostBreakdownChartProps) {
  const items: CostItem[] = [
    { label: "Material", value: materialCost, color: "bg-blue-500" },
    { label: "Labour", value: labourCost, color: "bg-emerald-500" },
    { label: "Tooling", value: toolingCost, color: "bg-amber-500" },
    { label: "Consumables", value: consumablesCost, color: "bg-purple-500" },
  ];

  const maxValue = Math.max(...items.map((i) => i.value), 1);

  // Pie chart data (SVG)
  const total = items.reduce((sum, item) => sum + item.value, 0) || 1;
  const pieColors = ["#3b82f6", "#10b981", "#f59e0b", "#a855f7"];

  function buildPieSlices() {
    let cumulativeAngle = 0;
    return items.map((item, index) => {
      const fraction = item.value / total;
      const startAngle = cumulativeAngle;
      const endAngle = cumulativeAngle + fraction * 360;
      cumulativeAngle = endAngle;

      if (fraction === 0) return null;

      // SVG arc math
      const startRad = ((startAngle - 90) * Math.PI) / 180;
      const endRad = ((endAngle - 90) * Math.PI) / 180;
      const x1 = 50 + 40 * Math.cos(startRad);
      const y1 = 50 + 40 * Math.sin(startRad);
      const x2 = 50 + 40 * Math.cos(endRad);
      const y2 = 50 + 40 * Math.sin(endRad);
      const largeArc = fraction > 0.5 ? 1 : 0;

      const d = `M 50 50 L ${x1} ${y1} A 40 40 0 ${largeArc} 1 ${x2} ${y2} Z`;

      return <path key={index} d={d} fill={pieColors[index]} />;
    });
  }

  return (
    <div className="space-y-4">
      {/* Total Cost Banner */}
      <div className="flex items-center gap-3 rounded-lg bg-primary-50 px-4 py-3 dark:bg-primary-900/20">
        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-primary-100 text-primary-700 dark:bg-primary-800 dark:text-primary-300">
          <DollarSign size={20} />
        </div>
        <div>
          <p className="text-xs font-medium text-primary-600 dark:text-primary-400">
            Estimated Total Cost Per Part
          </p>
          <p className="text-2xl font-bold text-primary-900 dark:text-white">
            {formatUSD(totalCost)}
          </p>
        </div>
      </div>

      {/* Chart + Bars */}
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
        {/* Pie Chart */}
        <div className="flex items-center justify-center">
          <svg viewBox="0 0 100 100" className="h-40 w-40">
            {buildPieSlices()}
            {/* Center circle for donut effect */}
            <circle
              cx="50"
              cy="50"
              r="22"
              fill="white"
              className="dark:fill-secondary-800"
            />
            <text
              x="50"
              y="48"
              textAnchor="middle"
              className="fill-secondary-900 text-[7px] font-bold dark:fill-white"
            >
              {formatUSD(totalCost)}
            </text>
            <text
              x="50"
              y="56"
              textAnchor="middle"
              className="fill-secondary-500 text-[4px]"
            >
              per part
            </text>
          </svg>
        </div>

        {/* Bar Chart */}
        <div className="space-y-3">
          {items.map((item) => (
            <div key={item.label}>
              <div className="flex items-center justify-between text-sm">
                <span className="text-secondary-700 dark:text-secondary-300">
                  {item.label}
                </span>
                <span className="font-medium text-secondary-900 dark:text-white">
                  {formatUSD(item.value)}
                </span>
              </div>
              <div className="mt-1 h-2 overflow-hidden rounded-full bg-secondary-100 dark:bg-secondary-700">
                <div
                  className={`h-full rounded-full transition-all ${item.color}`}
                  style={{
                    width: `${Math.max((item.value / maxValue) * 100, 2)}%`,
                  }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Notes */}
      {notes && notes.length > 0 && (
        <div className="rounded-lg bg-secondary-50 px-4 py-3 dark:bg-secondary-800/50">
          <p className="mb-1 text-xs font-medium text-secondary-600 dark:text-secondary-400">
            Cost Notes
          </p>
          <ul className="space-y-0.5 text-xs text-secondary-600 dark:text-secondary-400">
            {notes.map((note, i) => (
              <li key={i} className="flex gap-1.5">
                <span className="mt-0.5 text-secondary-400">--</span>
                {note}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
