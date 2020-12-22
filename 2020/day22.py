#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/22
"""
import collections
import aoc

PUZZLE = aoc.Puzzle(day=22, year=2020)


def score(winner):
    """Calculate the winning score for the winner"""
    multiplier = 1
    total = 0
    while len(winner) > 0:
        total += multiplier * winner.pop()
        multiplier += 1
    return total


def regular(player1, player2):
    """Play a normal game of combat"""
    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.popleft()
        card2 = player2.popleft()
        if card1 > card2:
            player1.extend((card1, card2))
        else:
            player2.extend((card2, card1))
    if len(player1) > 0:
        winner = player1
    else:
        winner = player2
    return score(winner)


def recursive(player1, player2, report_score=False):
    """Play a recursive game of combat"""
    previous_rounds = set()
    while len(player1) > 0 and len(player2) > 0:
        this_round = (
            ','.join(map(str, list(player1))),
            ','.join(map(str, list(player2))),
            )
        if this_round in previous_rounds:
            # this game's winner is player1 (detected below outside the while)
            break
        previous_rounds.add(this_round)
        card1 = player1.popleft()
        card2 = player2.popleft()
        if len(player1) >= card1 and len(player2) >= card2:
            winner_name = recursive(
                collections.deque(list(player1)[:card1]),
                collections.deque(list(player2)[:card2]),
                )
        elif card1 > card2:
            winner_name = 1
        else:
            winner_name = 2
        if winner_name == 1:
            player1.extend((card1, card2))
        else:
            player2.extend((card2, card1))
    if len(player1) > 0:
        winner = player1
        winner_name = 1
    else:
        winner = player2
        winner_name = 2
    if report_score:
        return score(winner)
    return winner_name


def solve(part='a'):
    """Solve puzzle"""
    player1, player2 = PUZZLE.input.split('\n\n')
    player1 = collections.deque(map(int, player1.splitlines()[1:]))
    player2 = collections.deque(map(int, player2.splitlines()[1:]))
    if part == 'a':
        return regular(player1, player2)
    return recursive(player1, player2, report_score=True)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
