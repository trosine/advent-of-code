#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/16
"""
from collections import deque
from itertools import product
from point import Point2D
import aoc

PUZZLE = aoc.Puzzle(day=16, year=2023)


class Point(Point2D):
    """Enhanced Point class with named directions"""
    named_dirs = {
        "u": Point2D(-1, 0),
        "d": Point2D(1, 0),
        "r": Point2D(0, 1),
        "l": Point2D(0, -1),
    }


class Space:
    """Defines what is present at a given location"""

    _source_translation = {
        "l": "r",
        "r": "l",
        "u": "d",
        "d": "u",
    }
    _translations = {
        "\\": {
                "l": "d",
                "r": "u",
                "u": "r",
                "d": "l",
        },
        "/": {
                "l": "u",
                "r": "d",
                "u": "l",
                "d": "r",
        },
        "|": {
                "l": "ud",
                "r": "ud",
                "u": "d",
                "d": "u",
        },
        "-": {
                "l": "r",
                "r": "l",
                "u": "lr",
                "d": "lr",
        },
        ".": {
                "l": "r",
                "r": "l",
                "u": "d",
                "d": "u",
        },
    }

    def __init__(self, char):
        self.char = char
        self.light_sources = set()

    @property
    def energized(self):
        """Determine if this space is energized or not"""
        return bool(self.light_sources)

    @classmethod
    def to_source(cls, dest):
        """Converts an output direction to a source direction"""
        return cls._source_translation[dest]

    def travel(self, source):
        """Generate (dest, direction) tuples for light entering from source"""
        self.light_sources.add(source)
        for dest in self._translations[self.char][source]:
            yield dest, Point.named_dirs[dest]


def count_energized(grid, grid_max, pos, source):
    """Count the number of energized spaces"""
    energized = set()
    queue = deque()
    queue.append((pos, source))
    while queue:
        current, source = queue.pop()
        space = grid[current]
        if source in space.light_sources:
            continue  # already seen
        energized.add(current)
        for dir_name, direction in space.travel(source):
            new_pos = current + direction
            if 0 <= new_pos.x <= grid_max.x and 0 <= new_pos.y <= grid_max.y:
                queue.append((new_pos, space.to_source(dir_name)))
    value = len(energized)
    # reset the grid
    for current in energized:
        grid[current].light_sources.clear()
    return value


def solve(part="a"):
    """Solve puzzle"""
    grid = {}
    row = None
    col = None
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, char in enumerate(line):
            grid[Point(row, col)] = Space(char)
    grid_max = Point(row, col)

    best = 0
    starts = [
        ("l", range(grid_max.x+1), [0]),
        ("r", range(grid_max.x+1), [grid_max.y]),
        ("u", [0],                 range(grid_max.y+1)),
        ("d", [grid_max.x],        range(grid_max.y+1)),
    ]
    if part == "a":
        starts = [("l", [0], [0])]

    for source, rows, cols in starts:
        for pos in product(rows, cols):
            count = count_energized(grid, grid_max, Point(*pos), source)
            best = max(best, count)
    return best


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
