#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/11
"""
from math import lcm  # pylint: disable=no-name-in-module
import re

import aoc

PUZZLE = aoc.Puzzle(day=11, year=2022)
PARSER = re.compile(
    r"Monkey (?P<id>\d+):\n"
    r"\s+Starting items: (?P<items>.*)\n"
    r"\s+Operation: new = (?P<operation>(:?old|\d+) [-+*/] (:?old|\d+))\n"
    r"\s+Test: divisible by (?P<test>\d+)\n"
    r"\s+If true: throw to monkey (?P<True>\d+)"
    r"\s+If false: throw to monkey (?P<False>\d+)"
)


def parse_input():
    """Parse the puzzle input"""
    data = PUZZLE.input.split("\n\n")
    monkeys = [None] * len(data)
    for details in data:
        monkey = PARSER.match(details).groupdict()
        monkey["items"] = list(map(int, monkey["items"].split(", ")))
        monkey["operation"] = compile(monkey["operation"], "-", "eval")
        monkey["evals"] = 0
        for key in ("id", "test", "True", "False"):
            monkey[key] = int(monkey[key])
        monkeys[monkey["id"]] = monkey
    return monkeys


def solve(part='a'):
    """Solve puzzle"""
    rounds = 20
    reduction = 3
    if part == 'b':
        rounds = 10000
        reduction = 1
    monkeys = parse_input()
    multiple = lcm(*[monkey["test"] for monkey in monkeys])
    for _ in range(rounds):
        for monkey in monkeys:
            for old in monkey["items"]:
                monkey["evals"] += 1
                new = eval(monkey["operation"])  # pylint: disable=eval-used
                new = new // reduction % multiple
                dest = str(new % monkey["test"] == 0)
                monkeys[monkey[dest]]["items"].append(new)
                del old
            monkey["items"] = []
    evals = sorted([monkey["evals"] for monkey in monkeys], reverse=True)
    return evals[0] * evals[1]


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
