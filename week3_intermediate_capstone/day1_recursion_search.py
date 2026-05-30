"""
Day 1: Recursion & Searching
==============================

Difficulty: Easy-Medium

Problem 1: Factorial (Recursion basics)
Problem 2: Fibonacci Sequence (Recursion with multiple branches)
Problem 3: Binary Search (Iterative and Recursive)
"""

from typing import List


def factorial(n: int) -> int:
    """
    Calculate the factorial of n recursively.
    factorial(n) = n * factorial(n-1)
    Base case: factorial(0) = 1
    """
    # TODO: Implement
    pass


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number recursively.
    fib(n) = fib(n-1) + fib(n-2)
    Base cases: fib(0) = 0, fib(1) = 1
    
    (Note: This basic recursive version is O(2^n). 
     Try to implement it, but understand it's slow for large n).
    """
    # TODO: Implement
    pass


def binary_search(nums: List[int], target: int) -> int:
    """
    Find the target in a sorted array `nums` using Binary Search.
    Return the index if found, otherwise return -1.
    Time Complexity: O(log n)
    """
    # TODO: Implement
    pass


def binary_search_recursive(nums: List[int], target: int, left: int = 0, right: int = None) -> int:
    """
    Same as binary_search, but implemented recursively.
    """
    # TODO: Implement
    pass
