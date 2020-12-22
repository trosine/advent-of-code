#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/2
"""
from itertools import combinations, starmap
import functools
import operator
import aoc

PUZZLE = aoc.Puzzle(day=2, year=2015)


def solve(part='a'):
    """Solve puzzle"""
    paper = 0
    ribbon = 0
    for box in PUZZLE.input.splitlines():
        dimensions = tuple(map(int, box.split('x')))
        areas = tuple(starmap(operator.mul, combinations(dimensions, 2)))
        paper += sum(2 * areas) + min(areas)
        ribbon += 2 * (sum(dimensions) - max(dimensions))
        ribbon += functools.reduce(operator.mul, dimensions)  # the bow
    if part == 'a':
        return paper
    return ribbon


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
