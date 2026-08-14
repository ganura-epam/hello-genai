# Code Stats Tool Instructions

## Role
When asked to analyse the codebase, run `tools/code_stats.py` and interpret the output for the user.

## What the Tool Does
`tools/code_stats.py` scans a directory recursively for `.py` files and reports:
- Total, code, blank, and comment line counts per file
- Number of function definitions per file
- Project-wide totals and a summary

## How to Invoke
```bash
# Analyse the entire project
python tools/code_stats.py

# Analyse a specific subdirectory
python tools/code_stats.py --path <directory>

# Show usage help
python tools/code_stats.py --help
```

## When to Use This Tool
- Before a code review to get a quick size overview
- After adding new modules to verify coverage growth
- When asked "how big is the codebase?" or "how many functions are defined?"

## Interpreting Output
- **Code lines**: executable statements — the primary measure of complexity
- **Comment lines**: lines starting with `#` — high ratio may indicate over-commenting
- **Blank lines**: whitespace — PEP 8 recommends blank lines for readability
- **Funcs**: total function definitions including nested ones

## Limitations
- Does not count class methods separately from standalone functions
- Does not report test coverage or cyclomatic complexity
- Files with syntax errors report 0 functions (line counts are still accurate)
