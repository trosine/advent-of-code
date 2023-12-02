#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/2
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=2, year=2023)
GAME = re.compile(r"Game\s+(\d+)")
TURN = re.compile(r"(?P<number>\d+)\s+(?P<color>red|green|blue)")
VALIDATION = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse(line):
    """Validate the game"""
    game, line = line.split(":")
    game = GAME.match(game).group(1)
    minimum = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for match in TURN.finditer(line):
        count, color = match.groups()
        minimum[color] = max(minimum[color], int(count))
    return game, minimum


def solve(part="a"):
    """Solve puzzle"""
    valid_total = 0
    power_total = 0
    for line in PUZZLE.input.splitlines():
        game, minimum = parse(line)
        valid = True
        power = 1
        for color, count in minimum.items():
            power *= count
            if count > VALIDATION[color]:
                valid = False
        power_total += power
        if valid:
            valid_total += int(game)
    if part == "a":
        return valid_total
    return power_total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
