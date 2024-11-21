from Shape import Circle, Square, Rectangle, Triangle
from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory


def main():
    dp = DrawingProgram()

    # Add shapes using ShapeFactory
    circle = ShapeFactory.create_shape("Circle", 5)
    square = ShapeFactory.create_shape("Square", 4)
    rectangle = ShapeFactory.create_shape("Rectangle", 3, 6)
    triangle = ShapeFactory.create_shape("Triangle", 3, 4, 3, 4, 5)

    dp.add_shape(circle)
    dp.add_shape(square)
    dp.add_shape(rectangle)
    dp.add_shape(triangle)

    print("Shapes after addition:")
    print(dp)

    # Sort shapes
    dp.sort_shapes()
    print("\nShapes after sorting:")
    print(dp)

    # Remove all circles
    removed_count = dp.remove_shape(Circle(0))  # Dummy Circle to match type
    print(f"\nRemoved {removed_count} circles")
    print(dp)

    # Iterating over shapes
    print("\nIterating over shapes:")
    for shape in dp:
        print(shape)

if __name__ == "__main__":
    main()
