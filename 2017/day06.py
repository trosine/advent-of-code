#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/6
"""
import aoc

PUZZLE = aoc.Puzzle(day=6, year=2017)


def redistribute(banks):
    """Redistribute the memory blocks across the banks"""
    width = len(banks)
    to_move = max(banks)
    bank = banks.index(to_move)
    banks[bank] = 0
    for _ in range(to_move):
        bank = (bank + 1) % width
        banks[bank] += 1


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        pass
    steps = 0
    seen = set()  # for faster `in` lookups
    history = []  # for part b
    banks = list(map(int, PUZZLE.input.split()))
    print(banks)
    while tuple(banks) not in seen:
        steps += 1
        seen.add(tuple(banks))
        history.append(tuple(banks))
        redistribute(banks)
    if part == 'a':
        return steps
    return len(history) - history.index(tuple(banks))


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
