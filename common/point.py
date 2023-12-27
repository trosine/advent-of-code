"""Coordinate system point management"""

from collections import namedtuple
from operator import add, sub, mul


class PointFunctions(tuple):
    """Functions that can be mixed in to handle management of coordinates"""

    def __abs__(self):
        return type(self)(*map(abs, self))

    def __add__(self, right):
        return type(self)(*map(add, self, right))

    def __mul__(self, right):
        if isinstance(right, int):
            return type(self)(*(x * right for x in self))
        if isinstance(right, (tuple, list)):
            return type(self)(*map(mul, self, right))
        assert False, "Right hand operand of * must either be int or tuple"

    def __sub__(self, right):
        return type(self)(*map(sub, self, right))

    def distance(self, other):
        """Return the manhattan distance to the other point"""
        return sum(abs(self-other))

    # def __repr__(self):
    #     return repr(tuple(self))

    def unit(self):
        """Return a Point() with each axis normalized to -1, 0 or 1"""
        elements = []
        for element in self:  # pylint: disable=not-an-iterable
            sign = 0
            if element > 0:
                sign = 1
            elif element < 0:
                sign = -1
            elements.append(sign)
        return type(self)(*elements)


class Point2D(PointFunctions, namedtuple("Point2D", ["x", "y"])):
    """A 2D Coordinate Point"""
    cardinals = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]
    diagonals = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    def neighbors(self, directions):
        """Yield neighboring points by adding each direction to self"""
        for direction in directions:
            yield self + direction


class Point3D(PointFunctions, namedtuple("Point3D", ["x", "y", "z"])):
    """A 3-Dimentional point"""


direction_cardinals = {
    "UDLR"[i]: Point2D(*d)
    for i, d in enumerate(Point2D.cardinals)
}
