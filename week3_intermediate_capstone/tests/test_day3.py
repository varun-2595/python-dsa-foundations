"""Tests for Day 3: Sorting"""
import sys, os, random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week3_intermediate_capstone.day3_sorting import bubble_sort, merge_sort

def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]

def test_merge_sort():
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]

def test_merge_sort_large():
    nums = [random.randint(0, 1000) for _ in range(1000)]
    assert merge_sort(nums) == sorted(nums)
