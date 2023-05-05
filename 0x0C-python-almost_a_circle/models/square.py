#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square.
        Args:
            size (int): The size of the Square.
            x (in): horizontal position of Square.
            y (int): vertical position of Square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the of size Square """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the value of size """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """Return string representation of Sqaure"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the Square
        Args:
            *args: list of arguments to update Square with
            **kwargs: Keyword arguments to update Square with
        """
        attr = [self.id, self.width, self.x, self.y]

        if len(args) == 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    if type(kwargs[key]) != int:
                        raise TypeError("width" + self.int_err)
                    elif kwargs[key] <= 0:
                        raise ValueError("width must be > 0")
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    if type(kwargs[key]) != int:
                        raise TypeError("x" + self.int_err)
                    elif kwargs[key] < 0:
                        raise ValueError("x must be >= 0")
                    self.x = kwargs[key]
                elif key == "y":
                    if type(kwargs[key]) != int:
                        raise TypeError("y" + self.int_err)
                    elif kwargs[key] < 0:
                        raise ValueError("y must be > 0")
                    self.y = kwargs[key]
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    if type(args[i]) != int:
                        raise TypeError("width" + self.int_err)
                    elif args[i] <= 0:
                        raise ValueError("width must be > 0")
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    if type(args[i]) != int:
                        raise TypeError("x" + self.int_err)
                    elif args[i] < 0:
                        raise ValueError("x must be >= 0")
                    self.x = args[i]
                elif i == 3:
                    if type(args[i]) != int:
                        raise TypeError("y" + self.int_err)
                    elif args[i] < 0:
                        raise ValueError("y must be >= 0")
                    self.y = args[i]

    def to_dictionary(self):
        """Return dictionary representation of Square"""

        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
