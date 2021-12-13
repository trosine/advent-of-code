#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/20
"""
import collections

import aoc

PUZZLE = aoc.Puzzle(day=20, year=2016)

Range = collections.namedtuple('Range', ('start', 'end'))


def solve(part='a'):
    """Solve puzzle"""
    rules = [
        Range(*map(int, line.split('-')))
        for line in PUZZLE.input.splitlines()
        ]
    rules.sort()
    candidate = 0
    allowed = 0
    while rules:
        rule = rules.pop(0)
        if candidate < rule.start:
            if part == 'a':
                return candidate
            allowed += rule.start - candidate
        candidate = max(candidate, rule.end + 1)
    if candidate < 2**32 - 1:
        allowed += 2**32 - candidate
    return allowed


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
