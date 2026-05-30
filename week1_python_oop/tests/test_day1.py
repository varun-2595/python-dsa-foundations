import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week1_python_oop.day1_fundamentals import sum_even_numbers, get_squares, process_variables
from utils.complexity_analyzer import analyze_complexity

def test_sum_even_numbers():
    assert analyze_complexity(sum_even_numbers, 10) == 30

def test_get_squares():
    assert analyze_complexity(get_squares, 4) == [1, 4, 9, 16]

def test_process_variables():
    assert process_variables(5.5, "6") == "High"
    assert process_variables(3.1, "4") == "Low"
