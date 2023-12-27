"""A common way to handle shapes"""


class Linear:
    """Base functions for handling linear shapes like rectangles, cubes, etc"""

    def __init__(self, start, end):
        # normalize so the end is always > start
        normal_start = []
        normal_end = []
        axes = range(len(start))
        for axis in axes:
            normal_start.append(min(start[axis], end[axis]))
            normal_end.append(max(start[axis], end[axis]))

        self.start = type(start)(*normal_start)
        self.end = type(start)(*normal_end)

    def __str__(self):
        return f"Linear({self.start}, {self.end})"

    def __repr__(self):
        return str(self)

    def overlaps(self, other, axes=None):
        """Determine if these two shapes overlap"""
        if axes is None:
            axes = range(len(self.start))
        for axis in axes:
            if other.start[axis] > self.end[axis]:
                return False
            if other.end[axis] < self.start[axis]:
                return False
        return True

    def intersection(self, other):
        """Find the intersection of these two objects"""
        if not self.overlaps(other):
            return None
        return None
