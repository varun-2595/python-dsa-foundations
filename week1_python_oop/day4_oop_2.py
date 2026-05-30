"""
Day 4: OOP Part 2 - Inheritance, polymorphism, magic methods
"""

class Animal:
    """Base class for animals."""

    def __init__(self, name: str):
        # TODO: Implement
        pass

    def speak(self) -> str:
        # TODO: Implement
        pass

class Dog(Animal):
    """Dog inherits from Animal."""

    def speak(self) -> str:
        # TODO: Implement
        pass

    def __str__(self) -> str:
        # TODO: Implement
        pass

    def __eq__(self, other: object) -> bool:
        # TODO: Implement
        pass