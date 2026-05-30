import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week1_python_oop.day2_functions import test_scope, math_operations, flexible_function
from utils.complexity_analyzer import analyze_complexity

def test_scope_test():
    assert analyze_complexity(test_scope) == "I am global and I am local"

def test_math_operations():
    assert analyze_complexity(math_operations, 5, 3, lambda x, y: x + y) == 8

def test_flexible_function():
    args, kwargs = flexible_function(1, 2, name="test")
    assert args == (1, 2)
    assert kwargs == {"name": "test"}
