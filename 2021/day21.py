#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/21
"""
import collections
import itertools

import aoc

PUZZLE = aoc.Puzzle(day=21, year=2021)


def solve_b(positions):
    """Solve puzzle part b"""
    rolls = collections.Counter(
        sum(rolls)
        for rolls in itertools.product(range(1, 4), repeat=3)
        )
    unfinished = {(positions[0], positions[1], 0, 0): 1}
    finished = collections.defaultdict(int)
    turn = 0
    while unfinished:
        # print(f'unfinished={len(unfinished)}, finished={finished}')
        new_states = collections.defaultdict(int)
        for roll, frequency in rolls.items():
            for state, universes in unfinished.items():
                state = list(state)
                universes *= frequency
                state[turn] = (state[turn] + roll) % 10 or 10
                state[turn+2] += state[turn]
                if state[turn+2] >= 21:
                    finished[turn] += universes
                else:
                    new_states[tuple(state)] += universes
        unfinished = new_states
        turn = 1 - turn
    return max(finished.values())


def solve(part='a'):
    """Solve puzzle"""
    positions = [
        int(player.split()[-1]) % 10
        for player in PUZZLE.input.splitlines()
        ]
    # positions = [4, 8]
    if part == 'b':
        return solve_b(positions)

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
    PUZZLE.report_b(solve('b'))
