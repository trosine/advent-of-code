#!/usr/bin/env python3
"""
https://adventofcode.com/2024/day/4
"""
import aoc

import numpy as np

PAIRS = [
    [(-1, -1), (1, 1)],
    [(-1, 1), (1, -1)],
]
PUZZLE = aoc.Puzzle(day=4, year=2024)


def count(array):
    """Count the occurrances of XMAS forward and reverse"""
    total = 0
    for line in array:
        string = "".join(line)
        total += string.count("XMAS")
        total += string.count("SAMX")
    return total


def diagonal(array):
    """Extract the diagonals from the array"""
    start = - max(array.shape)
    end = abs(start)
    for offset in range(start, end):
        yield array.diagonal(offset=offset)


def find_x(array):
    """Find X-MAS pattern"""
    total = 0
    for index in np.argwhere(array == "A"):
        # "A" was found on the edge
        if not 0 < index[0] < array.shape[0]-1:
            continue
        if not 0 < index[1] < array.shape[1]-1:
            continue

        total += is_x_pattern(array, index)
    return total


def is_x_pattern(array, index):
    """Determines if this index is an X-MAS pattern"""
    valid = set("MS")
    # in each diagonal direction, we check to see if the neighboring letters
    # are M and S (order doesn't matter, since there are only 2 letters)
    # only if both diagonals are valid, is the X pattern is found
    for pair in PAIRS:
        letters = set()
        for direction in pair:
            letters.add(array[tuple(index + direction)])
        if letters != valid:
            return False
    return True


def solve(part="a"):
    """Solve puzzle"""
    array = np.array(
        [list(line) for line in PUZZLE.input.splitlines()]
    )
    if part == "b":
        return find_x(array)
    total = 0
    total += count(array)
    total += count(array.T)
    total += count(diagonal(array))
    total += count(diagonal(array.T))
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
