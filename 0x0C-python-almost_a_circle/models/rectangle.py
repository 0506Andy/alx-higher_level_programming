#!/usr/bin/python3
"""Defines rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent the rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle, a new rectangle.

        Args:
            width (int): Width of the new Rectangle.
            height (int): Height of the new Rectangle.
            x (int): x coordinate of the new Rectangle.
            y (int): y coordinate of the new Rectangle.
            id (int): Identity of the new Rectangle.
        Raises:
            TypeError: If either the Width or the Height of the rectangle is not an int.
            ValueError: If either of Width or Height of the rectangle  <= 0.
            TypeError: If either of x or y of the rectangle is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("the width must be an integer")
        if value <= 0:
            raise ValueError("the width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError(" the height must be an integer")
        if value <= 0:
            raise ValueError(" the height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("the x coordinate must be an integer")
        if value < 0:
            raise ValueError(" the x coordinate must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("the y coordinate  must be an integer")
        if value < 0:
            raise ValueError("the y coordinate must be >= 0")
        self.__y = value

    def area(self):
        """Return  area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute of the rectangle
                - 2nd argument represents width attribute of the rectangle
                - 3rd argument represent height attribute of the rectangle
                - 4th argument represents x attribute of the rectangle
                - 5th argument represents y attribute of the rectangle
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return  print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
