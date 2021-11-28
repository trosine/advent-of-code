#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/6
"""
from collections import defaultdict
from operator import itemgetter

import aoc

PUZZLE = aoc.Puzzle(day=6, year=2016)


def solve(part='a'):
    """Solve puzzle"""
    letters = []
    data = PUZZLE.input.splitlines()
    for letter in range(len(data[0])):
        letters.append(defaultdict(int))
    for line in data:
        for pos, letter in enumerate(line):
            letters[pos][letter] += 1

    picker = max if part == 'a' else min
    message = ''
    for letter in letters:
        message += picker(letter.items(), key=itemgetter(1))[0]
    return message


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
