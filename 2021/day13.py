#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/13
"""
from collections import defaultdict

import aoc

PUZZLE = aoc.Puzzle(day=13, year=2021)


def fold(grid, axis, crease):
    """Fold the code"""
    if axis == 'x':
        variant = 0
    else:
        variant = 1
    to_merge = [
        pos
        for pos in grid.keys()
        if pos[variant] > crease
        ]
    for pos in to_merge:
        if pos[variant] > crease:
            dest = list(pos)
            dest[variant] = crease - (pos[variant] - crease)
            dest = tuple(dest)
            # print(f'fold along {axis}={crease}: {pos} => {dest}')
            grid[dest] = 1  # the only keys in the grid are "on"
            del grid[pos]


def solve(part='a'):
    """Solve puzzle"""
    grid = defaultdict(int)
    dots, folds = PUZZLE.input.split('\n\n')
    for dot in dots.splitlines():
        pos = tuple(map(int, dot.split(',')))
        grid[pos] = 1

    for instruction in folds.splitlines():
        axis, crease = instruction.split('=')
        fold(grid, axis[-1], int(crease))
        if part == 'a':
            return sum(grid.values())

    max_x, max_y = map(max, *grid.keys())
    for row in range(max_y + 1):
        line = ''
        for col in range(max_x + 1):
            line += '#' if grid[(col, row)] else ' '
        print(line)
    print()
    return input('Type in the code you see above: ').upper()


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
