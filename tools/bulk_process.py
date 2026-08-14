"""
bulk_process.py — Bulk-clean Python/text files in a directory tree.

Transformations applied per file:
  - Strip trailing whitespace from every line
  - Ensure the file ends with exactly one newline
  - Optionally replace tabs with spaces (--expand-tabs)

Usage:
    python tools/bulk_process.py --input <dir> [options]
"""

import argparse
import os
import sys
from pathlib import Path


SUPPORTED_EXTENSIONS = {".py", ".txt", ".md", ".csv", ".json"}


def process_file(path: Path, expand_tabs: int = 0, dry_run: bool = False) -> dict:
    """
    Clean a single file and return a change summary.

    Returns a dict with keys: path, lines_changed, trailing_newline_fixed, tabs_expanded, skipped.
    """
    try:
        original = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError) as exc:
        return {"path": str(path), "skipped": str(exc)}

    lines = original.splitlines()
    cleaned_lines = []
    lines_changed = 0
    tabs_expanded = 0

    for line in lines:
        new_line = line.rstrip()
        if expand_tabs:
            expanded = new_line.expandtabs(expand_tabs)
            if expanded != new_line:
                tabs_expanded += 1
            new_line = expanded
        if new_line != line:
            lines_changed += 1
        cleaned_lines.append(new_line)

    cleaned = "\n".join(cleaned_lines)
    trailing_newline_fixed = not original.endswith("\n") or original.endswith("\n\n")
    cleaned = cleaned.rstrip("\n") + "\n"

    changed = cleaned != original
    if changed and not dry_run:
        path.write_text(cleaned, encoding="utf-8")

    return {
        "path": str(path),
        "changed": changed,
        "lines_changed": lines_changed,
        "tabs_expanded": tabs_expanded,
        "trailing_newline_fixed": trailing_newline_fixed and changed,
        "skipped": None,
    }


def collect_files(root: Path, extensions: set, recursive: bool) -> list[Path]:
    """Return all files under root matching the given extensions."""
    if recursive:
        return [p for p in root.rglob("*") if p.is_file() and p.suffix in extensions]
    return [p for p in root.iterdir() if p.is_file() and p.suffix in extensions]


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="bulk_process.py",
        description="Bulk-clean Python/text files: strip trailing whitespace and fix newlines.",
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Directory to scan for files.",
    )
    parser.add_argument(
        "--ext",
        nargs="+",
        default=[".py"],
        metavar="EXT",
        help="File extensions to process (default: .py).",
    )
    parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Scan subdirectories recursively.",
    )
    parser.add_argument(
        "--expand-tabs",
        type=int,
        default=0,
        metavar="N",
        help="Replace tabs with N spaces (0 = disabled).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report changes without writing files.",
    )

    args = parser.parse_args()
    root = Path(args.input).resolve()

    if not root.is_dir():
        print(f"ERROR: '{root}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    extensions = {e if e.startswith(".") else f".{e}" for e in args.ext}
    files = collect_files(root, extensions, args.recursive)

    if not files:
        print(f"No files matching {extensions} found under '{root}'.")
        return

    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"{mode}Scanning: {root}")
    print(f"Extensions : {', '.join(sorted(extensions))}")
    print(f"Recursive  : {args.recursive}")
    print(f"Expand tabs: {args.expand_tabs if args.expand_tabs else 'disabled'}")
    print(f"Files found: {len(files)}\n")

    changed_count = skipped_count = 0
    for path in sorted(files):
        result = process_file(path, expand_tabs=args.expand_tabs, dry_run=args.dry_run)
        rel = Path(result["path"]).relative_to(root)

        if result.get("skipped"):
            print(f"  SKIP  {rel}  ({result['skipped']})")
            skipped_count += 1
        elif result["changed"]:
            details = []
            if result["lines_changed"]:
                details.append(f"{result['lines_changed']} line(s) stripped")
            if result["tabs_expanded"]:
                details.append(f"{result['tabs_expanded']} tab(s) expanded")
            if result["trailing_newline_fixed"]:
                details.append("trailing newline fixed")
            print(f"  {'WOULD FIX' if args.dry_run else 'FIXED'}  {rel}  ({', '.join(details)})")
            changed_count += 1
        else:
            print(f"  OK     {rel}")

    print(f"\nSummary: {changed_count} file(s) {'would be ' if args.dry_run else ''}modified, "
          f"{skipped_count} skipped, {len(files) - changed_count - skipped_count} already clean.")


if __name__ == "__main__":
    main()
