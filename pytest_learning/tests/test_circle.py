import math
import source.shapes as shapes


class TestCircle:

    def setup_method(self, method):
        """Setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    
    def teardown_method(self, method):
        """Teardown any state that was previously setup with a setup_method
        call.
        """
        print(f"Tearing down {method}")
        del self.circle


    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius


    def test_area(self):
        assert self.circle.area() == math.pi * (self.circle.radius ** 2)
    
    
    def test_not_equal_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()