"""
Day 3: OOP Part 1 - Classes, init, instance methods, encapsulation
"""

class BankAccount:
    """A simple bank account demonstrating encapsulation."""
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance  # private attribute
        
    def deposit(self, amount: float) -> float:
        """Deposits amount to the account."""
        if amount > 0:
            self.__balance += amount
        return self.__balance
        
    def withdraw(self, amount: float) -> float:
        """Withdraws amount if sufficient balance exists."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance
        
    def get_balance(self) -> float:
        """Returns current balance."""
        return self.__balance
