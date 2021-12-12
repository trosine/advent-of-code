#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/12
"""
from collections import Counter, defaultdict, deque

import aoc

PUZZLE = aoc.Puzzle(day=12, year=2021)


def valid_path(path, part='a'):
    """Determines if a path is valid or not"""
    neighbor = path[-1]
    if neighbor.islower() and neighbor in path[:-1]:
        if part == 'a':
            return False  # small cave already visited
        counter = Counter(path)
        if counter[neighbor] > 2:
            return False
        for cave, count in counter.items():
            if cave.islower() and cave != neighbor and count > 1:
                return False  # two small caves visited twice
    return True


def solve(part='a'):
    """Solve puzzle"""
    links = defaultdict(list)
    for link in PUZZLE.input.splitlines():
        caves = link.split('-')
        links[caves[0]].append(caves[1])
        links[caves[1]].append(caves[0])
    queue = deque([['start']])
    paths = 0  # or use a set()
    while queue:
        path = queue.popleft()
        for neighbor in links[path[-1]]:
            # print(f'Checking {path} + {neighbor}')
            if neighbor == 'end':
                paths += 1
                continue
            if neighbor == 'start':
                continue  # can't revisit start
            new_path = path.copy()
            new_path.append(neighbor)
            if valid_path(new_path, part):
                queue.append(new_path)
    return paths


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
