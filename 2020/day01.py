#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/1
"""
import itertools
import functools
import operator
import aoc

PUZZLE = aoc.Puzzle(day=1, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    # print(PUZZLE.input)
    count = 2
    if part == 'b':
        count = 3
    content = map(int, PUZZLE.input.splitlines())
    for numbers in itertools.combinations(content, count):
        if sum(numbers) == 2020:
            return functools.reduce(operator.mul, numbers)
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
