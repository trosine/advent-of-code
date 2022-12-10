#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/5
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=5, year=2022)
CRATES = re.compile(r'[A-Z]')
MOVE = re.compile(r'move (?P<count>\d+) from (?P<source>\d+) to (?P<dest>\d+)')


def parse_stacks(lines):
    """Convert the input data to a list of stacks to operate with"""
    # stacks[0] will be empty to simplify the execution of moves
    # since the stack numbers start from 1
    stacks = [[]]
    for _ in lines[-1].split():
        stacks.append([])
    for line in lines[::-1]:
        for match in CRATES.finditer(line):
            stacks[match.start()//4+1].append(match.group())
    return stacks


def execute(stacks, line, order=-1):
    """Update the stacks based on the line"""
    move = {
        key: int(val)
        for key, val in MOVE.match(line).groupdict().items()
    }
    source = stacks[move['source']]
    dest = stacks[move['dest']]
    moved = source[-move['count']:]

    stacks[move['source']] = source[:-move['count']]
    stacks[move['dest']] = dest + moved[::order]


def print_stacks(stacks):
    """Print out the stacks as simple strings"""
    for stack in stacks:
        print(''.join(stack))


def solve(part='a'):
    """Solve puzzle"""
    order = -1
    if part == 'b':
        order = 1
    stacks, moves = PUZZLE.input.split('\n\n')
    stacks = parse_stacks(stacks.splitlines())
    # print_stacks(stacks)
    for line in moves.splitlines():
        execute(stacks, line, order)
        # print_stacks(stacks)
    result = ''
    for stack in stacks[1:]:
        result += stack[-1]
    return result


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
