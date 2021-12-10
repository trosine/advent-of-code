#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/10
"""
import statistics

import aoc

PUZZLE = aoc.Puzzle(day=10, year=2021)
ILLEGAL_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    }
INCOMPLETE_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
    }
EXPECTED = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
    }


def solve(part='a'):
    """Solve puzzle"""
    error_score = 0
    incompletes = []
    for line in PUZZLE.input.splitlines():
        expected = []
        illegal = None
        for char in line:
            if char in EXPECTED:
                expected.append(EXPECTED[char])
            elif char == expected[-1]:
                expected.pop()
            else:
                illegal = char
                break
        if illegal:
            error_score += ILLEGAL_SCORES[illegal]
        else:
            complete = 0
            for char in expected[::-1]:
                complete = complete * 5 + INCOMPLETE_SCORES[char]
            incompletes.append(complete)
    if part == 'a':
        return error_score
    return statistics.median(incompletes)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
