from Shape import Circle, Square, Rectangle, Triangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_name, *args):
        if shape_name == "Circle":
            return Circle(*args)
        elif shape_name == "Square":
            return Square(*args)
        elif shape_name == "Rectangle":
            return Rectangle(*args)
        elif shape_name == "Triangle":
            return Triangle(*args)
        else:
            raise ValueError("Unknown shape type")
