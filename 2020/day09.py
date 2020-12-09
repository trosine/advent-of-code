#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/9
"""
import itertools
import aoc

PUZZLE = aoc.Puzzle(day=9, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    invalid = None
    data = list(map(int, PUZZLE.input.splitlines()))
    for index, number in enumerate(data[25:]):
        preamble = data[index:index+25]
        for pair in itertools.combinations(preamble, 2):
            if sum(pair) == number:
                break
        else:
            invalid = number
            break
    if part == 'a':
        return invalid

    start = 0
    while start < len(data):
        total = 0
        for offset in range(start, len(data)):
            total += data[offset]
            if total == invalid:
                group = data[start:offset+1]
                return min(group) + max(group)
        start += 1

    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
