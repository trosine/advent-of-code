#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/9
"""
from collections import namedtuple
from operator import add, sub

import aoc

PUZZLE = aoc.Puzzle(day=9, year=2022)


class Point(namedtuple('Point', ('x', 'y'))):
    """A point class with overridden operators"""

    def __abs__(self):
        return Point(*map(abs, self))

    def __add__(self, right):
        return Point(*map(add, self, right))

    def __sub__(self, right):
        return Point(*map(sub, self, right))

    def __repr__(self):
        return '(' + ', '.join(map(str, self)) + ')'

    def unit(self):
        """Return a Point() with each attribute set to -1, 0 or 1"""
        elements = []
        for element in self:
            sign = 0
            if element > 0:
                sign = 1
            elif element < 0:
                sign = -1
            elements.append(sign)
        return Point(*elements)


HEAD_DIRS = {
    'U': Point(1, 0),
    'D': Point(-1, 0),
    'L': Point(0, -1),
    'R': Point(0, 1),
}


def solve(part='a'):
    """Solve puzzle"""
    count = 2
    if part == 'b':
        count = 10
    knots = [Point(0, 0)] * count
    visited = set(knots[-1:])
    for line in PUZZLE.input.splitlines():
        direction, count = line.split()
        for _ in range(int(count)):
            knots[0] = knots[0] + HEAD_DIRS[direction]
            previous = knots[0]
            for offset, knot in enumerate(knots[1:], 1):
                diff = previous - knot
                if diff.x in (-1, 0, 1) and diff.y in (-1, 0, 1):
                    # tail is still "touching" head
                    previous = knot
                    continue
                knot = knot + diff.unit()
                knots[offset] = knot
                previous = knot
            visited.add(knots[-1])
    return len(visited)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
