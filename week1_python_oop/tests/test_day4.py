import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week1_python_oop.day4_oop_2 import Dog, Animal
from utils.complexity_analyzer import analyze_complexity

def test_dog_inheritance():
    d1 = Dog("Rex")
    d2 = Dog("Rex")
    d3 = Dog("Max")
    
    assert analyze_complexity(d1.speak) == "Woof!"
    assert str(d1) == "Dog named Rex"
    assert d1 == d2
    assert d1 != d3
