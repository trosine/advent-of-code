#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/17
"""
import itertools
import operator
import aoc

ACTIVE = '#'
INACTIVE = '.'
PUZZLE = aoc.Puzzle(day=17, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        dimensions = 3
    else:
        dimensions = 4
    directions = [
        d
        for d in itertools.product(range(-1, 2), repeat=dimensions)
        if d != tuple([0]*dimensions)]
    state = {}
    lines = PUZZLE.input.splitlines()
    size = [1] * dimensions
    size[0] = len(lines)
    size[1] = len(lines[0])
    ranges = [range(d) for d in size]
    for cube in itertools.product(*ranges):
        state[cube] = lines[cube[0]][cube[1]]

    for turn in range(6):
        new_state = {}
        ranges = [range(-1-turn, d+turn+1) for d in size]
        for cube in itertools.product(*ranges):
            count = 0
            for direction in directions:
                neighbor = tuple(map(operator.add, cube, direction))
                count += state.get(neighbor) == ACTIVE
            if state.get(cube) == ACTIVE and count in (2, 3):
                new_state[cube] = ACTIVE
            elif state.get(cube, INACTIVE) == INACTIVE and count == 3:
                new_state[cube] = ACTIVE
        state = new_state
    count = 0
    for cube in state.values():
        count += cube == ACTIVE
    return count


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
