#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/2
"""
import aoc

PUZZLE = aoc.Puzzle(day=2, year=2021)


def solve(part='a'):
    """Solve puzzle"""
    aim = 0
    depth = 0
    pos = 0
    for command in PUZZLE.input.splitlines():
        direction, value = command.split()
        value = int(value)
        if direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
        else:
            pos += value
            depth += aim * value
    if part == 'a':
        return pos * aim
    return pos * depth


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
