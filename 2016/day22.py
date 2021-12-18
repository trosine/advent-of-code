#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/22
"""
import collections
import itertools
import operator
import re

import aoc

NEIGHBORS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    )
PUZZLE = aoc.Puzzle(day=22, year=2016)
PARSE_DF = re.compile(r'-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T')

Node = collections.namedtuple('Node', ('size', 'used'))
GridState = collections.namedtuple('GridState', ('goal', 'empty'))


def neighbors(pos):
    """Return possible neighbor locations"""
    for neighbor in NEIGHBORS:
        yield tuple(map(operator.add, pos, neighbor))


def search(grid, state):
    """Return the fewest moves to obtain the data"""
    queue = collections.deque([state])
    shortest_paths = {state: 0}

    while queue:
        current = queue.popleft()
        steps = shortest_paths[current] + 1

        for neighbor in neighbors(current.empty):
            if neighbor not in grid:
                continue
            if grid[neighbor].used > grid[current.empty].size:
                continue

            if neighbor == current.goal:
                state = GridState(goal=current.empty, empty=current.goal)
                state = GridState(*current[::-1])
            else:
                state = GridState(goal=current.goal, empty=neighbor)

            if state.goal == (0, 0):
                return steps
            if state not in shortest_paths:
                shortest_paths[state] = steps
                queue.append(state)


def valid_pairs(grid):
    """Find the possible combinations of valid pairs"""
    valid = 0
    for src, dst in itertools.permutations(grid.keys(), 2):
        source = grid[src]
        dest = grid[dst]
        if not source.used or src == dst:
            continue
        if (source.used + dest.used) < dest.size:
            valid += 1
    return valid


def solve(part='a'):
    """Solve puzzle"""
    grid = {}
    for line in PUZZLE.input.splitlines():
        if line[0] != '/':
            continue
        groups = tuple(map(int, PARSE_DF.search(line).groups()))
        location = groups[:2]
        node = Node(*groups[2:])
        if node.used == 0:
            empty_node = location
        grid[location] = node
    if part == 'a':
        return valid_pairs(grid)
    max_x = max(x for x, _ in grid)
    return search(grid, GridState(goal=(max_x, 0), empty=empty_node))


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
