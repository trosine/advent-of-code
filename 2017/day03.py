#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/3
"""
import operator
import aoc

DIRECTIONS = (
    (0, -1),
    (-1, 0),
    (0, 1),
    (1, 0),
)
NEIGHBORS = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
)
PUZZLE = aoc.Puzzle(day=3, year=2017)


def add_tuples(one, two):
    """Add two tuples element-wise"""
    return tuple(map(operator.add, one, two))


def solve_b():
    """Sum neighboring slots"""
    limit = int(PUZZLE.input)
    memory = {(0, 0): 1}
    width = 2
    pos = (0, 0)
    while True:
        pos = add_tuples(pos, (1, 1))
        for direction in DIRECTIONS:
            for _ in range(width):
                pos = add_tuples(pos, direction)
                total = 0
                for neighbor in NEIGHBORS:
                    total += memory.get(add_tuples(pos, neighbor), 0)
                memory[pos] = total
                # print(pos, total)
                if total > limit:
                    return total
        width += 2
    return None


def solve(part='a'):
    """Solve puzzle"""
    if part == 'b':
        return solve_b()
    # print(PUZZLE.input)
    address = int(PUZZLE.input)
    start = 2
    width = 2
    while 4 * width + start <= address:
        start = 4 * width + start
        width += 2
    tier = width // 2
    offset = address - start
    while offset >= width:
        offset -= width
    offset = abs(tier - offset - 1)
    return tier + offset


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
