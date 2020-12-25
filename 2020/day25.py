#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/25
"""
import aoc

PUZZLE = aoc.Puzzle(day=25, year=2020)


def transform(subject, value=1, loops=1):
    """Transform the current key"""
    for _ in range(loops):
        value = subject * value % 20201227
    return value


def get_loops(target, subject=7):
    """Find how many loops it takes to transform to a target"""
    value = 1
    loops = 0
    while value != target:
        value = transform(subject, value=value)
        loops += 1
    # print(f'took {loops} loops to generate {target}')
    return loops


def solve(part='a'):
    """Solve puzzle"""
    del part  # no part b
    public = tuple(map(int, PUZZLE.input.splitlines()))
    loops = tuple(get_loops(x, 7) for x in public)
    shortest = loops.index(min(loops))
    return transform(public[(shortest+1) % 2], loops=loops[shortest])


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
