from Shape import Shape, Circle, Square, Rectangle, Triangle
from ShapeFactory import ShapeFactory

# Initialize the class DrawingProgram
class DrawingProgram:
    def __init__(self, shapes=None):
        self.shapes = shapes if shapes else []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        removed_count = sum(1 for s in self.shapes if type(s) == type(shape))
        self.shapes = [s for s in self.shapes if type(s) != type(shape)]
        return removed_count

    def print_shape(self, shape_type):
        for shape in self.shapes:
            if isinstance(shape, shape_type):
                print(shape)

    def sort_shapes(self):
        self.shapes.sort(key=lambda s: (s.name, s.area()))

    def __str__(self):
        return "\n".join(str(shape) for shape in self.shapes)

    def get_shape(self, index):
        return self.shapes[index]

    def set_shape(self, index, shape):
        self.shapes[index] = shape

# Iterator class
class DrawingProgramIterator:
    def __init__(self, drawing_program):
        self._shapes = drawing_program.shapes
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._shapes):
            shape = self._shapes[self._index]
            self._index += 1
            return shape
        else:
            raise StopIteration

# Add the iterator capability to DrawingProgram
DrawingProgram.__iter__ = lambda self: DrawingProgramIterator(self)
