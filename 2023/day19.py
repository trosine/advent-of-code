#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/19
"""
import operator
import re
import aoc

PUZZLE = aoc.Puzzle(day=19, year=2023)
OPERATORS = {
    ">": operator.gt,
    "<": operator.lt,
    None: lambda x, y: True,
}
RULE = re.compile(
    r"((?P<cat>[xmas])(?P<op>[<>])(?P<value>\d+):)?(?P<dest>\w+)$"
)


class Rule:
    """Manages and processes workflow rules"""

    category = None
    operator = OPERATORS[None]
    value = None

    def __init__(self, text):
        parsed = RULE.match(text).groupdict()
        self.text = text
        self.dest = parsed["dest"]
        self.operator = OPERATORS[parsed["op"]]
        if parsed["op"]:
            self.value = int(parsed["value"])
            self.category = parsed["cat"]
            if parsed["op"] == ">":
                self.split = self.split_gt
            else:
                self.split = self.split_lt

    def __str__(self):
        return self.text

    def check(self, part):
        """Returns the destination if the rule matches"""
        if self.operator(part.get(self.category), self.value):
            return self.dest
        return None

    def split_gt(self, part):
        """Split the part's combinations for > rules"""
        current = part[self.category]
        yield range(self.value+1, current.stop)
        yield range(current.start, self.value+1)

    def split_lt(self, part):
        """Split the part's combinations for < rules"""
        current = part[self.category]
        yield range(current.start, self.value)
        yield range(self.value, current.stop)


def parse_input():
    """Parse this puzzle's input"""
    workflows = {}
    parts = []
    for line in PUZZLE.input.splitlines():
        if line == "":
            continue
        if match := re.match(r"(\w+){(.*)}", line):
            flow, rules = match.groups()
            workflows[flow] = [Rule(rule) for rule in rules.split(",")]
            continue
        part = {}
        for cat, value in re.findall(r"([xmas])=(\d+)", line):
            part[cat] = int(value)
        parts.append(part)
    return workflows, parts


def part_score(workflows, part):
    """Run the part through the workflows"""
    flow = "in"
    while flow not in "RA":
        for rule in workflows[flow]:
            flow = rule.check(part)
            if flow:
                break
            # since the last rule of each is a catch-all
            # flow will always be defined
    if flow == "A":
        return sum(part.values())
    return 0


def solve(part="a"):
    """Solve puzzle"""
    workflows, parts = parse_input()
    if part == "a":
        return sum(part_score(workflows, p) for p in parts)
    queue = [[{x: range(1, 4001) for x in "xmas"}, "in"]]
    total = 0
    while queue:
        combo, dest = queue.pop()
        if dest == "R":
            continue
        if dest == "A":
            product = 1
            for value in combo.values():
                product *= len(value)
            total += product
            continue
        # split the combinations apart, with the conditional rules
        for rule in workflows[dest][:-1]:
            new_combo = combo.copy()
            good, bad = rule.split(combo)
            new_combo[rule.category] = good
            combo[rule.category] = bad
            queue.append([new_combo, rule.dest])
        # add the catch-all rule
        queue.append([combo, workflows[dest][-1].dest])
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
