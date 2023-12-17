#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/10
"""
from collections import defaultdict, deque
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
ZOOM = {
    "n": "|",
    "s": "|",
    "w": "-",
    "e": "-",
}


class Pixel:
    """Represents a single pixel in a grid of pipes"""

    def __init__(self, glyph="."):
        self.glyph = glyph
        self.connects = PIPES[glyph]
        self.kind = None

    def __str__(self):
        return self.glyph

    def __contains__(self, item):
        return item in self.connects

    def exit(self, start):
        """Determine the other end of the pipe, given start"""
        return self.connects.replace(start, "")


def count_inside(grid):
    """Count the number cells contained within the loop"""
    last = max(grid)
    search = deque()
    for row in range(0, last.x, 2):
        for col in range(0, last.y, 2):
            pos = Point2D(row, col)
            if grid[pos].kind == "loop":
                search.append(pos + Point2D(1, 1))
                break
        if search:
            break

    inside = 0
    while search:
        pos = search.pop()
        if grid[pos].kind:
            # already seen this one
            continue
        grid[pos].kind = "inside"
        if (pos.x % 2) == 0 and (pos.y % 2) == 0:
            inside += 1
        for direction in Point2D.cardinals:
            new_pos = pos + direction
            if (0 <= new_pos.x <= last.x) and (0 <= new_pos.y <= last.y):
                search.append(new_pos)
    return inside


def solve(part='a'):
    """Solve puzzle"""
    grid = defaultdict(Pixel)
    row = None
    col = None
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, char in enumerate(line):
            location = Point2D(2*row, 2*col)
            grid[location] = Pixel(char)
            if char == "S":
                start = location
                grid[location].kind = "loop"

    dest = None
    compass = None
    # figure out which way to go around the loop
    # this assumes that only 2 pipes are pointing toward the start
    for compass, direction in DIRECTIONS.items():
        source = compass.translate(CONNECT)
        if source in grid[start + direction + direction]:
            dest = start + direction
            break

    steps = 1
    extend = True
    while dest != start:
        if extend:
            grid[dest] = Pixel(ZOOM[compass])
        else:
            source = compass.translate(CONNECT)
            compass = grid[dest].exit(source)  # the direction we're now headed
            steps += 1
        grid[dest].kind = "loop"
        dest += DIRECTIONS[compass]  # move through the pipe
        extend = not extend

    if part == "a":
        return steps // 2
    return count_inside(grid)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
