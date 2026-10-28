def add(a, b):
    """Add two numbers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be a number")
    return a + b

print(add(2, 3))
