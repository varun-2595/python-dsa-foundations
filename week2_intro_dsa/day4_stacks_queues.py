"""
Day 4: Stacks & Queues
"""
from collections import deque
from typing import Any

def is_valid_parentheses(s: str) -> bool:
    """Checks for valid parentheses using a stack."""
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack

class SimpleQueue:
    """A simple queue simulation using deque."""
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, item: Any) -> None:
        self.queue.append(item)
        
    def dequeue(self) -> Any:
        if not self.queue:
            return None
        return self.queue.popleft()
        
    def size(self) -> int:
        return len(self.queue)
