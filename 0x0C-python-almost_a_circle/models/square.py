#!/usr/bin/python3
"""
This square module has one class which inherit from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """initialized data"""
    def __init__(self, size, x=0, y=0, id=None):
        """add variables"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """return value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """change the value of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the values of variable"""
        if args and len(args) != 0:
            p = 0
            for arg in args:
                if p == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = arg
                elif p == 1:
                    self.width = arg
                    self.height = arg
                elif p == 2:
                    self.x = arg
                elif p == 3:
                    self.y = arg
                p += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = v
                elif k == 'size':
                    self.width = v
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """to dictionary"""
        return {
                    'id': self.id,
                    'size': self.width,
                    'x': self.x,
                    'y': self.y
                }
