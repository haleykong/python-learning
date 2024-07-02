# test_calculator.py

# Put code into different file from test
from calculator import add
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_raises_integer_plus_string():
    with pytest.raises(TypeError):
        add(1, 'a')
