#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/3
"""
import itertools
import re

import aoc

PUZZLE = aoc.Puzzle(day=3, year=2023)
NUMBERS = re.compile(r"\d+")
SYMBOLS = "!@#$%^&*/=-+"


def ispart(schematic, endpos, row, span):
    """Look for symbols near the number"""
    rows = range(max(0, row-1), min(endpos[0], row+1)+1)
    cols = range(max(0, span[0]-1), min(endpos[1], span[1])+1)
    # print(span, rows, cols)
    for row_, col_ in itertools.product(rows, cols):
        if schematic[row_][col_] in SYMBOLS:
            return True
    return False


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        pass
    schematic = PUZZLE.input.splitlines()
    endpos = (len(schematic)-1, len(schematic[0])-1)
    total = 0
    for row, line in enumerate(schematic):
        for match in NUMBERS.finditer(line):
            if ispart(schematic, endpos, row, match.span()):
                total += int(match.group(0))
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
