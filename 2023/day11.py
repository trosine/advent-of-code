#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/11
"""
from itertools import combinations
from point import Point2D
import aoc

PUZZLE = aoc.Puzzle(day=11, year=2023)


def expansions(start, end, to_expand, expansion):
    """Calculate how much space is added due to expansion"""
    distance = 0
    big = max(start, end)
    small = min(start, end)
    for row in to_expand:
        if small < row < big:
            distance += expansion
    return distance


def solve(part='a'):
    """Solve puzzle"""
    # note, in part a, we're replacing 1 row with 2 (adding 1)
    # in part b, we're replacing 1 row with 1 million
    expansion = 2-1
    if part == 'b':
        expansion = 1_000_000-1
    data = PUZZLE.input.splitlines()
    galaxies = []
    rows_to_expand = set(range(len(data)))
    cols_to_expand = set(range(len(data[0])))
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "#":
                galaxies.append(Point2D(row, col))
                rows_to_expand.discard(row)
                cols_to_expand.discard(col)

    total = 0
    for source, dest in combinations(galaxies, 2):
        distance = source.distance(dest)
        distance += expansions(source.x, dest.x, rows_to_expand, expansion)
        distance += expansions(source.y, dest.y, cols_to_expand, expansion)
        total += distance
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
