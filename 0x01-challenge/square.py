#!/usr/bin/python3

class Square:  # Use PascalCase for class names
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

    def area(self):
        """Calculates and returns the area of the square."""
        return self.width * self.width  # Consistent calculation for a square

    def perimeter(self):
        """Calculates and returns the perimeter of the square."""
        if self.width != self.height:  # Check if it's actually a rectangle
            return "This is not a square. Use separate calculations for rectangles."
        else:
            return 4 * self.width  # Perimeter for a square

    def __str__(self):
        """Returns a string representation of the square in the format 'width/height'."""
        return f"{self.width}/{self.height}"  # Use f-strings for cleaner formatting

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)  # Output: 12/9
    print(s.area())  # Output: 144
    print(s.perimeter())  # Output: This is not a square. Use separate calculations for rectangles.
