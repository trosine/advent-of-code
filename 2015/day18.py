#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/18
"""
import collections
import operator
from itertools import product
import aoc

PUZZLE = aoc.Puzzle(day=18, year=2015)
NEIGHBORS = tuple(x for x in product(range(-1, 2), repeat=2) if x != (0, 0))


def solve(part='a'):
    """Solve puzzle"""
    always_on = []
    if part == 'b':
        always_on = list(product((0, 99), repeat=2))
    current = collections.defaultdict(bool)
    for row, lights in enumerate(PUZZLE.input.splitlines()):
        for col, light in enumerate(lights):
            current[(row, col)] = light == '#'
    for pos in always_on:
        current[pos] = True

    for _ in range(100):
        new = collections.defaultdict(bool)
        for pos in product(range(100), repeat=2):
            count = 0
            for direction in NEIGHBORS:
                count += current[tuple(map(operator.add, pos, direction))]
            if pos in always_on:
                new[pos] = True
            elif current[pos]:
                new[pos] = count in (2, 3)
            else:
                new[pos] = count == 3
        current = new
    return sum(current.values())


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
