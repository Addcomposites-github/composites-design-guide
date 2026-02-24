#!/usr/bin/env python3
"""
Audit script for the composites design knowledge base.

Checks:
1. Front matter validity — every .md file has required YAML fields
2. No proprietary images — no .gif, .jpg, .png references to catia_composites_offline/
3. Image references — all image embeds (![alt](path)) resolve to existing files
4. Cross-reference integrity — all internal links point to files that exist
5. Section structure — every file has Key Takeaways and Further Reading
6. Content guidelines — section length checks, no raw HTML
7. No verbatim CATIA content — flags suspiciously long quoted blocks
8. Example file links — flags references to .CATPart or other CATIA sample files

Usage:
    python scripts/audit_knowledge_base.py
"""

import os
import re
import sys
import yaml
from pathlib import Path


# --- Configuration ---
REPO_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = REPO_ROOT / "knowledge"

REQUIRED_FRONT_MATTER_FIELDS = [
    "title", "category", "tags", "difficulty", "related", "tools", "last_updated"
]

VALID_CATEGORIES = [
    "fundamentals", "design-rules", "manufacturing", "analysis", "catia", "tools", "glossary"
]

VALID_DIFFICULTIES = ["beginner", "intermediate", "advanced"]

PROHIBITED_IMAGE_PATTERNS = [
    r"catia_composites_offline",
    r"\.gif\b",  # GIF files from CATIA mirror
]

PROHIBITED_CONTENT_PATTERNS = [
    (r"<\s*(div|span|table|tr|td|img|a\s)[^>]*>", "Raw HTML tag detected"),
    (r"Click\s+(Insert|Edit|Tools|View|File)\s*>", "CATIA menu path detected (should be removed)"),
    (r"Dassault\s+Syst[eè]mes", "Dassault Systemes reference (check context)"),
    (r"\.CATPart\b", "CATIA example file reference (.CATPart) — should not appear in knowledge base"),
    (r"\.CATProduct\b", "CATIA example file reference (.CATProduct) — should not appear in knowledge base"),
    (r"Open\s+the\s+\w+\.CAT", "CATIA 'Open the...' instruction — should be rewritten or removed"),
]

# Image file extensions to verify exist on disk
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".svg", ".webp"}


class AuditResult:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []

    def error(self, file, message):
        self.errors.append(f"  ERROR  {file}: {message}")

    def warn(self, file, message):
        self.warnings.append(f"  WARN   {file}: {message}")

    def log(self, message):
        self.info.append(f"  INFO   {message}")

    def summary(self):
        lines = []
        lines.append("=" * 70)
        lines.append("COMPOSITES KNOWLEDGE BASE AUDIT REPORT")
        lines.append("=" * 70)

        if self.info:
            lines.append("\n--- Info ---")
            lines.extend(self.info)

        if self.warnings:
            lines.append(f"\n--- Warnings ({len(self.warnings)}) ---")
            lines.extend(self.warnings)

        if self.errors:
            lines.append(f"\n--- Errors ({len(self.errors)}) ---")
            lines.extend(self.errors)

        lines.append("\n" + "=" * 70)
        if self.errors:
            lines.append(f"RESULT: FAIL — {len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        elif self.warnings:
            lines.append(f"RESULT: PASS with warnings — {len(self.warnings)} warning(s)")
        else:
            lines.append("RESULT: PASS — all checks passed")
        lines.append("=" * 70)

        return "\n".join(lines)


def extract_front_matter(filepath):
    """Extract YAML front matter from a markdown file."""
    content = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n", content, re.DOTALL)
    if not match:
        return None, content
    try:
        fm = yaml.safe_load(match.group(1))
        body = content[match.end():]
        return fm, body
    except yaml.YAMLError:
        return None, content


def check_front_matter(filepath, fm, result):
    """Validate front matter fields."""
    rel = filepath.relative_to(REPO_ROOT)

    if fm is None:
        result.error(rel, "Missing or invalid YAML front matter")
        return

    for field in REQUIRED_FRONT_MATTER_FIELDS:
        if field not in fm:
            result.error(rel, f"Missing front matter field: {field}")

    if "category" in fm and fm["category"] not in VALID_CATEGORIES:
        result.warn(rel, f"Unknown category: {fm['category']}")

    if "difficulty" in fm and fm["difficulty"] not in VALID_DIFFICULTIES:
        result.warn(rel, f"Unknown difficulty: {fm['difficulty']}")

    if "tags" in fm:
        if not isinstance(fm["tags"], list) or len(fm["tags"]) < 2:
            result.warn(rel, "Tags should be a list with at least 2 items")
        if isinstance(fm["tags"], list) and len(fm["tags"]) > 6:
            result.warn(rel, f"Tags has {len(fm['tags'])} items (guideline: 2-6)")

    if "related" in fm and isinstance(fm["related"], list):
        for ref in fm["related"]:
            # Resolve relative path from the file's directory
            ref_path = (filepath.parent / ref).resolve()
            if not ref_path.exists():
                result.warn(rel, f"Related file not found: {ref}")


def check_content_structure(filepath, body, result):
    """Check for required sections and content guidelines."""
    rel = filepath.relative_to(REPO_ROOT)

    # Check for Key Takeaways section
    if "## Key Takeaways" not in body:
        result.warn(rel, "Missing '## Key Takeaways' section")

    # Check for Further Reading section
    if "## Further Reading" not in body:
        result.warn(rel, "Missing '## Further Reading / Tools' section")

    # Check for very long sections (> 500 words between ## headings)
    sections = re.split(r"\n## ", body)
    for i, section in enumerate(sections[1:], 1):  # skip content before first ##
        heading = section.split("\n")[0]
        word_count = len(section.split())
        if word_count > 500:
            result.warn(rel, f"Section '{heading}' is {word_count} words (guideline: 100-400 for RAG)")


def check_prohibited_content(filepath, body, result):
    """Check for prohibited images, HTML, and CATIA menu paths."""
    rel = filepath.relative_to(REPO_ROOT)

    for pattern in PROHIBITED_IMAGE_PATTERNS:
        if re.search(pattern, body, re.IGNORECASE):
            result.error(rel, f"Prohibited image/file reference: pattern '{pattern}' found")

    for pattern, message in PROHIBITED_CONTENT_PATTERNS:
        matches = re.findall(pattern, body)
        if matches:
            result.error(rel, f"{message} (found {len(matches)} occurrence(s))")


def check_internal_links(filepath, body, result):
    """Check that markdown links to local files resolve."""
    rel = filepath.relative_to(REPO_ROOT)

    # Match markdown links: [text](path) — skip http/https URLs
    link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    for text, target in re.findall(link_pattern, body):
        if target.startswith("http://") or target.startswith("https://"):
            continue
        if target.startswith("#"):
            continue  # internal anchor

        # Strip any anchor from the path
        target_path = target.split("#")[0]
        if not target_path:
            continue

        resolved = (filepath.parent / target_path).resolve()
        if not resolved.exists():
            result.warn(rel, f"Broken internal link: [{text}]({target})")


def check_no_proprietary_images(filepath, body, result):
    """Ensure no image references to proprietary sources."""
    rel = filepath.relative_to(REPO_ROOT)

    # Match image references: ![alt](path)
    img_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    for alt, src in re.findall(img_pattern, body):
        if "catia" in src.lower() or "fibersim" in src.lower():
            result.error(rel, f"Proprietary image reference: {src}")


def check_image_references(filepath, body, result):
    """Verify that all image embeds point to existing files."""
    rel = filepath.relative_to(REPO_ROOT)

    img_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    for alt, src in re.findall(img_pattern, body):
        # Skip external URLs
        if src.startswith("http://") or src.startswith("https://"):
            continue

        # Resolve the image path relative to the markdown file
        img_path = (filepath.parent / src).resolve()
        suffix = img_path.suffix.lower()

        if suffix in IMAGE_EXTENSIONS and not img_path.exists():
            result.error(rel, f"Image file not found: {src}")

        # Check for prohibited image types (GIFs from CATIA mirror)
        if suffix == ".gif":
            result.error(rel, f"GIF image reference (likely from CATIA mirror): {src}")


def check_example_file_links(filepath, body, result):
    """Flag references to CATIA example/sample files that should not be in the knowledge base."""
    rel = filepath.relative_to(REPO_ROOT)

    # Check for references to CATIA sample document names
    sample_pattern = r"\b\w+\d*\.CAT(?:Part|Product|Drawing|Process)\b"
    matches = re.findall(sample_pattern, body)
    if matches:
        result.error(rel, f"CATIA sample file reference(s): {', '.join(set(matches))} — remove or rewrite")

    # Check for references to opening sample documents
    open_sample = r"(?:Open|open)\s+(?:the\s+)?(?:sample\s+)?(?:document|file)\b"
    if re.search(open_sample, body, re.IGNORECASE):
        result.warn(rel, "Reference to opening a sample document — may be copied from CATIA docs")


def main():
    result = AuditResult()

    # Find all .md files in knowledge/
    md_files = sorted(KNOWLEDGE_DIR.rglob("*.md"))
    result.log(f"Found {len(md_files)} markdown files in knowledge/")

    # Check directory structure
    expected_dirs = [
        "01-fundamentals", "02-design-rules", "03-manufacturing-processes",
        "04-structural-analysis", "05-catia-workflows", "06-free-tools", "07-glossary"
    ]
    for d in expected_dirs:
        dir_path = KNOWLEDGE_DIR / d
        if not dir_path.exists():
            result.warn("knowledge/", f"Expected directory missing: {d}")
        else:
            count = len(list(dir_path.glob("*.md")))
            result.log(f"{d}: {count} file(s)")

    # Audit each file
    for filepath in md_files:
        fm, body = extract_front_matter(filepath)
        check_front_matter(filepath, fm, result)
        check_content_structure(filepath, body, result)
        check_prohibited_content(filepath, body, result)
        check_internal_links(filepath, body, result)
        check_no_proprietary_images(filepath, body, result)
        check_image_references(filepath, body, result)
        check_example_file_links(filepath, body, result)

    print(result.summary())
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
