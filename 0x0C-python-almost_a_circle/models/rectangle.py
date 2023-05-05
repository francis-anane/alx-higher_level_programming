#!/usr/bin/python3

"""rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
            x (int): rectangle point x
            y (int): rectangle point y
            id (int): Rectangle objectq id
        """

        self.__int_err = " must be an integer"  # int requirement err msg
        if type(width) != int:
            raise TypeError("width" + self.__int_err)
        elif type(height) != int:
            raise TypeError("height" + self.__int_err)
        elif type(x) != int:
            raise TypeError("x" + self.__int_err)
        elif type(y) != int:
            raise TypeError("y" + self.__int_err)
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Return width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""

        if type(value) != int:
            raise TypeError("width" + self.__int_err)
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Return height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""

        if type(value) != int:
            raise TypeError("height" + self.__int_err)
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Return x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""

        if type(value) != int:
            raise TypeError("x" + self.__int_err)
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Return y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets x"""

        if type(value) != int:
            raise TypeError("y" + self.__int_err)
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Return area of Rectangle """

        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle to stdout"""
        h = self.__height
        x_symbol = ""
        y_symbol = ""
        if self.__x > 0:
            x_symbol = " " * self.__x
        if self.__y > 0:
            y_symbol = "\n" * self.__y
        print(y_symbol, end="")
        while h > 0:
            print(x_symbol + "#" * self.__width)
            h -= 1

    @property
    def int_err(self):
        """Return int_err string"""

        return self.__int_err

    def __str__(self):
        """Return string representation of Rectangle"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update the Rectangle
        Args:
            *args: list of arguments to update Rectangle with
        """
        attr = [self.id, self.__width, self.__height, self.__x, self.__y]

        if len(args) == 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    if type(kwargs[key]) != int:
                        raise TypeError("width" + self.__int_err)
                    elif kwargs[key] <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = kwargs[key]
                elif key == "height":
                    if type(kwargs[key]) != int:
                        raise TypeError("height" + self.__int_err)
                    elif kwargs[key] <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = kwargs[key]
                elif key == "x":
                    if type(kwargs[key]) != int:
                        raise TypeError("x" + self.__int_err)
                    elif kwargs[key] < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = kwargs[key]
                elif key == "y":
                    if type(kwargs[key]) != int:
                        raise TypeError("y" + self.__int_err)
                    elif kwargs[key] < 0:
                        raise ValueError("y must be > 0")
                    self.__y = kwargs[key]
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    if type(args[i]) != int:
                        raise TypeError("width" + self.__int_err)
                    elif args[i] <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = args[i]
                elif i == 2:
                    if type(args[i]) != int:
                        raise TypeError("height" + self.__int_err)
                    elif args[i] <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = args[i]
                elif i == 3:
                    if type(args[i]) != int:
                        raise TypeError("x" + self.__int_err)
                    elif args[i] < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = args[i]
                elif i == 4:
                    if type(args[i]) != int:
                        raise TypeError("y" + self.__int_err)
                    elif args[i] < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = args[i]

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""

        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
