#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/3
"""
import aoc

PUZZLE = aoc.Puzzle(day=3, year=2022)


def priority(common):
    """Calculate the priority value of common"""
    if common >= 'a':
        return ord(common) - ord('a') + 1
    return ord(common) - ord('A') + 27


def solve_b():
    """Solve puzzle part b"""
    total = 0
    sacks = PUZZLE.input.splitlines()
    for offset in range(0, len(sacks), 3):
        group = set(sacks[offset])
        group.intersection_update(sacks[offset+1])
        group.intersection_update(sacks[offset+2])
        total += priority(group.pop())
    return total


def solve(part='a'):
    """Solve puzzle"""
    if part == 'b':
        return solve_b()
    total = 0
    for sack in PUZZLE.input.splitlines():
        comp1 = set(sack[:len(sack)//2])
        comp2 = set(sack[len(sack)//2:])
        common = comp1.intersection(comp2).pop()
        total += priority(common)
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
