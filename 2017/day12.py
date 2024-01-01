#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/12
"""
from collections import defaultdict
import aoc

PUZZLE = aoc.Puzzle(day=12, year=2017)


def collect_group(programs, start):
    """Find all of the programs within a given group"""
    in_group = set()
    queue = [start]
    while queue:
        program = queue.pop()
        in_group.add(program)
        for dest in programs[program]:
            if dest not in in_group:
                queue.append(dest)
    return in_group


def solve(part="a"):
    """Solve puzzle"""
    # if part == "b":
    #     return None
    programs = defaultdict(set)
    for line in PUZZLE.input.splitlines():
        source, destinations = line.split(" <-> ")
        for dest in destinations.split(", "):
            programs[source].add(dest)
    if part == "a":
        return len(collect_group(programs, "0"))
    groups = 0
    while programs:
        groups += 1
        start = list(programs.keys())[0]
        group = collect_group(programs, start)
        for program in group:
            del programs[program]
    return groups


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
