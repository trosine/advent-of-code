#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/1
"""
import aoc

PUZZLE = aoc.Puzzle(day=1, year=2022)


def solve(part='a'):
    """Solve puzzle"""
    top = 1
    if part == 'b':
        top = 3
    elves = []
    for elf in PUZZLE.input.split('\n\n'):
        elves.append(sum(map(int, elf.splitlines())))
    elves.sort()
    return sum(elves[-top:])


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
