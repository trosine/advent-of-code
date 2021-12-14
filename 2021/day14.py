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
    # template = 'NNCB'
    rules = {}
    for rule in instructions.splitlines():
        rules[rule[0:2]] = rule[0] + rule[-1]
    for _ in range(cycles):
        new_template = ''
        for index in range(len(template) - 1):
            new_template += rules[template[index:index+2]]
        template = new_template + template[-1]
    counts = Counter(template)
    return max(counts.values()) - min(counts.values())


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
