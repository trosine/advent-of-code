#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/14
"""
import aoc

PUZZLE = aoc.Puzzle(day=14, year=2022)


def print_cave(cave):
    """Display the cave"""
    values = [x for x, y in cave]
    edges = [min(values), max(values)]
    edges.append(max([y for x, y in cave]))
    for row in range(0, edges[2]+1):
        for col in range(edges[0], edges[1]+1):
            print(cave.get((col, row), " "), end="")
        print()
    input()


def add_sand(cave, max_y, floor):
    """Add sand to the cave"""
    current = (500, 0)
    while True:
        next_row = current[1] + 1
        default = None
        if not floor and next_row > max_y:
            return None
        if floor and next_row == max_y + 2:
            default = "#"
        left, center, right = [
            (current[0]+x, next_row)
            for x in (-1, 0, 1)
        ]
        if cave.get(center, default):
            if not cave.get(left, default):
                current = left
                continue
            if not cave.get(right, default):
                current = right
                continue
            cave[current] = 'o'
            return current
        current = center


def add_line(cave, start, end):
    """Add a line to the cave"""
    for col in range(start[0], end[0]+1):
        for row in range(start[1], end[1]+1):
            cave[(col, row)] = '#'


def solve(part='a'):
    """Solve puzzle"""
    cave = {}
    for line in PUZZLE.input.splitlines():
        points = line.split(' -> ')
        previous = None
        # previous = tuple(map(int, points[0].split()))
        for current in points:
            current = tuple(map(int, current.split(",")))
            if previous:
                start, end = sorted((previous, current))
                add_line(cave, start, end)
            previous = current
    max_y = max([y for x, y in cave])
    added = 0
    # print_cave(cave)
    while placed := add_sand(cave, max_y, part == "b"):
        added += 1
        if placed == (500, 0):
            break
        # print_cave(cave)
    return added


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
