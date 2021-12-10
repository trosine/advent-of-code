#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/9
"""
import collections
import operator

import aoc

PUZZLE = aoc.Puzzle(day=9, year=2021)
ADJACENT = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
    ]


def basin_size(start, grid):
    """Return the size of the basin"""
    queue = collections.deque([start])
    locations = set([start])

    while queue:
        current = queue.popleft()
        locations.add(current)

        for direction in ADJACENT:
            neighbor = tuple(map(operator.add, current, direction))
            if grid.get(neighbor, 10) >= 9:
                continue
            if neighbor not in locations:
                locations.add(neighbor)
                queue.append(neighbor)
    return len(locations)


def solve(part='a'):
    """Solve puzzle"""
    grid = {}
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, height in enumerate(line):
            grid[(row, col)] = int(height)
    risk = 0
    basins = []
    for coord, height in grid.items():
        for direction in ADJACENT:
            pos = tuple(map(operator.add, coord, direction))
            if grid.get(pos, 10) <= height:
                # not a low point, at least one neighbor is lower
                break
        else:
            risk += height + 1
            size = basin_size(coord, grid)
            # print(f'low point found at {coord} (h={height}, s={size})')
            basins.append(size)
    if part == 'a':
        return risk
    basins.sort(reverse=True)
    multiple = 1
    for basin in basins[:3]:
        multiple *= basin
    return multiple


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
