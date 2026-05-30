"""
Day 4: Capstone Project — In-Memory Database
==============================================

Difficulty: Medium-Hard

Bring together everything you've learned: OOP, Hash Maps, Stacks, and logic.

Design a simple In-Memory Key-Value database that supports nested transactions.

Methods:
    set(key, value)
    get(key) -> value or None
    delete(key)
    
    begin() -> start a transaction
    commit() -> commit the current transaction
    rollback() -> revert the current transaction
"""

from typing import Any, Optional


class Database:
    def __init__(self):
        """
        Initialize your main data store and transaction stack.
        Hint: Use a dictionary for the main store, and a stack of dictionaries
        for active transactions.
        """
        # TODO: Implement
        pass

    def set(self, key: str, value: Any) -> None:
        """Set key to value."""
        # TODO: Implement
        pass

    def get(self, key: str) -> Optional[Any]:
        """Get the value for key. Returns None if not found or deleted."""
        # TODO: Implement
        pass

    def delete(self, key: str) -> None:
        """Delete key. If in transaction, mark as deleted."""
        # TODO: Implement
        pass

    def begin(self) -> None:
        """Start a new nested transaction."""
        # TODO: Implement
        pass

    def commit(self) -> bool:
        """
        Commit the current transaction.
        Apply changes to the previous transaction state or main store.
        Returns False if no active transaction.
        """
        # TODO: Implement
        pass

    def rollback(self) -> bool:
        """
        Rollback the current transaction, discarding its changes.
        Returns False if no active transaction.
        """
        # TODO: Implement
        pass
