"""Tests for Day 1: Recursion & Searching"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week3_intermediate_capstone.day1_recursion_search import factorial, fibonacci, binary_search, binary_search_recursive

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([], 1) == -1
    assert binary_search([1], 1) == 0

def test_binary_search_recursive():
    assert binary_search_recursive([1, 2, 3, 4, 5], 3) == 2
    assert binary_search_recursive([1, 2, 3, 4, 5], 6) == -1
    assert binary_search_recursive([], 1) == -1
    assert binary_search_recursive([1], 1) == 0
