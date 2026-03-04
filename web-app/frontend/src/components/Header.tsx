import { Layers, Home, FlaskConical, BookOpen } from "lucide-react";
import type { Page } from "../types";

interface HeaderProps {
  currentPage: Page;
  onNavigate: (page: Page) => void;
}

export default function Header({ currentPage, onNavigate }: HeaderProps) {
  const navItems: { page: Page; label: string; icon: React.ReactNode }[] = [
    { page: "home", label: "Home", icon: <Home size={16} /> },
    { page: "analyze", label: "Analyze", icon: <FlaskConical size={16} /> },
    { page: "knowledge", label: "Knowledge Base", icon: <BookOpen size={16} /> },
  ];

  return (
    <header className="sticky top-0 z-50 border-b border-secondary-200/60 bg-white/80 backdrop-blur-xl dark:border-secondary-700/60 dark:bg-secondary-900/80">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">
        {/* Logo */}
        <button
          onClick={() => onNavigate("home")}
          className="flex items-center gap-2.5 transition-opacity hover:opacity-80"
        >
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-primary-600 to-primary-800 text-white shadow-sm">
            <Layers size={18} />
          </div>
          <div className="flex flex-col">
            <span className="text-base font-bold leading-tight tracking-tight text-secondary-900 dark:text-white">
              OpenComposites
            </span>
            <span className="text-[10px] font-medium uppercase leading-tight tracking-wide text-secondary-400 dark:text-secondary-500">
              by Addcomposites
            </span>
          </div>
        </button>

        {/* Navigation */}
        <nav className="flex items-center gap-0.5">
          {navItems.map(({ page, label, icon }) => (
            <button
              key={page}
              onClick={() => onNavigate(page)}
              className={`flex items-center gap-1.5 rounded-full px-3.5 py-1.5 text-[13px] font-medium transition-all ${
                currentPage === page
                  ? "bg-primary-50 text-primary-700 shadow-sm ring-1 ring-primary-200/60 dark:bg-primary-900/30 dark:text-primary-300 dark:ring-primary-700/40"
                  : "text-secondary-500 hover:bg-secondary-50 hover:text-secondary-900 dark:text-secondary-400 dark:hover:bg-secondary-800 dark:hover:text-white"
              }`}
            >
              {icon}
              <span className="hidden sm:inline">{label}</span>
            </button>
          ))}
        </nav>
      </div>
    </header>
  );
}
