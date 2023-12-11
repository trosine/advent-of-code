#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/8
"""
from itertools import cycle
import math
import re

import aoc

PUZZLE = aoc.Puzzle(day=8, year=2023)
NODE = re.compile(r"(?P<name>\w+) = \((?P<L>\w+), (?P<R>\w+)\)")


def human_start(name):
    """Determine if this is the starting point for a human"""
    return name == "AAA"


def human_end(name):
    """Determine if this is the ending point for a human"""
    return name == "ZZZ"


def ghost_start(name):
    """Determine if this is the starting point for a ghost"""
    return name[-1] == "A"


def ghost_end(name):
    """Determine if this is the ending point for a ghost"""
    return name[-1] == "Z"


def solve(part='a'):
    """Solve puzzle"""
    if part == "a":
        is_start = human_start
        is_end = human_end
    else:
        is_start = ghost_start
        is_end = ghost_end

    directions, lines = PUZZLE.input.split("\n\n")
    network = {}
    for line in lines.splitlines():
        match = NODE.match(line)
        node = match.groupdict()
        network[node["name"]] = node

    all_steps = []
    for name, node in network.items():
        if not is_start(name):
            continue
        steps = 0
        for direction in cycle(directions):
            if is_end(node["name"]):
                break
            node = network[node[direction]]
            steps += 1
        all_steps.append(steps)
    return math.lcm(*all_steps)  # pylint: disable=c-extension-no-member


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
