#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/13
"""
# pylint: disable=c-extension-no-member
import collections
import math
import operator

import aoc

PUZZLE = aoc.Puzzle(day=13, year=2016)


def is_open(favorite, x, y):
    """Calculate if a coordinate is open space or a wall"""
    # pylint: disable=invalid-name
    if x < 0 or y < 0:
        return False
    number = x*x + 3*x + 2*x*y + y + y*y + favorite
    ones = filter(lambda x: x == '1', format(number, 'b'))
    return len(list(ones)) % 2 == 0


def neighbors(coord, favorite):
    """Find all valid neighbors of coord"""
    possible = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
        ]
    for direction in possible:
        neighbor = tuple(map(operator.add, coord, direction))
        if is_open(favorite, *neighbor):
            yield neighbor


# https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
def bfs_distance(start, end, favorite, depth=math.inf):
    """Calculate the shortest distance from start to end"""
    distance = {start: 0}
    queue = collections.deque([start])

    while queue:
        current = queue.popleft()
        if distance[current] >= depth:
            return distance[current], len(distance)

        for neighbor in neighbors(current, favorite):
            if neighbor == end:
                return distance[current] + 1, len(distance)
            if neighbor not in distance:
                queue.append(neighbor)
                distance[neighbor] = distance[current] + 1
    return -1


def solve(part='a'):
    """Solve puzzle"""
    depth = 50 if part == 'b' else math.inf
    favorite = int(PUZZLE.input)
    distance, visited = bfs_distance((1, 1), (31, 39), favorite, depth=depth)
    return distance if part == 'a' else visited


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
