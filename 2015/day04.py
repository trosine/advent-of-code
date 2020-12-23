#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/4
"""
import hashlib
import aoc

PUZZLE = aoc.Puzzle(day=4, year=2015)


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        zeros = '00000'
    else:
        zeros = '000000'
    salt = PUZZLE.input.strip()
    number = 0
    while True:
        digest = hashlib.md5(bytes(salt + str(number), 'utf-8')).hexdigest()
        if digest.startswith(zeros):
            break
        number += 1
    return number


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
