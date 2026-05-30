"""
Day 4: OOP Part 2 - Inheritance, polymorphism, magic methods
"""

class Animal:
    """Base class for animals."""
    def __init__(self, name: str):
        self.name = name
        
    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):
    """Dog inherits from Animal."""
    def speak(self) -> str:
        return "Woof!"
        
    def __str__(self) -> str:
        return f"Dog named {self.name}"
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dog):
            return NotImplemented
        return self.name == other.name
