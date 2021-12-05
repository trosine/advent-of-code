#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/15
"""
import itertools
import re

import aoc

PUZZLE = aoc.Puzzle(day=15, year=2016)
PARSE = re.compile(r'Disc #(\d) has (\d+) positions;.* at position (\d+)')


def solve(part='a'):
    """Solve puzzle"""
    discs = {}
    for line in PUZZLE.input.splitlines():
        disc, positions, initial = map(int, PARSE.match(line).groups())
        discs[disc] = (positions, initial)
    if part == 'b':
        discs[max(discs.keys()) + 1] = (11, 0)
    for time in itertools.count():
        for disc, info in discs.items():
            reach = time + disc  # the time it will reach this disc
            positions, initial = info
            if (reach + initial) % positions != 0:
                # bounce off
                break
        else:
            return time
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
