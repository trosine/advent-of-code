#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/22
"""
import itertools
import re

import aoc

PUZZLE = aoc.Puzzle(day=22, year=2021)
INTEGERS = re.compile(r'-?\d+')


def solve(part='a'):
    """Solve puzzle"""
    enabled = set()
    for rule in PUZZLE.input.splitlines():
        coords = list(map(int, INTEGERS.findall(rule)))
        for maxval in (1, 3, 5):
            coords[maxval] += 1
        x_range = range(*coords[0:2])
        y_range = range(*coords[2:4])
        z_range = range(*coords[4:6])
        if part == 'a':
            if x_range.start > 50 or x_range.stop < -50:
                continue
            if y_range.start > 50 or y_range.stop < -50:
                continue
            if z_range.start > 50 or z_range.stop < -50:
                continue
        cubes = itertools.product(x_range, y_range, z_range)
        if rule.startswith('on'):
            method = enabled.add
        else:
            method = enabled.discard
        for cube in cubes:
            method(cube)
    return len(enabled)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
