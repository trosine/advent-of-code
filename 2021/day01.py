#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/1
"""
import aoc

PUZZLE = aoc.Puzzle(day=1, year=2021)


def solve(part='a'):
    """Solve puzzle"""
    window = 1 if part == 'a' else 3
    increases = 0
    data = list(map(int, PUZZLE.input.splitlines()))
    previous = data[:window]
    for depth in data[window:]:
        new_group = previous[1:]
        new_group.append(depth)
        if sum(new_group) > sum(previous):
            increases += 1
        previous = new_group
    return increases


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
