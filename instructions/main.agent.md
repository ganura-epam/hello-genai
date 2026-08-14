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
