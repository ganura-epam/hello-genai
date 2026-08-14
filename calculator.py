"""Basic calculator functions."""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"2 ** 8 = {power(2, 8)}")
    print(f"17 % 5 = {modulo(17, 5)}")
