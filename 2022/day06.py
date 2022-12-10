#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/6
"""
import aoc

PUZZLE = aoc.Puzzle(day=6, year=2022)


def solve(part='a'):
    """Solve puzzle"""
    size = 4
    if part == 'b':
        size = 14
    buffer = PUZZLE.input
    for offset in range(0, len(buffer)-size):
        marker = set(buffer[offset:offset+size])
        if len(marker) == size:
            return offset + size
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
