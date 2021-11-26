#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/3
"""
import aoc

PUZZLE = aoc.Puzzle(day=3, year=2016)


def parser_a():
    """Parse input via the rules for part a"""
    for spec in PUZZLE.input.splitlines():
        yield map(int, spec.split())


def parser_b():
    """Parse input via the rules for part a"""
    lines = PUZZLE.input.splitlines()
    while lines:
        # read 3 lines
        group = [lines.pop().split() for row in range(3)]
        # yield the columns instead of rows
        for column in range(3):
            yield [int(row[column]) for row in group]


def solve(part='a'):
    """Solve puzzle"""
    parser = parser_a
    if part == 'b':
        parser = parser_b
    possible = 0
    for triangle in parser():
        sides = sorted(triangle)
        if sides[0] + sides[1] > sides[2]:
            possible += 1
    return possible


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
