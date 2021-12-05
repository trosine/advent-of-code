#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/5
"""
from collections import defaultdict
import re

import aoc

PUZZLE = aoc.Puzzle(day=5, year=2021)
LINE = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')


def get_step(x_1, x_2):
    """Get the step value for a values along an axis"""
    if x_1 == x_2:
        return 0
    # return (x_2 - x_1) // abs(x_2 - x_1)
    if x_1 > x_2:
        return -1
    return 1


def solve(part='a'):
    """Solve puzzle"""
    field = defaultdict(int)
    for line in PUZZLE.input.splitlines():
        x_1, y_1, x_2, y_2 = map(int, LINE.match(line).groups())
        if part == 'a':
            if x_1 != x_2 and y_1 != y_2:
                # ignore diagonal lines
                continue
        x_step = get_step(x_1, x_2)
        y_step = get_step(y_1, y_2)
        while True:
            x_1 += x_step
            y_1 += y_step
            field[(x_1, y_1)] += 1
            if x_1 == x_2 and y_1 == y_2:
                break
    total = 0
    for count in field.values():
        if count > 1:
            total += 1
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
