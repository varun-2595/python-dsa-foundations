import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week2_intro_dsa.day2_hash_maps import count_frequencies, two_sum_easy, deduplicate

def test_count_frequencies():
    assert count_frequencies([1, 2, 2, 3]) == {1: 1, 2: 2, 3: 1}

def test_two_sum_easy():
    assert two_sum_easy([2, 7, 11, 15], 9) == [0, 1]

def test_deduplicate():
    assert sorted(deduplicate([1, 2, 2, 3])) == [1, 2, 3]
