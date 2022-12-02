#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/2
"""
import aoc

PUZZLE = aoc.Puzzle(day=2, year=2022)
OUTCOMES = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}
# the value is an offset and the score for the hand
OFFSETS = {
    'X': (-1, 0),  # need to lose, so select the "previous" one
    'Y': (0, 3),  # need to draw, so select the "same" one
    'Z': (-2, 6),  # need to win, so select the "next" one
}
OPPONENT = 'ABC'
SELF = 'XYZ'


def score_a(hand):
    """Calculate the score for the given hand assuming XYZ = RPS"""
    _, self = hand.split()
    score = SELF.index(self) + 1 + OUTCOMES[hand]
    return score


def score_b(hand):
    """Calculate the score for the given hand assuming XYZ = LDW"""
    opp, result = hand.split()
    offset, hand_score = OFFSETS[result]
    chosen = OPPONENT.index(opp) + offset
    # score = SELF.index(SELF[chosen]) + 1 + hand_score
    score = chosen % 3 + 1 + hand_score
    return score


def solve(part='a'):
    """Solve puzzle"""
    score = score_a
    if part == 'b':
        score = score_b
    total = 0
    for hand in PUZZLE.input.splitlines():
        total += score(hand)
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
