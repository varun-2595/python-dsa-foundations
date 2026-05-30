"""
Day 2: Linked Lists
=====================

Difficulty: Easy-Medium

A linked list is a linear data structure where elements are not stored 
at contiguous memory locations.

Problem 1: ListNode definition
Problem 2: Traverse and print a linked list
Problem 3: Reverse a linked list
"""

from typing import List, Optional


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    """
    Traverse a linked list and return its values as a Python list.
    """
    # TODO: Implement
    pass


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list in-place.
    Return the new head.
    Time: O(n), Space: O(1)
    """
    # TODO: Implement
    pass
