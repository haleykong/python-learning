import pytest
import source.shapes as shapes

def test_area(my_rectangle):
    return my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle):
    return my_rectangle.perimeter == 60


def test_not_equal(my_rectangle, other_rectangle):
    assert my_rectangle != other_rectangle 