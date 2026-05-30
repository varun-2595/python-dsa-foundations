import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week2_intro_dsa.day3_two_pointers import is_palindrome, reverse_array_in_place

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False

def test_reverse_array_in_place():
    arr = [1, 2, 3, 4]
    reverse_array_in_place(arr)
    assert arr == [4, 3, 2, 1]
