#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/5
"""
import aoc

PUZZLE = aoc.Puzzle(day=5, year=2017)


def adjust_a(value):
    """Adjust the jump offset by 1"""
    return value + 1


def adjust_b(value):
    """Adjust the jump offset by 1 or -1"""
    if value >= 3:
        return value - 1
    return value + 1


def solve(part='a'):
    """Solve puzzle"""
    adjust = adjust_a
    if part == 'b':
        adjust = adjust_b
    steps = 0
    pos = 0
    program = list(map(int, PUZZLE.input.splitlines()))
    instructions = len(program)
    while 0 <= pos < instructions:
        offset = program[pos]
        program[pos] = adjust(offset)
        pos += offset
        steps += 1
    return steps


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
