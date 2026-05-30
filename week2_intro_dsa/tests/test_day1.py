import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week2_intro_dsa.day1_arrays_strings import reverse_string, find_max

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_find_max():
    assert find_max([1, 5, 3, 9, 2]) == 9
