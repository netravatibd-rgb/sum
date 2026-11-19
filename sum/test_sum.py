import pytest
from sum import add

def test_add():
    assert add(2, 3) == 5

def test_add_two_numbers():
    assert add(10, 20) == 30

def test_add_zero():
    assert add(0, 0) == 0