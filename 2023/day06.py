#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/6
"""
import aoc

PUZZLE = aoc.Puzzle(day=6, year=2023)


def count_better(time, minimum):
    """Determine how many different ways to get better distances"""
    better = 0
    for held in range(time):
        run_time = time - held
        if held * run_time > minimum:
            better += 1
    return better


def solve(part='a'):
    """Solve puzzle"""
    records = PUZZLE.input
    if part == 'b':
        records = records.replace(" ", "")
    times, distances = records.splitlines()
    times = map(int, times.split(":")[1].split())
    distances = map(int, distances.split(":")[1].split())
    races = zip(times, distances)
    product = 1
    for race in races:
        product *= count_better(*race)
    return product


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
