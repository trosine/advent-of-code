#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/10
"""
from point import Point2D
import aoc

PUZZLE = aoc.Puzzle(day=10, year=2023)
CONNECT = str.maketrans("nswe", "snew")
PIPES = {
    "|": "ns",
    "-": "ew",
    "L": "ne",
    "J": "nw",
    "7": "ws",
    "F": "se",
    "S": "nswe",
    ".": "",
}
DIRECTIONS = {
    "n": Point2D(-1, 0),
    "s": Point2D(1, 0),
    "w": Point2D(0, -1),
    "e": Point2D(0, 1),
}


def solve(part='a'):
    """Solve puzzle"""
    if part == 'b':
        return None
    grid = {}
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, char in enumerate(line):
            location = Point2D(row, col)
            grid[location] = PIPES.get(char)
            if char == "S":
                start = location

    dest = None
    # figure out which way to go around the loop
    # this assumes that only 2 pipes are pointing toward the start
    for name, direction in DIRECTIONS.items():
        source = name.translate(CONNECT)
        if source in grid[start + direction]:
            dest = start + direction
            break

    steps = 1
    while dest != start:
        name = grid[dest].replace(source, "")  # the direction we're now headed
        source = name.translate(CONNECT)
        dest += DIRECTIONS[name]
        steps += 1
    return steps // 2


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
