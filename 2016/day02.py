#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/2
"""
from operator import add

import aoc

PUZZLE = aoc.Puzzle(day=2, year=2016)
KEYPAD = {
    'a': (
        '123',
        '456',
        '789',
        ),
    'b': (
        '  1',
        ' 234',
        '56789',
        ' ABC',
        '  D',
        ),
    }
DIRECTIONS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
    }


def solve(part='a'):
    """Solve puzzle"""
    keypad = KEYPAD[part]
    pos = (1, 1)
    if part == 'b':
        pos = (2, 0)
    code = ''
    data = PUZZLE.input
    data = 'ULL\nRRDDD\nLURDL\nUUUUD'
    key = '5'
    for line in data.splitlines():
        for direction in line:
            new_pos = tuple(map(add, pos, DIRECTIONS[direction]))
            if new_pos[0] < 0 or new_pos[1] < 0:
                # negative index: stay on current key
                continue
            try:
                new_key = keypad[new_pos[0]][new_pos[1]]
                if new_key == ' ':
                    continue
                key = new_key
            except IndexError:
                # key beyond the bottom/right of keypad
                continue
            pos = new_pos
        code += key
    return code


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
