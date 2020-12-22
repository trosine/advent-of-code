#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/1
"""
import aoc

PUZZLE = aoc.Puzzle(day=1, year=2015)


def solve(part='a'):
    """Solve puzzle"""
    data = PUZZLE.input.strip()
    if part == 'a':
        return data.count('(') - data.count(')')
    floor = 0
    for index, char in enumerate(data):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return index + 1

    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
