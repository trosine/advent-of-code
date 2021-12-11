#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/11
"""
from collections import deque
from itertools import product, count
import operator

import aoc

PUZZLE = aoc.Puzzle(day=11, year=2021)
NEIGHBORS = tuple(x for x in product(range(-1, 2), repeat=2) if x != (0, 0))


def neighbors(pos):
    """Iterate over all valid neighbors"""
    for direction in NEIGHBORS:
        row, col = map(operator.add, pos, direction)
        if 0 <= row < 10 and 0 <= col < 10:
            yield row, col


def solve(part='a'):
    """Solve puzzle"""
    grid = {}
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, energy in enumerate(line):
            grid[(row, col)] = int(energy)
    flashes = 0
    for step in count():
        new_flashes = set()
        for pos in grid:
            grid[pos] += 1
            if grid[pos] == 10:
                new_flashes.add(pos)
        queue = deque(new_flashes)
        while queue:
            pos = queue.pop()
            for neighbor in neighbors(pos):
                grid[neighbor] += 1
                if grid[neighbor] == 10:
                    new_flashes.add(neighbor)
                    queue.append(neighbor)
        for pos in new_flashes:
            grid[pos] = 0
        flashes += len(new_flashes)
        if part == 'a' and step >= 99:
            return flashes
        if part == 'b' and len(new_flashes) == 100:
            return step + 1
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
