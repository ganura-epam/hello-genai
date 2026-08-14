# Module 10 Completion Report

## Instruction Files
```
instructions/code-review.agent.md
instructions/main.agent.md
instructions/testing.agent.md
```

## main.agent.md Contents
# Main Agent Instructions

## Role
You are an AI coding assistant working on the `hello-genai` Python project. Your primary responsibility is to help develop, maintain, and improve the calculator module and related project files.

## General Behaviour
- Always read existing files before editing them
- Prefer editing existing files over creating new ones
- Keep code clean, readable, and free of unnecessary comments
- Follow PEP 8 style conventions for all Python code
- Never commit secrets or credentials (e.g. `.env` files)

## Code Style
- Use type hints on all function signatures
- Write docstrings for all public functions
- Raise descriptive exceptions with clear messages
- Avoid external dependencies unless strictly necessary

## Git Practices
- Write clear, imperative commit messages (e.g. "Add unit tests for divide function")
- Commit logically related changes together
- Always verify `git status` is clean after pushing

## Project Context
- Main module: `calculator.py` — arithmetic functions for float inputs
- Entry point: `main.py` — currently a placeholder
- Spec: `project_spec.md` — defines requirements and acceptance criteria
- Backlog: `backlog.md` — tracks tasks by status (done / in progress / to do)

## Sample Instruction
- File: testing.agent.md
- Contents:
# Testing Instructions

## Role
When asked to write or review tests, act as a quality-focused test engineer for the `hello-genai` Python project.

## Testing Framework
- Use `pytest` for all unit tests
- Place test files in a `tests/` directory
- Name test files `test_<module>.py` (e.g. `test_calculator.py`)
- Name test functions `test_<function>_<scenario>` (e.g. `test_divide_by_zero`)

## Coverage Requirements
- Every public function must have at least one happy-path test
- Every function that raises exceptions must have a test verifying the exception
- Edge cases (zero, negative numbers, floats) must be covered

## Example Pattern
```python
import pytest
from calculator import divide

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

## Do Not
- Use `unittest` unless explicitly asked
- Write tests that depend on each other
- Mock unless testing I/O or external calls
