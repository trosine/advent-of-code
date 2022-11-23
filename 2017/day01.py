#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/1
"""
import aoc

PUZZLE = aoc.Puzzle(day=1, year=2017)


def solve(part='a'):
    """Solve puzzle"""
    data = PUZZLE.input
    if part == 'a':
        shift = -1
    else:
        shift = -len(data)//2
    captcha = 0
    for offset, char in enumerate(data):
        if data[offset+shift] == char:
            captcha += int(char)
    return captcha


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
