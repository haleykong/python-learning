import pytest
import source.shapes as shapes

# Global Fixtures
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(1, 1)
