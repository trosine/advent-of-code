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


# using my original part a solution, I found that all numbers have either 0 or
# 1 symbols next to them, making it feasible to have the search for symbols be
# the outer loop. Using symbols as the outer loop makes it easier to use the
# same base logic for both parts.

# from my original solution for part a
def ispart(schematic, endpos, row, span):
    """Look for symbols near the number"""
    rows = range(max(0, row-1), min(endpos[0], row+1)+1)
    cols = range(max(0, span[0]-1), min(endpos[1], span[1])+1)
    # print(span, rows, cols)
    for row_, col_ in itertools.product(rows, cols):
        if schematic[row_][col_] in SYMBOLS:
            return True
    return False


def find_parts(numbers, endpos, row, col):
    """Find parts next to the symbol found"""
    rows = range(max(0, row-1), min(endpos[0], row+1)+1)
    parts = []
    for row_ in rows:
        for match in numbers[row_]:
            if (match.span()[0]-1) <= col < (match.span()[1]+1):
                parts.append(match)
    return parts


def solve(part="a"):
    """Solve puzzle"""
    if part == "a":
        symbols = SYMBOLS
    else:
        symbols = "*"
    symbols = re.compile("[" + re.escape(symbols) + "]")

    schematic = PUZZLE.input.splitlines()
    endpos = (len(schematic)-1, len(schematic[0])-1)
    total = 0
    ratio_total = 0
    numbers = [
        list(NUMBERS.finditer(row))
        for row in schematic
    ]

    for row, line in enumerate(schematic):
        for match in symbols.finditer(line):
            parts = find_parts(numbers, endpos, row, match.start())
            if len(parts) == 2:
                ratio_total += int(parts[0].group()) * int(parts[1].group())
            for part_match in parts:
                total += int(part_match.group())

    if part == "a":
        return total
    return ratio_total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
