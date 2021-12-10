#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/7
"""
import aoc

PUZZLE = aoc.Puzzle(day=7, year=2021)


def sum_of(number):
    """Returns the sum of all integers from 1..number"""
    return number * (number + 1) // 2


def solve(part='a'):
    """Solve puzzle"""
    crabs = list(map(int, PUZZLE.input.split(',')))
    # crabs = list(map(int, '16,1,2,0,4,2,7,1,2,14'.split(',')))
    if part == 'a':
        calc_func = int
        # converge = statistics.median(crabs)
        # fuel = sum(abs(crab-converge) for crab in crabs)
    else:
        calc_func = sum_of
    possibles = [
        sum(calc_func(abs(crab-converge)) for crab in crabs)
        for converge in range(min(crabs), max(crabs))
        ]
    fuel = min(possibles)
    converge = possibles.index(fuel)
    print(f'converge={converge}, fuel={fuel}')
    return fuel


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
