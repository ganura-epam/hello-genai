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
