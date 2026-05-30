"""Tests for Day 2: Linked Lists"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week3_intermediate_capstone.day2_linked_lists import ListNode, linked_list_to_array, reverse_list

def test_linked_list_to_array():
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert linked_list_to_array(head) == [1, 2, 3]
    assert linked_list_to_array(None) == []

def test_reverse_list():
    head = ListNode(1, ListNode(2, ListNode(3)))
    reversed_head = reverse_list(head)
    assert linked_list_to_array(reversed_head) == [3, 2, 1]
    
    assert reverse_list(None) is None
    assert linked_list_to_array(reverse_list(ListNode(1))) == [1]
