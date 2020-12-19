#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/15
"""
import aoc

PUZZLE = aoc.Puzzle(day=15, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        rounds = 2020
    else:
        rounds = 30000000
    starters = list(map(int, PUZZLE.input.split(',')))
    # starters = [0, 3, 6]
    history = dict(zip(starters, range(len(starters)-1)))
    last_stated = starters[-1]
    for turn in range(len(starters), rounds):
        when = history.get(last_stated, turn-1)
        stated = turn - when - 1
        history[last_stated] = turn - 1
        last_stated = stated
    return last_stated


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
