# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if type(width) is not int or type(height) is not int:
            raise TypeError("Width and height must be integers")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    def is_square(self):
        """
        Returns True if the rectangle is a square.
        """
        return self.width == self.height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
