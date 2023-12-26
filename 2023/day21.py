#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/21
"""
from collections import deque
from itertools import product
from point import Point2D
import aoc

PUZZLE = aoc.Puzzle(day=21, year=2023)


def print_grid(grid):
    """Print the grid back out"""
    last_point = max(grid)
    row_range = range(last_point.x + 1)
    col_range = range(last_point.y + 1)
    previous = 0
    for row, col in product(row_range, col_range):
        if row != previous:
            print()
        print(grid[(row, col)], end="")
        previous = row
    print()


def load_grid():
    """Load the map from the input"""
    grid = {}
    start = None
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, char in enumerate(line):
            pos = Point2D(row, col)
            if char == "S":
                char = "."
                start = pos
            grid[pos] = char
    return grid, start


def solve(part="a"):
    """Solve puzzle"""
    max_steps = 64
    if part == "b":
        return None
    grid, start = load_grid()

    print(start)
    seen = {}
    queue = deque()
    queue.append((start, 0))
    while queue:
        pos, distance = queue.popleft()
        if distance >= max_steps:
            continue
        for neighbor in pos.neighbors(Point2D.cardinals):
            if neighbor not in grid:
                continue
            if grid[neighbor] == "#" or neighbor in seen:
                continue
            seen[neighbor] = distance + 1
            queue.append((neighbor, distance + 1))
    total = 0
    for distance in seen.values():
        if distance % 2 == 0:
            total += 1
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
