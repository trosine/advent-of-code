#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/1
"""
import aoc

PUZZLE = aoc.Puzzle(day=1, year=2016)

CHANGES = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    )


def solve(part='a'):
    """Solve puzzle"""
    path = PUZZLE.input.split(', ')
    # path = ('R8,R4,R4,R8').split(',')
    direction = 0
    pos = (0, 0)
    previous = [pos]
    for turn in path:
        direction += -1 if turn[0] == 'L' else 1
        direction %= 4
        count = int(turn[1:])
        # this loop isn't really needed for part a
        # but part b needs to know every intersection that was walked through
        for _ in range(count):
            pos = tuple(
                x + CHANGES[direction][i]
                for i, x in enumerate(pos)
                )
            if part == 'b' and pos in previous:
                return sum(map(abs, pos))
            previous.append(pos)
        print(pos)
    return sum(map(abs, pos))


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
