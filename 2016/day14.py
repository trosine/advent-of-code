#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/14
"""
import functools
import hashlib
import re

import aoc

PUZZLE = aoc.Puzzle(day=14, year=2016)
TRIPLE = re.compile(r'(\w)\1\1')


@functools.cache
def md5_hex(data, stretch=0):
    """Return the stretched md5 digest of data"""
    for _ in range(stretch+1):
        data = hashlib.md5(data.encode()).hexdigest()
    return data


def solve(part='a'):
    """Solve puzzle"""
    stretch = 0 if part == 'a' else 2016
    salt = PUZZLE.input
    index = 0
    keys = 0
    while keys < 64:
        hexdigest = md5_hex(salt + str(index), stretch)
        if match := TRIPLE.search(hexdigest):
            look_for = match.group(1) * 5
            for subindex in range(index+1, index+1001):
                hexdigest = md5_hex(salt + str(subindex), stretch)
                if look_for in hexdigest:
                    keys += 1
                    break
        index += 1
    return index-1


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
