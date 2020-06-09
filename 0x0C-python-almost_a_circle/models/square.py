#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):

        def __init__(self, size, x=0, y=0, id=None):

                super().__init__(size, size, x, y, id)
                self.__size = size

        def __str__(self):

                return ("[Square] ({}) {}/{} - {}".format(
                        self.id, self.x, self.y, self.__size))

        @property
        def size(self):
                return self.__size

        @size.setter
        def size(self, value):
                if type(value) is not int:
                        raise TypeError("width must be an integer")
                elif value <= 0:
                        raise ValueError("width must be > 0")
                else:
                        self.__size = value

        def update(self, *parameter, **kwargs):
                if len(parameter) > 0:
                        self.id = parameter[0]
                if len(parameter) > 1:
                        self.size = parameter[1]
                if len(parameter) > 2:
                        self.x = parameter[2]
                if len(parameter) > 3:
                        self.y = parameter[3]
                if parameter is None or len(parameter) == 0:
                        for key, value in kwargs.items():
                                if key == "size":
                                        self.size = value
                                elif key == "x":
                                        self.x = value
                                elif key == "y":
                                        self.y = value
                                elif key == "id":
                                        self.id = value

        def to_dictionary(self):

                return {'id': self.id,
                        'size': self.__size,
                        'x': self.x,
                        'y': self.y
                        }
