#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/10
"""
from itertools import combinations
import functools
import aoc

PUZZLE = aoc.Puzzle(day=10, year=2020)


def valid_removal(removals):
    """Checks to see if these adapters can be removed"""
    if len(removals) < 3:
        return True
    for index, item in enumerate(removals[:-2]):
        if removals[index + 2] == item + 2:
            # attempt to remove 3 consecutive items
            return False
    return True


@functools.cache
def valid_chains(items):
    """Determine the number of valid chains in a list of length items"""
    if items <= 2:
        return 1
    result = 1
    adapters = range(1, items-1)
    for remove in adapters:
        for removals in combinations(adapters, remove):
            if valid_removal(removals):
                result += 1
    print(f'  list of {items} items has {result} valid combinations')
    return result


def solve(part='a'):
    """Solve puzzle"""
    adapters = [
        1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
        32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49,
        ]
    adapters = map(int, PUZZLE.input.splitlines())
    previous = 0
    differences = [None, 0, 0, 1]
    group = 1
    product = 1
    for adapter in sorted(adapters):
        difference = adapter - previous
        differences[difference] += 1
        if difference == 3:
            product *= valid_chains(group)
            group = 1
        else:
            group += 1
        previous = adapter
    product *= valid_chains(group)
    print(differences)
    if part == 'a':
        return differences[1] * (differences[3])
    return product


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
