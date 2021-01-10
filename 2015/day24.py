#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/24
"""
from itertools import combinations
import math
import aoc

PUZZLE = aoc.Puzzle(day=24, year=2015)


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        groups = 3
    else:
        groups = 4
    presents = [int(x) for x in PUZZLE.input.splitlines()]
    target = sum(presents) // groups
    for count in range(2, len(presents)-groups):
        fronts = [x for x in combinations(presents, count) if sum(x) == target]
        if fronts:
            return min([math.prod(x) for x in fronts])
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
