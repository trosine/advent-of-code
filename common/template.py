#!/usr/bin/env python3
"""
https://adventofcode.com/YEAR/day/DAY
"""
import aoc

PUZZLE = aoc.Puzzle(day=DAY, year=YEAR)


def solve(part="a"):
    """Solve puzzle"""
    if part == "b":
        return None
    # print(PUZZLE.input)
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
