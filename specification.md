# Specification: hello-genai Calculator Prototype

## Overview
A rapid prototype of a command-line calculator application built in Python. The prototype validates the core user interaction model and arithmetic engine before full implementation.

## Problem Statement
Developers and testers need a lightweight, scriptable calculator that can be invoked from the terminal without opening a browser or GUI application. Existing solutions are either too heavy or not programmable.

## Goals
- Validate that the arithmetic engine (`calculator.py`) covers all required operations
- Confirm the CLI interaction model before investing in a full UI
- Demonstrate the project structure and coding conventions to stakeholders

## Prototype Scope

### In Scope
- CLI interface accepting `--operation` and two numeric operands
- Six arithmetic operations: add, subtract, multiply, divide, power, modulo
- Graceful error handling for division/modulo by zero
- `--help` usage output

### Out of Scope (deferred to full build)
- History / session persistence
- Expression parsing (e.g. `2 + 3 * 4`)
- Web or GUI frontend
- Authentication or user accounts

## User Stories

| # | As a… | I want to… | So that… |
|---|-------|-----------|---------|
| 1 | Developer | Run `python main.py --operation add 5 3` | I get `8.0` without writing a script |
| 2 | Developer | See a `--help` message | I can discover available operations |
| 3 | QA Engineer | Pass invalid inputs | I get a descriptive error, not a traceback |
| 4 | Developer | Import `calculator.py` as a module | I can reuse operations in other scripts |

## Acceptance Criteria
- All six operations produce correct results for float inputs
- `--help` lists all supported operations and arguments
- `divide(x, 0)` and `modulo(x, 0)` raise `ValueError` with clear messages
- Running `python main.py --operation divide 10 0` exits with a non-zero code and prints an error

## Tech Stack
- Language: Python 3.11+
- CLI framework: `argparse` (stdlib — no external deps)
- Test framework: `pytest` (deferred to full build)

## Prototype Success Metrics
- All six CLI operations return correct output in under 100ms
- Zero unhandled exceptions on valid inputs
- Code review approved by at least one peer
