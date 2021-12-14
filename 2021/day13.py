#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/13
"""
from collections import defaultdict
from itertools import product

import aoc

PUZZLE = aoc.Puzzle(day=13, year=2021)


def fold(grid, bottom_right, kind, crease):
    """Fold the code"""
    if kind[-1] == 'x':
        variant = 0
        step = -1
    else:
        variant = 1
        step = 1
    static_range = range(bottom_right[1 - variant] + 1)
    offset_range = range(1, crease + 1)
    # print(f'x={static_range}, y={offset_range}')
    for pos, offset in product(static_range, offset_range):
        source = (pos, crease + offset)[::step]
        dest = (pos, crease - offset)[::step]
        # print(f'{source} -> {dest}')
        grid[dest] = max(grid[source], grid[dest])
        del grid[source]
    bottom_right[variant] = crease - 1


def solve(part='a'):
    """Solve puzzle"""
    grid = defaultdict(int)
    dots, folds = PUZZLE.input.split('\n\n')
    bottom_right = (0, 0)
    for dot in dots.splitlines():
        pos = tuple(map(int, dot.split(',')))
        bottom_right = list(map(max, bottom_right, pos))
        grid[pos] = 1
    print(bottom_right)
    for instruction in folds.splitlines():
        kind, crease = instruction.split('=')
        fold(grid, bottom_right, kind[-1], int(crease))
        if part == 'a':
            return sum(grid.values())
    for row in range(bottom_right[1] + 1):
        for col in range(bottom_right[0] + 1):
            char = '#' if grid[(col, row)] else ' '
            print(char, end='')
        print()
    print()
    return input('Type in the code you see above: ').upper()


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
