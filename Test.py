from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory
from Shape import Circle, Square, Rectangle, Triangle
import unittest

class TestDrawingProgram(unittest.TestCase):
    def test_add_and_remove_shapes(self):
        dp = DrawingProgram()
        circle = ShapeFactory.create_shape("Circle", 5)
        dp.add_shape(circle)
        self.assertEqual(len(dp.shapes), 1)

        removed_count = dp.remove_shape(Circle(0))
        self.assertEqual(removed_count, 1)
        self.assertEqual(len(dp.shapes), 0)

    def test_sort_shapes(self):
        dp = DrawingProgram()
        dp.add_shape(ShapeFactory.create_shape("Square", 4))
        dp.add_shape(ShapeFactory.create_shape("Circle", 3))
        dp.add_shape(ShapeFactory.create_shape("Rectangle", 2, 5))
        dp.sort_shapes()

        self.assertEqual(dp.shapes[0].name, "Circle")

    def test_iterator(self):
        dp = DrawingProgram()
        dp.add_shape(ShapeFactory.create_shape("Square", 4))
        dp.add_shape(ShapeFactory.create_shape("Circle", 3))

        shapes = [shape for shape in dp]
        self.assertEqual(len(shapes), 2)

if __name__ == "__main__":
    unittest.main()
