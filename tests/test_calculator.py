# write unit tests for calculator functions
import pytest
from src.calculator import add, subtract, multiply, divide, power
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(2.5, 1.5) == 1.0
    assert subtract(3, 5) == -2
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply(2.5, 4) == 10.0
def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 3) == -2
    with pytest.raises(ValueError):
        divide(1, 0)
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(0, 5) == 0
    assert power(2, -1) == 0.5
    assert power(3, 2) == 9
    assert power(2, 10) == 1024
    assert power(1, 1000) == 1  