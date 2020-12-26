#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/9
"""
import itertools
import re
import aoc

PUZZLE = aoc.Puzzle(day=9, year=2015)
PARSE = re.compile(r'(\w+)\s+to\s+(\w+)\s+=\s+(\d+)')


def solve(part='a'):
    """Solve puzzle"""
    distance = {}
    for line in PUZZLE.input.splitlines():
        groups = PARSE.match(line).groups()
        distance[groups[:2]] = int(groups[2])
        distance[groups[1::-1]] = int(groups[2])
    cities = set(x[0] for x in distance)
    lengths = set()
    for path in itertools.permutations(cities):
        length = 0
        last = None
        for city in path:
            if last is not None:
                length += distance[(last, city)]
            last = city
        lengths.add(length)
    if part == 'a':
        return min(lengths)
    return max(lengths)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
