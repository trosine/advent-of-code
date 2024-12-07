#!/usr/bin/env python3
"""
https://adventofcode.com/2024/day/2
"""
import itertools

import aoc

PUZZLE = aoc.Puzzle(day=2, year=2024)


def verify(report):
    """Determine if a report is safe or unsafe"""
    ordered = sorted(report)
    if report not in (ordered, ordered[::-1]):
        # neither increasing or decreasing
        return False
    for left, right in itertools.pairwise(report):
        if abs(left - right) not in range(1, 4):
            return False
    return True


def remove_and_verify(report):
    """Determine if a report is safe, when a single value is removed"""
    if verify(report):
        return True
    for offset in range(len(report)):
        if verify(report[:offset] + report[offset+1:]):
            return True
    return False


def solve(part="a"):
    """Solve puzzle"""
    validator = verify
    if part == "b":
        validator = remove_and_verify
    total = 0
    for line in PUZZLE.input.splitlines():
        report = list(map(int, line.split()))
        valid = validator(report)
        # print(valid, report)
        total += valid
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
