#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/12
"""
import json
import re
import aoc

PUZZLE = aoc.Puzzle(day=12, year=2015)
NUMBERS = re.compile(r'(-?\d+)')


def total_object(data, reject='red'):
    """Return the sum of all object values"""
    if isinstance(data, dict):
        data = data.values()
        if reject in data:
            return 0
    total = 0
    for value in data:
        if isinstance(value, int):
            total += value
        elif isinstance(value, str):
            pass
        else:
            total += total_object(value)
    return total


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        return sum(int(d) for d in NUMBERS.findall(PUZZLE.input))
    data = json.loads(PUZZLE.input)
    return total_object(data)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
