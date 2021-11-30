#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/9
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=9, year=2016)
MARKER = re.compile(r'\((\d+)x(\d+)\)')


def expand_size(text, skip=True):
    """Calculate the expanded size of text"""
    length = 0
    pos = 0
    while match := MARKER.search(text, pos):
        length += match.start() - pos  # characters since the previous block
        chars, repeat = map(int, match.groups())
        if skip:
            length += repeat * chars
        else:
            start = match.end()
            end = match.end() + chars
            length += repeat * expand_size(text[start:end], skip=skip)
        pos = match.end() + chars
    length += len(text) - pos  # characters after last block
    return length


def solve(part='a'):
    """Solve puzzle"""
    skip = part == 'a'
    text = PUZZLE.input
    # text = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
    # text = 'X(8x2)(3x3)ABCY'
    # text = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
    return expand_size(text, skip=skip)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
