#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/25
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=25, year=2015)


def solve(part='a'):
    """Solve puzzle"""
    del part
    row, col = [int(x) for x in re.findall(r'\d+', PUZZLE.input)]
    base = row + col - 2  # full diagonals to run
    iterations = base * (base + 1) // 2  # sum(1..n)
    iterations += col  # partial diagonal
    code = 20151125
    for _ in range(1, iterations):
        code = (code * 252533) % 33554393
    return code


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
