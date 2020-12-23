#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/3
"""
import collections
import operator
import aoc

PUZZLE = aoc.Puzzle(day=3, year=2015)
MOVES = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
    }


def deliver(houses, moves):
    """Deliver presents to houses"""
    pos = (0, 0)
    houses[pos] += 1
    for move in moves:
        pos = tuple(map(operator.add, pos, MOVES[move]))
        houses[pos] += 1


def solve(part='a'):
    """Solve puzzle"""
    houses = collections.Counter()
    moves = PUZZLE.input.strip()
    if part == 'a':
        deliver(houses, moves)
    else:
        for santa in (0, 1):
            deliver(houses, [m for i, m in enumerate(moves) if i % 2 == santa])
    return len(houses)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
