#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/17
"""
from itertools import combinations
import aoc

PUZZLE = aoc.Puzzle(day=17, year=2015)
TARGET = 150


def solve(part='a'):
    """Solve puzzle"""
    containers = list(map(int, PUZZLE.input.splitlines()))
    valid = []
    for count in range(1, len(containers)+1):
        for combo in combinations(containers, count):
            if sum(combo) == TARGET:
                valid.append(count)
    if part == 'a':
        return len(valid)
    return valid.count(min(valid))


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
