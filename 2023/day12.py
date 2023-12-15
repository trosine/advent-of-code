#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/12
"""
from itertools import combinations, groupby
import aoc

PUZZLE = aoc.Puzzle(day=12, year=2023)


def validate(spring, check):
    """Confirm that this spring matches the check data"""
    new_check = [len(list(g)) for c, g in groupby(spring) if c == "#"]
    return new_check == check


def solve(part='a'):
    """Solve puzzle"""
    if part == 'b':
        return None
    valid = 0
    for line in PUZZLE.input.splitlines():
        springs, check = line.split()
        check = [int(x) for x in check.split(",")]
        unknowns = [i for i, x in enumerate(springs) if x == "?"]
        to_place = sum(check) - springs.count("#")
        # print(springs, check, unknowns, to_place)
        for combo in combinations(unknowns, to_place):
            spring_list = list(springs)
            for i in unknowns:
                spring_list[i] = "#" if i in combo else "."
            is_valid = validate(spring_list, check)
            # print(" ", is_valid, "".join(spring_list))
            valid += is_valid

    return valid


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
