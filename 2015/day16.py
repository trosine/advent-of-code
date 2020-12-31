#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/16
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=16, year=2015)
TARGET = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
    }


def solve(part='a'):
    """Solve puzzle"""
    for sue in PUZZLE.input.splitlines():
        for item, number in re.findall(r'(\w+): (\d+)', sue):
            number = int(number)
            if part == 'b' and item in ('cats', 'trees'):
                if number <= TARGET[item]:
                    break
            elif part == 'b' and item in ('pomeranians', 'goldfish'):
                if number >= TARGET[item]:
                    break
            else:
                if number != TARGET[item]:
                    break
        else:
            return re.match(r'Sue (\d+)', sue).group(1)
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
