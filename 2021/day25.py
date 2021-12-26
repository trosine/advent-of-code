#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/25
"""
import collections
import itertools

import aoc

PUZZLE = aoc.Puzzle(day=25, year=2021)


class Point(collections.namedtuple('PointT', ['row', 'col'])):
    """A location in the grid"""

    def destination(self, kind, modulus):
        """Determine where this cucumber's destination is"""
        offset = int(kind == '>')
        pos = list(self)
        pos[offset] = (pos[offset] + 1) % modulus[offset]
        return Point(*pos)


def move(east, south, modulus):
    """Move all cucumbers"""
    moved = False

    total = east.union(south)
    new_east = set()
    for pos in east:
        dest = pos.destination('>', modulus)
        if dest not in total:
            moved = True
            new_east.add(dest)
        else:
            new_east.add(pos)

    total = new_east.union(south)
    new_south = set()
    for pos in south:
        dest = pos.destination('v', modulus)
        if dest not in total:
            moved = True
            new_south.add(dest)
        else:
            new_south.add(pos)
    return moved, new_east, new_south


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        pass
    step = None
    row = None
    col = None
    east = set()
    south = set()
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, kind in enumerate(line):
            if kind == '>':
                east.add(Point(row, col))
            elif kind == 'v':
                south.add(Point(row, col))
    last = Point(row + 1, col + 1)
    for step in itertools.count(1):
        moved, east, south = move(east, south, last)
        if not moved:
            break
    for row in range(last.row):
        line = ''
        for col in range(last.col):
            pos = Point(row, col)
            if pos in east:
                line += '>'
            elif pos in south:
                line += 'v'
            else:
                line += '.'
        print(line)
    return step


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
