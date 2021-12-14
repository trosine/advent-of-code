#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/14
"""
from collections import Counter

import aoc

PUZZLE = aoc.Puzzle(day=14, year=2021)


def solve(part='a'):
    """Solve puzzle"""
    cycles = 10 if part == 'a' else 40
    template, instructions = PUZZLE.input.split('\n\n')
    # convert "AB -> C" to key="AB", value=("AC", "CB")
    # the values become the new pairs that we keep track of
    rules = {
        rule[0:2]: (rule[0] + rule[-1], rule[-1] + rule[1])
        for rule in instructions.splitlines()
        }
    pairs = Counter(
        template[index:index+2]
        for index in range(len(template) - 1)
        )

    for _ in range(cycles):
        new_pairs = Counter()
        for pair, count in pairs.items():
            for new_pair in rules[pair]:
                new_pairs[new_pair] += count
        pairs = new_pairs

    # seed the counter with the last char (not included in the loop)
    counts = Counter(template[-1])
    for pair, count in pairs.items():
        # the second character is the first char of a later pair
        counts[pair[0]] += count
    return max(counts.values()) - min(counts.values())


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
