#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/1
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=1, year=2023)
WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
DIGITS = {str(d): str(d) for d in range(10)}
ALL = WORDS | DIGITS


def solve(part="a"):
    """Solve puzzle"""
    if part == "a":
        digit_map = DIGITS
    else:
        digit_map = ALL
    digit_re = re.compile("(" + "|".join(digit_map.keys()) + ")")
    lines = PUZZLE.input.splitlines()
    total = 0
    for line in lines:
        # digits = [c for c in line if c.isdigit()]  # original solution for A
        # digits = digit_re.findall(line)  # broken solution for B
        offset = 0
        digits = []
        while match := digit_re.search(line[offset:]):
            digits.append(match.group(1))
            offset += match.start(1) + 1
        calibration = int(ALL[digits[0]] + ALL[digits[-1]])
        total += calibration
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
