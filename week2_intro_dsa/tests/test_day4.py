import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week2_intro_dsa.day4_stacks_queues import is_valid_parentheses, SimpleQueue

def test_is_valid_parentheses():
    assert is_valid_parentheses("()") is True
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False

def test_simple_queue():
    q = SimpleQueue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() is None
