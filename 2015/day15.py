#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/15
"""
import functools
from itertools import product
from operator import mul
import re
import aoc

PUZZLE = aoc.Puzzle(day=15, year=2015)
PARSE = re.compile(r'(-?\d+)')


def solve(part='a'):
    """Solve puzzle"""
    # properties is the transposition of the input
    properties = [[] for _ in range(5)]
    for ingredient in PUZZLE.input.splitlines():
        for index, value in enumerate(PARSE.findall(ingredient)):
            properties[index].append(int(value))
    recipes = []
    for recipe in product(range(1, 98), repeat=len(properties[0])-1):
        if sum(recipe) >= 100:
            # too many ingredients already
            continue
        recipe += (100 - sum(recipe), )
        values = [max(0, sum(map(mul, recipe, p))) for p in properties]
        if part == 'b' and values[-1] != 500:
            # only consider recipes resulting in 500 calories
            continue
        recipes.append(functools.reduce(mul, values[:-1]))
    return max(recipes)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
