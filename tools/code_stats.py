"""
code_stats.py — Analyse Python source files and print a summary report.

Usage:
    python tools/code_stats.py [--path <dir>] [--help]
"""

import argparse
import ast
import os
from pathlib import Path


def count_lines(path: Path) -> dict:
    """Return line count breakdown for a single Python file."""
    code_lines = blank_lines = comment_lines = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                blank_lines += 1
            elif stripped.startswith("#"):
                comment_lines += 1
            else:
                code_lines += 1
    return {
        "code": code_lines,
        "blank": blank_lines,
        "comment": comment_lines,
        "total": code_lines + blank_lines + comment_lines,
    }


def count_functions(path: Path) -> int:
    """Return the number of top-level and nested function definitions."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        return sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
    except SyntaxError:
        return 0


def analyse(root: Path) -> None:
    """Walk *root* for .py files and print a stats table."""
    py_files = sorted(root.rglob("*.py"))
    if not py_files:
        print(f"No Python files found under '{root}'.")
        return

    totals = {"code": 0, "blank": 0, "comment": 0, "total": 0, "functions": 0}
    rows = []

    for path in py_files:
        rel = path.relative_to(root)
        stats = count_lines(path)
        funcs = count_functions(path)
        rows.append((str(rel), stats["total"], stats["code"], stats["blank"], stats["comment"], funcs))
        for key in ("code", "blank", "comment", "total"):
            totals[key] += stats[key]
        totals["functions"] += funcs

    col_w = max(len(r[0]) for r in rows) + 2
    header = f"{'File':<{col_w}} {'Total':>6} {'Code':>6} {'Blank':>6} {'Comment':>8} {'Funcs':>6}"
    sep = "-" * len(header)
    print(sep)
    print(header)
    print(sep)
    for row in rows:
        print(f"{row[0]:<{col_w}} {row[1]:>6} {row[2]:>6} {row[3]:>6} {row[4]:>8} {row[5]:>6}")
    print(sep)
    print(
        f"{'TOTAL':<{col_w}} {totals['total']:>6} {totals['code']:>6} "
        f"{totals['blank']:>6} {totals['comment']:>8} {totals['functions']:>6}"
    )
    print(sep)
    print(f"\nFiles analysed : {len(py_files)}")
    print(f"Total lines    : {totals['total']}")
    print(f"Code lines     : {totals['code']}")
    print(f"Functions found: {totals['functions']}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="code_stats.py",
        description="Analyse Python source files and print a line/function summary.",
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Root directory to scan (default: current directory)",
    )
    args = parser.parse_args()
    root = Path(args.path).resolve()
    if not root.is_dir():
        parser.error(f"Path does not exist or is not a directory: {root}")
    print(f"Scanning: {root}\n")
    analyse(root)


if __name__ == "__main__":
    main()
