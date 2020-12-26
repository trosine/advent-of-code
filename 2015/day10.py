#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/10
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=10, year=2015)
PARSE = re.compile(r'((\d)\2*)')


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        turns = 40
    else:
        turns = 50
    value = PUZZLE.input
    for _ in range(turns):
        new_value = ''
        for length, match in PARSE.findall(value):
            new_value += str(len(length)) + match
        value = new_value
        # print(f'{turn} {value}')
    return len(value)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
