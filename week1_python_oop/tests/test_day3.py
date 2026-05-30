import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week1_python_oop.day3_oop_1 import BankAccount
from utils.complexity_analyzer import analyze_complexity

def test_bank_account():
    acc = BankAccount("Alice", 100)
    assert acc.get_balance() == 100
    
    analyze_complexity(acc.deposit, 50)
    assert acc.get_balance() == 150
    
    analyze_complexity(acc.withdraw, 30)
    assert acc.get_balance() == 120
