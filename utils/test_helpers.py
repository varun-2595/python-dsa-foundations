"""
Test Helpers — Shared utilities for test cases across all weeks.

Provides timing utilities, input generators, and assertion helpers
for the interview prep test suite.
"""

import time
import random
import string
from typing import Callable, Any, List, Tuple
from functools import wraps


def run_with_timer(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
    """
    Run a function and return (result, elapsed_time_ms).

    Example:
        result, elapsed = run_with_timer(my_sort, large_list)
        assert elapsed < 1000, "Solution too slow!"
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = (time.perf_counter() - start) * 1000  # ms
    return result, elapsed


def assert_time_limit(func: Callable, args: tuple, time_limit_ms: float = 2000,
                       description: str = ""):
    """
    Assert that a function completes within a time limit.

    Args:
        func: Function to test.
        args: Tuple of arguments to pass.
        time_limit_ms: Maximum allowed time in milliseconds.
        description: Description for error message.
    """
    result, elapsed = run_with_timer(func, *args)
    assert elapsed < time_limit_ms, (
        f"{'[' + description + '] ' if description else ''}"
        f"Time limit exceeded: {elapsed:.1f}ms > {time_limit_ms}ms"
    )
    return result


def generate_large_input(size: int, input_type: str = "int_list", **kwargs) -> Any:
    """
    Generate large test inputs of various types.

    Args:
        size: Size of the input.
        input_type: One of 'int_list', 'string', 'sorted_list', 'matrix',
                    'string_list', 'pairs', 'graph_edges'.
        **kwargs: Additional parameters (e.g., min_val, max_val for int_list).

    Returns:
        Generated input of the specified type.
    """
    if input_type == "int_list":
        min_val = kwargs.get("min_val", -10**6)
        max_val = kwargs.get("max_val", 10**6)
        return [random.randint(min_val, max_val) for _ in range(size)]

    elif input_type == "sorted_list":
        min_val = kwargs.get("min_val", -10**6)
        max_val = kwargs.get("max_val", 10**6)
        return sorted(random.randint(min_val, max_val) for _ in range(size))

    elif input_type == "string":
        chars = kwargs.get("chars", string.ascii_lowercase)
        return "".join(random.choice(chars) for _ in range(size))

    elif input_type == "string_list":
        word_len = kwargs.get("word_len", 5)
        return ["".join(random.choices(string.ascii_lowercase, k=word_len)) for _ in range(size)]

    elif input_type == "matrix":
        rows = size
        cols = kwargs.get("cols", size)
        min_val = kwargs.get("min_val", 0)
        max_val = kwargs.get("max_val", 100)
        return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    elif input_type == "pairs":
        min_val = kwargs.get("min_val", 0)
        max_val = kwargs.get("max_val", 10**6)
        return [(random.randint(min_val, max_val), random.randint(min_val, max_val))
                for _ in range(size)]

    elif input_type == "graph_edges":
        # Generate random graph edges for a graph with `size` nodes
        num_edges = kwargs.get("num_edges", size * 2)
        edges = set()
        for _ in range(num_edges):
            u = random.randint(0, size - 1)
            v = random.randint(0, size - 1)
            if u != v:
                edges.add((min(u, v), max(u, v)))
        return list(edges)

    else:
        raise ValueError(f"Unknown input_type: {input_type}")


def timed_test(time_limit_ms: float = 2000):
    """
    Decorator that enforces a time limit on a test function.

    Usage:
        @timed_test(time_limit_ms=1000)
        def test_performance():
            result = my_function(large_input)
            assert result == expected
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            assert elapsed < time_limit_ms, (
                f"{func.__name__}: Time limit exceeded: {elapsed:.1f}ms > {time_limit_ms}ms"
            )
            return result
        return wrapper
    return decorator


class TestCase:
    """
    A test case container for LeetCode-style problems.

    Usage:
        cases = [
            TestCase(args=([2, 7, 11, 15], 9), expected=[0, 1], name="basic"),
            TestCase(args=([3, 2, 4], 6), expected=[1, 2], name="duplicates"),
        ]
        for tc in cases:
            assert func(*tc.args) == tc.expected, f"Failed: {tc.name}"
    """

    def __init__(self, args: tuple, expected: Any, name: str = ""):
        self.args = args if isinstance(args, tuple) else (args,)
        self.expected = expected
        self.name = name

    def run(self, func: Callable) -> bool:
        """Run the test case and return True if passed."""
        result = func(*self.args)
        return result == self.expected

    def assert_pass(self, func: Callable):
        """Run the test case and assert it passes."""
        result = func(*self.args)
        assert result == self.expected, (
            f"Test '{self.name}' failed:\n"
            f"  Input:    {self.args}\n"
            f"  Expected: {self.expected}\n"
            f"  Got:      {result}"
        )

    def __repr__(self):
        return f"TestCase(name='{self.name}', args={self.args}, expected={self.expected})"
