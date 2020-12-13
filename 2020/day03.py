#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/3

How many trees (`#`) will you hit going from the first line, to the last.
The pattern repeats along the right.
"""
import aoc

PUZZLE = aoc.Puzzle(day=3, year=2020)


def hits(lines, right=3, down=1):
    """Find the number of trees hit given a specific slope"""
    hit = 0
    position = 0
    chars = len(lines[0])
    line = 0
    while line < len(lines):
        if lines[line][position] == '#':
            hit += 1
        position = (position + right) % chars
        line += down
    return hit


def solve(part='a'):
    """Find the number of trees hit while sledding"""
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
        ]
    if part == 'a':
        slopes = [slopes[1]]
    lines = PUZZLE.input.splitlines()
    product = 1
    for right, down in slopes:
        product = product * hits(lines, right, down)
    return product


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
