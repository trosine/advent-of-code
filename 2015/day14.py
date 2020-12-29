#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/14
"""
from collections import defaultdict, namedtuple
import re
import aoc

PUZZLE = aoc.Puzzle(day=14, year=2015)

Reindeer = namedtuple('Reindeer', ('name', 'speed', 'fly', 'rest'))


def solve(part='a'):
    """Solve puzzle"""
    parse = re.compile(
        r'(?P<name>\w+)\D+'
        r'(?P<speed>\d+)\D+'
        r'(?P<fly>\d+)\D+'
        r'(?P<rest>\d+)'
        )
    distances = {}
    places = defaultdict(int)
    if part == 'a':
        start = 2503
        winner = distances
    else:
        start = 1
        winner = places
    reindeer = []
    convert = (str, int, int, int)
    for deer in PUZZLE.input.splitlines():
        parsed = parse.match(deer).groups()
        reindeer.append(Reindeer(*[f(v) for f, v in zip(convert, parsed)]))
    for second in range(start, 2504):
        for deer in reindeer:
            burst = deer.fly + deer.rest
            # distance travelled in previous full bursts
            distance = deer.speed * (second // burst) * deer.fly
            # distance travelled in the last burst
            distance += deer.speed * min(second % burst, deer.fly)
            distances[deer.name] = distance
            # print(f'{distance} -- {deer}')
        farthest = max(distances.values())
        for deer, distance in distances.items():
            if distance == farthest:
                places[deer] += 1
    return max(winner.values())


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
