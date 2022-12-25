#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/13
"""
import functools
import itertools
import re

import aoc

PUZZLE = aoc.Puzzle(day=13, year=2022)
VALID = re.compile(r"^[\d,\n\[\]]+$")


def compare(left, right):
    """Compare two packets"""
    for lvalue, rvalue in itertools.zip_longest(left, right):
        if lvalue is None:
            return -1
        if rvalue is None:
            return 1
        if isinstance(lvalue, int) and isinstance(rvalue, int):
            if lvalue < rvalue:
                return -1
            if lvalue > rvalue:
                return 1
            continue  # both integers are equal
        # at this point, at least one value is a list
        if isinstance(lvalue, int):
            lvalue = [lvalue]
        if isinstance(rvalue, int):
            rvalue = [rvalue]
        result = compare(lvalue, rvalue)
        if result != 0:
            return result
    return 0


def solve(part='a'):
    """Solve puzzle"""
    total = 0
    marker1 = [[2]]
    marker2 = [[6]]
    packets = [marker1, marker2]
    for index, pair in enumerate(PUZZLE.input.split("\n\n"), start=1):
        left, right = pair.splitlines()
        if not VALID.search(left) or not VALID.search(right):
            print(f"Invalid pair: {left}, {right}")
            continue
        try:
            left = eval(left)  # pylint: disable=eval-used
            right = eval(right)  # pylint: disable=eval-used
        except SyntaxError:
            print(f"Eval failed for pair: {left}, {right}")
            continue
        if compare(left, right) < 0:
            total += index
        packets.append(left)
        packets.append(right)
    if part == 'a':
        return total
    packets.sort(key=functools.cmp_to_key(compare))
    return (packets.index(marker1)+1) * (packets.index(marker2)+1)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
