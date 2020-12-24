#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/6
"""
import itertools
import re
import aoc

PUZZLE = aoc.Puzzle(day=6, year=2015)
PARSE = re.compile(
    r'(?P<action>toggle|turn on|turn off)\s+'
    r'(?P<startx>\d+),(?P<starty>\d+)'
    r' through '
    r'(?P<endx>\d+),(?P<endy>\d+)'
    )
COMMANDS_A = {
    'turn on': lambda _: 1,
    'turn off': lambda _: 0,
    'toggle': lambda x: int(not x),
    }
COMMANDS_B = {
    'turn on': lambda x: x + 1,
    'turn off': lambda x: max(x - 1, 0),
    'toggle': lambda x: x + 2,
    }


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        commands = COMMANDS_A
    else:
        commands = COMMANDS_B
    lights = [[0] * 1000 for _ in range(1000)]
    for cmd in PUZZLE.input.splitlines():
        cmd = PARSE.match(cmd).groupdict()
        x_range = range(int(cmd['startx']), int(cmd['endx'])+1)
        y_range = range(int(cmd['starty']), int(cmd['endy'])+1)
        for posx, posy in itertools.product(x_range, y_range):
            lights[posx][posy] = commands[cmd['action']](lights[posx][posy])

    return sum([sum(row) for row in lights])


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
