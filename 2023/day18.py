#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/18
"""
from collections import defaultdict, deque
from point import Point2D, direction_cardinals
import aoc

PUZZLE = aoc.Puzzle(day=18, year=2023)


def solve(part="a"):
    """Solve puzzle"""
    if part == "b":
        return None
    grid = defaultdict(str)
    current = Point2D(0, 0)
    # dig out the trench
    for line in PUZZLE.input.splitlines():
        dest, count, color = line.split()
        count = int(count)
        for _ in range(count):
            current += direction_cardinals[dest]
            grid[current] = color
    # dig out the center
    current = min(grid) + (1, 1)
    queue = deque()
    queue.append(current)
    while queue:
        current = queue.pop()
        grid[current] = ""
        for neighbor in current.neighbors(current.cardinals):
            if neighbor not in grid:
                queue.append(neighbor)
    return len(grid)


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
