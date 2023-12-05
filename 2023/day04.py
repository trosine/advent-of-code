#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/4
"""
import collections
import re

import aoc

PUZZLE = aoc.Puzzle(day=4, year=2023)
PARSE = re.compile(r"Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)")


def parse(line):
    """Parse an individual card"""
    match = PARSE.match(line)
    card, winners, hand = match.groups()

    # convert types
    card = int(card)
    winners = set(winners.split())
    hand = set(hand.split())

    return card, winners, hand


def solve(part='a'):
    """Solve puzzle"""
    total = 0
    cards = collections.defaultdict(lambda: 1)
    for line in PUZZLE.input.splitlines():
        card, winners, hand = parse(line)
        matching = len(winners & hand)
        if matching > 0:
            total += 2 ** (matching-1)
        cards[card] += 0  # ensure this card exists in the dict
        for copy in range(card+1, card+matching+1):
            cards[copy] += cards[card]

    if part == "b":
        return sum(cards.values())
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
