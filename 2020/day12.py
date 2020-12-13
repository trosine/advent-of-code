#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/12
"""
from operator import add, mul
import aoc

PUZZLE = aoc.Puzzle(day=12, year=2020)
FORWARD_COMMANDS = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
    }
COMMANDS = {
    'N': lambda x: (0, x, 0),
    'S': lambda x: (0, -x, 0),
    'E': lambda x: (x, 0, 0),
    'W': lambda x: (-x, 0, 0),
    'L': lambda x: (0, 0, -x),
    'R': lambda x: (0, 0, x),
    }


def exec_way(command, state):
    """Move the waypoint around the ship"""
    movement = command[0]
    value = int(command[1:])
    pos = state[:2]
    way = state[2:]
    if movement == 'F':
        # multiply waypoint by the distance, and add to position
        move = map(mul, way, (value, value))
        return list(map(add, pos, move)) + way
    if movement in 'NSEW':
        # update the waypoint position, based on the movement needed
        return pos + list(map(add, way, COMMANDS[movement](value)))
    if value == 180:
        # rotate 180 - multiply the waypoint by -1
        return list(map(mul, state, (1, 1, -1, -1)))
    # rotation of 90 degrees in one direction or another
    way.reverse()
    if command in ('L90', 'R270'):
        way[0] *= -1
    else:
        way[1] *= -1
    return pos + way


def exec_ship(command, state):
    """Move the ship according to command"""
    movement = command[0]
    value = int(command[1:])
    if movement == 'F':
        movement = FORWARD_COMMANDS[state[2]]
    adjustment = list(map(add, state, COMMANDS[movement](value)))
    adjustment[2] %= 360
    return adjustment


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        state = [0, 0, 90]
        execute = exec_ship
    else:
        state = [0, 0, 10, 1]
        execute = exec_way
    for command in PUZZLE.input.splitlines():
        state = execute(command, state)
        # print(command, state, sep='\t')
    return abs(state[0]) + abs(state[1])


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
