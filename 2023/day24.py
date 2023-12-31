#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/24
"""
from itertools import combinations
import numpy
import aoc

PUZZLE = aoc.Puzzle(day=24, year=2023)


# https://stackoverflow.com/questions/74265725/find-intersection-of-two-vectors-with-numpy/74266064
def intersect(line1, line2):
    """Determine where the two lines intersect"""
    # this is basically solving Ax = b
    # where A is a vector matrix, and b the combined constants of the 2 lines
    # the resulting x values are the units along each of the individual lines
    # where the intersect happens
    coeff = numpy.array([line1[1], -line2[1]]).T
    const = line2[0] - line1[0]
    x_values, rank = numpy.linalg.lstsq(coeff, const, rcond=None)[:3:2]
    if rank == 2:
        return line1[1] * x_values[0] + line1[0]
    return None


def is_future(point, line):
    """Determine if this point is in the future"""
    return all(numpy.sign(line[1]) == numpy.sign(point-line[0]))


def solve(part="a"):
    """Solve puzzle"""
    data = PUZZLE.input
    window = (7, 27)
    window = (200000000000000, 400000000000000)
    dim = slice(None, -1)
    if part == "b":
        dim = slice(None)
        # return None
    lines = []
    for line in data.splitlines():
        pos, velocity = line.split(" @ ")
        pos = numpy.array([int(x) for x in pos.split(",")[dim]])
        velocity = numpy.array([int(x) for x in velocity.split(",")[dim]])
        lines.append((pos, velocity))
    total = 0
    for line1, line2 in combinations(lines, 2):
        point = intersect(line1, line2)
        if point is None:
            print("A:", line1)
            print("B:", line2)
            print()
            continue
        in_window = all(window[0] <= c <= window[1] for c in point)
        in_future = all(is_future(point, line) for line in (line1, line2))
        if in_window and in_future:
            total += 1
            # print("A:", line1)
            # print("B:", line2)
            # print("I:", in_window, in_future, point)
            # print()
            # break
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
