#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/4
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=4, year=2022)


def parse_pair(line):
    """Parse a pair of elf section tasks"""
    sections = tuple(map(int, re.split('[-,]', line)))
    elf1 = set(range(sections[0], sections[1]+1))
    elf2 = set(range(sections[2], sections[3]+1))
    return elf1, elf2


def full_overlap(elf1, elf2):
    """Determine if one range is fully contained in the other"""
    intersect = elf1.intersection(elf2)
    return intersect in (elf1, elf2)


def partial_overlap(elf1, elf2):
    """Determine if there is any overlap between the ranges"""
    intersect = elf1.intersection(elf2)
    return bool(intersect)


def solve(part='a'):
    """Solve puzzle"""
    overlap = full_overlap
    if part == 'b':
        overlap = partial_overlap
    total = 0
    for line in PUZZLE.input.splitlines():
        pair = parse_pair(line)
        total += overlap(*pair)
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
