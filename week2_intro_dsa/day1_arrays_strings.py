"""
Day 1: Arrays & Strings
"""
from typing import List

def reverse_string(s: str) -> str:
    """Reverses a string using basic slicing."""
    return s[::-1]

def find_max(arr: List[int]) -> int:
    """Finds the maximum element in an array."""
    if not arr:
        raise ValueError("Array is empty")
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val
