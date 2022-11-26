#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/7
"""
import re
from collections import defaultdict
import aoc

PUZZLE = aoc.Puzzle(day=7, year=2017)
PARSE = re.compile(
    r'(?P<name>[a-z]+)\s+'
    r'\((?P<weight>[0-9]+)\)'
    r'(?:\s+->\s+(?P<children>.+))?'
)


class Tower:
    """Tower with sub-towers"""
    name = None
    weight = None
    children = []
    parent = None

    def __init__(self, line):
        match = PARSE.match(line)
        children = match.group('children')
        self.name = match.group('name')
        self.weight = int(match.group('weight'))
        if children:
            self.children = children.split(', ')

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"{self.name} ({self.weight}) {self.children}"

    def tower_weight(self):
        """Return the full weight of tower"""
        weight = self.weight
        for child in self.children:
            weight += child.tower_weight()
        return weight

    def balanced(self):
        """Determine if the tower is balanced"""
        return len(self.child_weights()) == 1

    def misbalanced_child(self):
        """Determine which tower is misbalanced"""
        weights = self.child_weights()
        for children in weights.values():
            if len(children) == 1:
                return children[0]
        return None

    def child_weights(self):
        """Get a dict of {weight: [children]}"""
        weights = defaultdict(list)
        for child in self.children:
            weights[child.tower_weight()].append(child)
        return weights


def solve(part='a'):
    """Solve puzzle"""
    branches = []
    towers = {}
    # parse all towers - the children will be the child names temporarily
    for line in PUZZLE.input.splitlines():
        tower = Tower(line)
        if not tower.children:
            branches.append(tower)
        towers[tower.name] = tower
    # update all towers with references to their parent and children
    for tower in towers.values():
        for offset, child in enumerate(tower.children):
            towers[child].parent = tower
            tower.children[offset] = towers[child]
    # find the root
    tower = branches[0]
    while tower.parent:
        tower = tower.parent
    if part == 'a':
        return tower.name

    # start from root of the tower, and ascend to find the misbalanced tower
    # the problematic tower has its children balanced, where its parent is not
    while not tower.balanced():
        tower = tower.misbalanced_child()
    misbalanced = tower
    tower = tower.parent
    diff = 0
    for weight, children in tower.child_weights().items():
        if len(children) == 1:
            diff += weight
        else:
            diff -= weight
    return misbalanced.weight - diff


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
