"""
Day 3: Two Pointers
"""
from typing import List

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome using two pointers."""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def reverse_array_in_place(arr: List[int]) -> None:
    """Reverses an array in place."""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
