#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/18
"""
import aoc

PUZZLE = aoc.Puzzle(day=18, year=2016)


def solve(part='a'):
    """Solve puzzle"""
    rows = 40 if part == 'a' else 400000
    prev = PUZZLE.input
    tiles_per_row = len(prev)
    safe_tiles = prev.count('.')
    for _ in range(1, rows):
        new_row = '^' if prev[1] == '^' else '.'
        for offset in range(1, tiles_per_row-1):
            new_row += '^' if prev[offset-1] != prev[offset+1] else '.'
        new_row += '^' if prev[-2] == '^' else '.'
        safe_tiles += new_row.count('.')
        prev = new_row
    return safe_tiles


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
