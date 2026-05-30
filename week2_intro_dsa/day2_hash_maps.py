"""
Day 2: Hash Maps & Sets
"""
from typing import List, Dict

def count_frequencies(arr: List[int]) -> Dict[int, int]:
    """Counts the frequency of elements in an array."""
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

def two_sum_easy(arr: List[int], target: int) -> List[int]:
    """Finds indices of two numbers that add up to target using a hash map."""
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

def deduplicate(arr: List[int]) -> List[int]:
    """Removes duplicates from an array using a set."""
    return list(set(arr))
