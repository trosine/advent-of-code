#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/10
"""
from collections import defaultdict
import re

import aoc

PUZZLE = aoc.Puzzle(day=10, year=2016)
VALUE = re.compile(r'value (\d+) goes to (bot \d+)')
GIVE = re.compile(
    r'(bot \d+) gives '
    r'low to ((?:bot|output) \d+) and '
    r'high to ((?:bot|output) \d+)'
    )


def add_chip(bot, chip):
    """Add a chip to a bot - returns True if it's holding 2 chips"""
    bot.append(chip)
    bot.sort()
    return len(bot) == 2


def solve(part='a'):
    """Solve puzzle"""
    bots = defaultdict(list)
    commands = {}
    to_give = []

    for command in PUZZLE.input.splitlines():
        if command.startswith('value'):
            match = VALUE.match(command)
            chip, bot = match.groups()
            if add_chip(bots[bot], int(chip)):
                to_give.append(bot)
        else:
            match = GIVE.match(command)
            commands[match.group(1)] = match.group(2, 3)

    while to_give:
        giver = to_give.pop(0)
        if part == 'a' and bots[giver] == [17, 61]:
            _, number = giver.split()
            return number
        low, high = commands[giver]
        if add_chip(bots[high], bots[giver].pop()):
            to_give.append(high)
        if add_chip(bots[low], bots[giver].pop()):
            to_give.append(low)

    total = 1
    for output in range(3):
        total *= bots[f'output {output}'][0]
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
