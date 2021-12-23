#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/21
"""
import itertools

import aoc

PUZZLE = aoc.Puzzle(day=21, year=2021)




def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        pass
    positions = [
        int(player.split()[-1]) % 10
        for player in PUZZLE.input.splitlines()
        ]
    # positions = [4, 8]
    scores = [0, 0]
    player = 0
    rolls = 0
    die = itertools.count(1)
    while True:
        rolls += 3
        roll = sum(next(die) for _ in range(3))
        # position 0 is really position 10
        position = (positions[player] + roll) % 10 or 10
        positions[player] = position
        scores[player] += position
        if scores[player] >= 1000:
            # print(f'rolls={rolls}, {scores}')
            return scores[1-player] * rolls
        player = 1 - player
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
