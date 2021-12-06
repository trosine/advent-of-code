#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/6
"""
import aoc

PUZZLE = aoc.Puzzle(day=6, year=2021)


def solve(part='a'):
    """Solve puzzle"""
    days = 80 if part == 'a' else 256
    fish = [0] * 9
    for individual in map(int, PUZZLE.input.split(',')):
        fish[individual] += 1
    for _ in range(days):
        spawn = fish.pop(0)
        fish.append(spawn)
        fish[6] += spawn
    return sum(fish)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
