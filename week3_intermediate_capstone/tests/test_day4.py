"""Tests for Day 4: Capstone Database"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from week3_intermediate_capstone.day4_capstone_kvstore import Database

def test_set_and_get():
    db = Database()
    db.set("a", 10)
    assert db.get("a") == 10
    assert db.get("b") is None

def test_delete():
    db = Database()
    db.set("a", 10)
    db.delete("a")
    assert db.get("a") is None

def test_transaction_commit():
    db = Database()
    db.set("a", 10)
    db.begin()
    db.set("a", 20)
    db.set("b", 30)
    assert db.get("a") == 20
    db.commit()
    assert db.get("a") == 20
    assert db.get("b") == 30

def test_transaction_rollback():
    db = Database()
    db.set("a", 10)
    db.begin()
    db.set("a", 20)
    assert db.get("a") == 20
    db.rollback()
    assert db.get("a") == 10

def test_nested_transactions():
    db = Database()
    db.set("a", 10)
    
    db.begin()
    db.set("a", 20)
    
    db.begin()
    db.set("a", 30)
    assert db.get("a") == 30
    db.rollback()
    
    assert db.get("a") == 20
    db.commit()
    
    assert db.get("a") == 20

def test_commit_no_transaction():
    db = Database()
    assert db.commit() is False

def test_rollback_no_transaction():
    db = Database()
    assert db.rollback() is False
