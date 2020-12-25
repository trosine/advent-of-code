#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/8
"""
import ast
import aoc

PUZZLE = aoc.Puzzle(day=8, year=2015)


def solve(part='a'):
    """Solve puzzle"""
    result_a = 0
    result_b = 0
    for line in PUZZLE.input.splitlines():
        result_a += len(line) - len(ast.literal_eval(line))
        # the new surrounding quotes, plus backslashes to escape \ or "
        result_b += 2 + line.count('"') + line.count('\\')
    if part == 'a':
        return result_a
    return result_b


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
