#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/6

Custom Customs

For each group, git a count of the unique answers, then sum all of the group
counts.
"""
import aoc

PUZZLE = aoc.Puzzle(day=6, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    total = 0
    update = 'update'
    if part == 'b':
        update = 'intersection_update'
    for group in PUZZLE.input.split('\n\n'):
        group_lines = group.splitlines()
        group_result = set(group_lines[0])
        for line in group_lines[1:]:
            getattr(group_result, update)(set(line))
        total += len(group_result)
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
