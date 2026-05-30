"""
Day 2: Functions & Scope
"""
from typing import Callable, Any

GLOBAL_VAR = "I am global"

def test_scope() -> str:
    """Demonstrates variable scope."""
    local_var = "I am local"
    return f"{GLOBAL_VAR} and {local_var}"

def math_operations(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    """Uses a lambda or any callable to perform an operation."""
    return operation(a, b)

def flexible_function(*args: Any, **kwargs: Any) -> tuple:
    """Demonstrates *args and **kwargs."""
    return args, kwargs
