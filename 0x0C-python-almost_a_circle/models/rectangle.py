#!/usr/bin/python3
"""
This is rectangle module has one class Rectangle that inherit from Base
"""


from models.base import Base


class Rectangle(Base):
    """Initialized data"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Change the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """chnage the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """change the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """change the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """print in stdout the Rectangle instance with the char #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            print("{}{}".format(" " * self.x, '#' * self.width))

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update the value of the variables"""
        if args and len(args) != 0:
            p = 0
            for arg in args:
                if p == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif p == 1:
                    self.width = arg
                elif p == 2:
                    self.height = arg
                elif p == 3:
                    self.x = arg
                elif p == 4:
                    self.y = arg

                p += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """to dictionary"""
        return {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                }
