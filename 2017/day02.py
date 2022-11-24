#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/2
"""
from itertools import permutations

import aoc

PUZZLE = aoc.Puzzle(day=2, year=2017)


def divisible(values):
    """Find the evenly divisable pair of numbers and divide them"""
    values = sorted(values, reverse=True)
    for num, div in permutations(values, 2):
        if num % div == 0:
            return num // div
    return None


def max_minus_min(values):
    """Find the difference between the max and min items"""
    return max(values) - min(values)


def solve(part='a'):
    """Solve puzzle"""
    func = max_minus_min
    if part == 'b':
        func = divisible
    data = PUZZLE.input.splitlines()
    total = 0
    for line in data:
        values = list(map(int, line.split()))
        total += func(values)
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
