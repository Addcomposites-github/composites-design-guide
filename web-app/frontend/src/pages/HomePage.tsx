import {
  ArrowRight,
  Atom,
  Factory,
  DollarSign,
  Layers,
  BookOpen,
  Calculator,
  Droplets,
  Cog,
  Sparkles,
} from "lucide-react";
import type { Page } from "../types";

interface HomePageProps {
  onNavigate: (page: Page) => void;
}

interface FeatureCardData {
  icon: React.ReactNode;
  title: string;
  description: string;
}

const features: FeatureCardData[] = [
  {
    icon: <Atom size={24} />,
    title: "Material Selection",
    description:
      "Get fibre and resin recommendations based on your part geometry, load cases, and budget. Carbon, glass, aramid, and hybrid options.",
  },
  {
    icon: <Factory size={24} />,
    title: "Process Recommendation",
    description:
      "Find the best manufacturing process for your part. Wet layup, vacuum bagging, infusion, prepreg, and automated placement.",
  },
  {
    icon: <DollarSign size={24} />,
    title: "Cost Estimation",
    description:
      "Estimate per-part cost including materials, labour, tooling, and consumables. Compare processes to optimise your budget.",
  },
  {
    icon: <Layers size={24} />,
    title: "Stacking Rules",
    description:
      "Design your laminate with validated stacking sequences. Symmetry, balance, angle distribution, and ply drop-off rules.",
  },
];

interface ToolLinkData {
  icon: React.ReactNode;
  name: string;
  description: string;
  url: string;
}

const tools: ToolLinkData[] = [
  {
    icon: <Calculator size={18} />,
    name: "AddStack",
    description: "Free laminate calculator with CLT, failure criteria, and material database",
    url: "https://addstack.addcomposites.com",
  },
  {
    icon: <Droplets size={18} />,
    name: "Resin Flow Simulator",
    description: "VARTM infusion simulation for resin flow planning",
    url: "https://www.addcomposites.com/addcomposites-apps/resin-flow",
  },
  {
    icon: <Cog size={18} />,
    name: "CRDS",
    description: "Composite rotor and sleeve design tool",
    url: "https://www.addcomposites.com/addcomposites-apps/crds",
  },
];

export default function HomePage({ onNavigate }: HomePageProps) {
  return (
    <div className="animate-fade-in">
      {/* Hero Section */}
      <section className="bg-mesh bg-grid relative overflow-hidden px-4 py-20 text-center sm:py-28">
        <div className="relative z-10">
          <div className="mb-5 inline-flex items-center gap-2 rounded-full border border-primary-200/60 bg-white/60 px-3.5 py-1.5 text-xs font-medium text-primary-700 shadow-sm backdrop-blur-sm dark:border-primary-700/40 dark:bg-secondary-800/60 dark:text-primary-300">
            <span className="h-1.5 w-1.5 rounded-full bg-primary-500 animate-pulse" />
            Open-source composites design platform
          </div>
          <h1 className="mx-auto max-w-3xl text-4xl font-extrabold tracking-tight text-secondary-900 sm:text-5xl lg:text-6xl dark:text-white">
            Design Composite Parts{" "}
            <span className="text-gradient">with AI</span>
          </h1>
          <p className="mx-auto mt-5 max-w-xl text-base leading-relaxed text-secondary-500 dark:text-secondary-400">
            Upload a photo or describe your part. Get a complete manufacturing
            plan with material selection, laminate design, cost estimation, and
            step-by-step instructions.
          </p>
          <div className="mt-9 flex flex-col items-center justify-center gap-3 sm:flex-row">
            <button
              onClick={() => onNavigate("analyze")}
              className="flex items-center gap-2 rounded-full bg-gradient-to-r from-primary-700 to-primary-600 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-primary-500/20 transition-all hover:shadow-xl hover:shadow-primary-500/30 hover:brightness-110 dark:from-primary-600 dark:to-primary-500"
            >
              Start Designing
              <ArrowRight size={16} />
            </button>
            <button
              onClick={() => onNavigate("knowledge")}
              className="flex items-center gap-2 rounded-full border border-secondary-200 bg-white/80 px-7 py-3 text-sm font-semibold text-secondary-700 shadow-sm backdrop-blur-sm transition-all hover:border-secondary-300 hover:bg-white hover:shadow-md dark:border-secondary-600 dark:bg-secondary-800/80 dark:text-secondary-300 dark:hover:bg-secondary-800"
            >
              <BookOpen size={16} />
              Browse Knowledge Base
            </button>
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section className="mx-auto max-w-5xl px-4 py-16">
        <div className="mb-10 text-center">
          <h2 className="text-2xl font-bold tracking-tight text-secondary-900 dark:text-white">
            What You Get
          </h2>
          <p className="mt-2 text-sm text-secondary-500 dark:text-secondary-400">
            Everything you need to go from concept to manufactured part
          </p>
        </div>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {features.map((feature, i) => (
            <div
              key={feature.title}
              className="group relative rounded-2xl border border-secondary-100 bg-white p-6 transition-all duration-300 hover:-translate-y-1 hover:border-primary-200/60 hover:shadow-xl hover:shadow-primary-500/5 dark:border-secondary-700/60 dark:bg-secondary-800/50 dark:hover:border-primary-700/40"
              style={{ animationDelay: `${i * 80}ms` }}
            >
              <div className="mb-4 flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br from-primary-50 to-primary-100 text-primary-600 ring-1 ring-primary-200/40 transition-transform group-hover:scale-110 dark:from-primary-900/30 dark:to-primary-800/20 dark:text-primary-400 dark:ring-primary-700/30">
                {feature.icon}
              </div>
              <h3 className="mb-1.5 text-sm font-semibold text-secondary-900 dark:text-white">
                {feature.title}
              </h3>
              <p className="text-[13px] leading-relaxed text-secondary-500 dark:text-secondary-400">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* Knowledge Base Stats */}
      <section className="relative overflow-hidden px-4 py-16">
        <div className="absolute inset-0 bg-gradient-to-b from-secondary-50/80 to-white dark:from-secondary-800/30 dark:to-secondary-900" />
        <div className="relative z-10 mx-auto max-w-3xl text-center">
          <h2 className="text-2xl font-bold tracking-tight text-secondary-900 dark:text-white">
            Open Knowledge Base
          </h2>
          <p className="mt-2 text-sm text-secondary-500 dark:text-secondary-400">
            Backed by a comprehensive, open-source composites knowledge base.
            Written in plain language. Structured for LLM retrieval. Free
            forever.
          </p>
          <div className="mt-8 grid grid-cols-2 gap-4 sm:grid-cols-4">
            {[
              { value: "56", label: "Articles" },
              { value: "67k+", label: "Words" },
              { value: "10", label: "Topic Areas" },
              { value: "CC BY 4.0", label: "License" },
            ].map((stat) => (
              <div
                key={stat.label}
                className="rounded-2xl border border-secondary-100 bg-white/80 px-4 py-5 shadow-sm backdrop-blur-sm dark:border-secondary-700/50 dark:bg-secondary-800/50"
              >
                <p className="text-2xl font-bold tracking-tight text-gradient">
                  {stat.value}
                </p>
                <p className="mt-0.5 text-xs font-medium text-secondary-400 dark:text-secondary-500">
                  {stat.label}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Free Tools */}
      <section className="mx-auto max-w-3xl px-4 py-16">
        <div className="mb-8 text-center">
          <h2 className="text-2xl font-bold tracking-tight text-secondary-900 dark:text-white">
            Free Composites Tools
          </h2>
          <p className="mt-2 text-sm text-secondary-500 dark:text-secondary-400">
            Open tools by Addcomposites to accelerate your design workflow
          </p>
        </div>
        <div className="space-y-3">
          {tools.map((tool) => (
            <a
              key={tool.name}
              href={tool.url}
              target="_blank"
              rel="noopener noreferrer"
              className="group flex items-center gap-4 rounded-xl border border-secondary-100 bg-white px-5 py-4 transition-all duration-200 hover:-translate-y-0.5 hover:border-primary-200/60 hover:shadow-lg hover:shadow-primary-500/5 dark:border-secondary-700/60 dark:bg-secondary-800/50 dark:hover:border-primary-700/40"
            >
              <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-accent-500/10 to-accent-500/5 text-accent-600 ring-1 ring-accent-500/10 dark:text-accent-400 dark:ring-accent-500/20">
                {tool.icon}
              </div>
              <div className="flex-1">
                <p className="text-sm font-semibold text-secondary-900 dark:text-white">
                  {tool.name}
                </p>
                <p className="text-[13px] text-secondary-500 dark:text-secondary-400">
                  {tool.description}
                </p>
              </div>
              <ArrowRight
                size={16}
                className="text-secondary-300 transition-transform group-hover:translate-x-1 group-hover:text-primary-500 dark:text-secondary-600"
              />
            </a>
          ))}
        </div>
      </section>

      {/* What's New */}
      <section className="relative overflow-hidden px-4 py-16">
        <div className="absolute inset-0 bg-gradient-to-b from-secondary-50/80 to-white dark:from-secondary-800/30 dark:to-secondary-900" />
        <div className="relative z-10 mx-auto max-w-3xl">
          <h2 className="mb-8 text-center text-2xl font-bold tracking-tight text-secondary-900 dark:text-white">
            What's New
          </h2>
          <div className="rounded-2xl border border-secondary-100 bg-white/80 p-6 shadow-sm backdrop-blur-sm dark:border-secondary-700/50 dark:bg-secondary-800/50">
            <div className="flex items-center gap-3">
              <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-primary-50 to-primary-100 text-primary-600 dark:from-primary-900/30 dark:to-primary-800/20 dark:text-primary-400">
                <Sparkles size={18} />
              </div>
              <div className="flex items-center gap-2.5">
                <span className="rounded-full bg-gradient-to-r from-primary-600 to-primary-500 px-2.5 py-0.5 text-xs font-semibold text-white shadow-sm">
                  v1.0.0
                </span>
                <span className="text-xs text-secondary-400 dark:text-secondary-500">
                  Feb 2026
                </span>
              </div>
            </div>
            <p className="mt-3 text-sm leading-relaxed text-secondary-500 dark:text-secondary-400">
              Launch of OpenComposites — the open composites design platform.
              AI-powered analysis, CLT calculator, sandwich panel analysis,
              bolted joint analysis, and 56 knowledge articles.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
