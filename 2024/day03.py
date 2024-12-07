#!/usr/bin/env python3
"""
https://adventofcode.com/2024/day/3
"""
import operator
import re

import aoc

PUZZLE = aoc.Puzzle(day=3, year=2024)


def solve(part="a"):
    """Solve puzzle"""
    enabled = 1
    mul = re.compile(r"(mul)\(([0-9]{1,3}),([0-9]{1,3})\)")
    if part == "b":
        mul = re.compile(
            r"(?:"
            r"(do|don't)\(\)"
            "|"
            + mul.pattern +
            ")"
        )

    total = 0
    for instruction in mul.finditer(PUZZLE.input):
        groups = instruction.groups()
        if groups[0] == "do":
            enabled = 1
        elif groups[0] == "don't":
            enabled = 0
        else:
            total += enabled * operator.mul(*map(int, groups[-2:]))
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
