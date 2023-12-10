#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/7
"""
from collections import Counter
from functools import cache

import aoc

PUZZLE = aoc.Puzzle(day=7, year=2023)
TO_HEX = str.maketrans("TJQKA", "abcde")
TO_JOKER = str.maketrans("TJQKA", "a0cde")


class Hand:
    """Represents a hand of CamelCards"""

    def __init__(self, hand, joker=False):
        self.cards, self.bid = hand.split()
        self.bid = int(self.bid)
        self.joker = joker
        translation = TO_JOKER if joker else TO_HEX
        self._cards = self.cards.translate(translation)

    def __lt__(self, other):
        assert isinstance(other, Hand)
        self_sort = (self.strength(), self._cards)
        other_sort = (other.strength(), other._cards)
        return self_sort < other_sort

    def __str__(self):
        return f"Hand({self.cards}, {self.bid})"

    @cache
    def strength(self):
        """Return the strength of a hand"""
        # weights each rank by the (number of cards ^ 2)
        # this weights each group significantly higher than the sum of smaller
        # groups
        #   * a pair becomes 4 instead of 2
        #   * three of a kind becomes 9 instead of 3 (or 5)
        counter = Counter(self._joker_cards())
        total = 0
        for value in counter.values():
            total += value ** 2
        return total

    def _joker_cards(self):
        # convert jokers to create the best hand
        if not self.joker:
            return self.cards
        counter = Counter(self.cards)
        del counter["J"]
        if not counter:
            # all jokers - just return
            return self.cards
        cards = list(sorted(counter, key=lambda k: counter[k], reverse=True))
        return self.cards.replace("J", cards[0])


def solve(part='a'):
    """Solve puzzle"""
    hands = [Hand(hand, (part == "b")) for hand in PUZZLE.input.splitlines()]
    hands = sorted(hands)
    winnings = 0
    for rank, hand in enumerate(hands, 1):
        winnings += rank * hand.bid
    return winnings


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
