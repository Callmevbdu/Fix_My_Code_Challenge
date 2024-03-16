#!/usr/bin/python3

class Square:
    """Represents a square with width and height."""

    def __init__(self, width=0, height=0):
        """
        Initializes a Square object.

        Args:
            width (int, optional): The width of the square. Defaults to 0.
            height (int, optional): The height of the square. Defaults to 0.
        """
        self.width = width
        self.height = height

        # Check for geometric perfection during initialization (optional)
        if self.width != self.height:
            print("This object represents a rectangle, not a perfect square (geometrically).")

    def area(self):
        """Calculates and returns the area of the square."""
        return self.width * self.width

    def is_perfect_square_area(self):
        """
        Checks if the square's area is a perfect square (area is an integer square).

        Returns:
            bool: True if the area is a perfect square, False otherwise.
        """
        area = self.area()  # Calculate the area
        return area == int(area)  # Check if area is equal to its integer part

    def __str__(self):
        """Returns a string representation of the square in the format 'width/height'."""
        return f"{self.width}/{self.height}"

if __name__ == "__main__":

    # Option 1: Geometrically perfect square
    s1 = Square(width=10, height=10)
    print("Square 1:", s1)
    print("Area of Square 1:", s1.area())
    print("Is Square 1 a perfect square (area-wise):", s1.is_perfect_square_area())
    print()

    # Option 2: Square with potentially non-perfect area
    s2 = Square(width=12, height=9)
    print("Square 2:", s2)
    print("Area of Square 2:", s2.area())
    print("Is Square 2 a perfect square (area-wise):", s2.is_perfect_square_area())
