#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/11
"""
from collections import namedtuple
from point import PointFunctions
import aoc

PUZZLE = aoc.Puzzle(day=11, year=2017)


# https://www.redblobgames.com/grids/hexagons/
class HexCubeFlat(PointFunctions, namedtuple("HexCubeFlat", "q r s")):
    """Represent a point in a Hex grid with flat-top (North is a neighbor)

    In this representation, q + r + s = 0 (ie, moving se,sw,n returns to the
    original).
    """

    directions = {
        "n": (0, -1, 1),
        "ne": (1, -1, 0),
        "se": (1, 0, -1),
        "s": (0, 1, -1),
        "sw": (-1, 1, 0),
        "nw": (-1, 0, 1),
    }

    def distance(self, other):
        # Note above how moving 1 tile consists of 2 distinct moves in the
        # coordinate system - hence the division by 2
        return super().distance(other) // 2


def solve(part="a"):
    """Solve puzzle"""
    data = PUZZLE.input
    origin = HexCubeFlat(0, 0, 0)
    pos = origin
    distances = []
    for direction in data.split(","):
        pos += pos.directions[direction]
        distances.append(pos.distance(origin))
    if part == "a":
        return pos.distance(origin)
    return max(distances)


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
