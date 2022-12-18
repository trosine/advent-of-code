#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/12
"""
import math

from collections import namedtuple
from operator import add, sub

import aoc

PUZZLE = aoc.Puzzle(day=12, year=2022)


class PointFunctions:
    """Functions that can be mixed in to handle management of coordinates"""

    def __abs__(self):
        return type(self)(*map(abs, self))

    def __add__(self, right):
        # print(f"add({self}, {right})")
        return type(self)(*map(add, self, right))

    def __sub__(self, right):
        return type(self)(*map(sub, self, right))

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


def neighbors(pos, end):
    """Return a list of neighboring positions"""
    for direction in Point2D.cardinals:
        neighbor = pos + direction
        if 0 <= neighbor[0] <= end[0] and 0 <= neighbor[1] <= end[1]:
            yield neighbor


# https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
# modified: there's no need for edge relaxation
# all valid paths between nodes have weight=1, so
# there's also no need to return to a location we've already been to
# we've already taken the fastest (or equivalent) route to get there
def dijkstra(grid, start, end):
    """Find the shortest path cost from start to end"""
    shortest_paths = {start: 0}  # value is previous node, weight
    current_node = start
    last = max(grid.keys())

    while current_node != end:
        # bypass edge relaxation; all individual paths have weight=1
        current_height = grid.pop(current_node)
        current_weight = shortest_paths.pop(current_node)

        for neighbor in neighbors(current_node, last):
            if neighbor not in grid:
                # already visited; so this would be "more costly"
                continue
            if grid[neighbor] > current_height + 1:
                # too steep, cannot go this direction
                continue
            weight = current_weight + 1
            if neighbor not in shortest_paths:
                shortest_paths[neighbor] = weight

        # find the next node (with the shortest total path)
        next_neighbors = {
            node: weight
            for node, weight in shortest_paths.items()
            if node in grid
        }
        current_node = min(next_neighbors, key=lambda x: next_neighbors[x])

    return shortest_paths[end]


def solve(part='a'):
    """Solve puzzle"""
    start = None
    end = None
    grid = {}
    possible_starts = []
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, height in enumerate(line):
            pos = Point2D(row, col)
            if height == "S":
                start = pos
                height = "a"
            elif height == "E":
                end = pos
                height = "z"
            if height == "a":
                possible_starts.append(pos)
            grid[pos] = ord(height)
    if part == 'a':
        return dijkstra(grid, start, end)
    best = math.inf  # pylint: disable=c-extension-no-member
    for start in possible_starts:
        try:
            best = min(best, dijkstra(grid.copy(), start, end))
        except ValueError:
            pass
    return best


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
