#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/21
"""
import itertools

import aoc

PUZZLE = aoc.Puzzle(day=21, year=2021)


class Die:
    # pylint: disable=too-few-public-methods
    """The die used in the game"""

    def __init__(self):
        self._iter = itertools.cycle(range(1, 101))
        self.rolls = 0

    def roll(self):
        """Roll the die 3 times"""
        self.rolls += 3
        return sum(next(self._iter) for _ in range(3))


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        pass
    positions = [
        int(player.split()[-1]) % 10
        for player in PUZZLE.input.splitlines()
        ]
    # positions = [4, 8]
    die = Die()
    scores = [0, 0]
    player = 0
    while True:
        roll = die.roll()
        position = (positions[player] + roll) % 10
        positions[player] = position
        scores[player] += position or 10  # position 0 is really position 10
        if scores[player] >= 1000:
            print(f'rolls={die.rolls}, {scores}')
            return scores[1-player] * die.rolls
        player = 1 - player
    print(positions)
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
