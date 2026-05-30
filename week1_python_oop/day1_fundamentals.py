"""
Day 1: Basic Data Types & Control Flow
"""
from typing import List

def sum_even_numbers(n: int) -> int:
    """Returns the sum of all even numbers from 1 to n using a loop."""
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total

def get_squares(n: int) -> List[int]:
    """Returns a list of squares from 1 to n using list comprehension."""
    return [i * i for i in range(1, n + 1)]

def process_variables(x: float, y: str) -> str:
    """Demonstrates type casting and basic control flow."""
    val = int(x) + int(y)
    if val > 10:
        return "High"
    return "Low"
