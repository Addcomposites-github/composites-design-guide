export default function Footer() {
  const links = [
    { label: "Addcomposites", href: "https://www.addcomposites.com" },
    { label: "AddStack", href: "https://addstack.addcomposites.com" },
    { label: "GitHub", href: "https://github.com/addcomposites/composites-design-guide" },
    { label: "Contribute", href: "https://github.com/addcomposites/composites-design-guide/blob/master/CONTRIBUTING.md" },
    { label: "Report an Error", href: "https://github.com/addcomposites/composites-design-guide/issues/new?labels=correction&title=[Correction]%20" },
  ];

  return (
    <footer className="border-t border-secondary-100 bg-white dark:border-secondary-800 dark:bg-secondary-900">
      <div className="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
        {/* Links Row */}
        <div className="flex flex-wrap items-center justify-center gap-x-5 gap-y-2">
          {links.map((link) => (
            <a
              key={link.label}
              href={link.href}
              target="_blank"
              rel="noopener noreferrer"
              className="text-[13px] text-secondary-400 transition-colors hover:text-primary-600 dark:text-secondary-500 dark:hover:text-primary-400"
            >
              {link.label}
            </a>
          ))}
        </div>

        {/* Attribution */}
        <p className="mt-5 text-center text-[11px] text-secondary-400 dark:text-secondary-600">
          Knowledge base content licensed under{" "}
          <a
            href="https://creativecommons.org/licenses/by/4.0/"
            target="_blank"
            rel="noopener noreferrer"
            className="underline decoration-secondary-300 hover:text-primary-600 dark:decoration-secondary-600 dark:hover:text-primary-400"
          >
            CC BY 4.0
          </a>
        </p>

        {/* Disclaimer */}
        <p className="mx-auto mt-3 max-w-2xl text-center text-[11px] leading-relaxed text-secondary-300 dark:text-secondary-700">
          This tool provides preliminary design guidance only. Always verify
          with a qualified composites engineer. It is not a substitute for
          professional engineering judgement, company-specific design manuals, or
          regulatory certification requirements.
        </p>
      </div>
    </footer>
  );
}
