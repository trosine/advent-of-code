#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/8
"""
from itertools import product

import aoc

PUZZLE = aoc.Puzzle(day=8, year=2022)


def visible_trees(trees, height, row_range, col_range):
    """Calculate the number of visible trees in a single direction"""
    visible = 0
    for row, col in product(row_range, col_range):
        visible += 1
        if trees[row][col] >= height:
            break
    return visible


def solve_b():
    """Solve part b of the puzzle"""
    trees = PUZZLE.input.splitlines()
    rows = len(trees)
    cols = len(trees[0])
    best = 0
    for row, col in product(range(rows), range(cols)):
        height = trees[row][col]
        score = 1
        score *= visible_trees(trees, height, range(row-1, -1, -1), [col])
        score *= visible_trees(trees, height, range(row+1, rows), [col])
        score *= visible_trees(trees, height, [row], range(col-1, -1, -1))
        score *= visible_trees(trees, height, [row], range(col+1, cols))
        best = max(best, score)
    return best


def solve(part='a'):
    """Solve puzzle"""
    if part == 'b':
        return solve_b()
    total = 0
    trees = PUZZLE.input.splitlines()
    rows = len(trees)
    cols = len(trees[0])
    for row, col in product(range(rows), range(cols)):
        height = trees[row][col]
        north = all(
            trees[neighbor][col] < height
            for neighbor in range(row)
        )
        south = all(
            trees[neighbor][col] < height
            for neighbor in range(row+1, rows)
        )
        west = all(
            trees[row][neighbor] < height
            for neighbor in range(col)
        )
        east = all(
            trees[row][neighbor] < height
            for neighbor in range(col+1, cols)
        )
        total += any((north, south, west, east))
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
