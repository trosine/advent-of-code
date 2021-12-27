#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/24
"""
import collections
import itertools

import aoc

PUZZLE = aoc.Puzzle(day=24, year=2016)


class Point(collections.namedtuple('PointT', ('x', 'y'))):
    """A two-dimensional point in space"""

    def __add__(self, other):
        if not isinstance(other, tuple):
            return super().__add__(other)
        other = Point(*other)
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return str(tuple(self))

    def orthogonals(self):
        """Provide a list of neighbors directly next to the point"""
        for neighbor in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            yield self + neighbor


def find_edges(grid, edges, name, start, destinations):
    """Find the edges from the start to each of the other destinations"""
    queue = collections.deque([start])
    depth = {start: 0}
    found = set([name])
    how_many = len(destinations)
    while queue:
        current = queue.popleft()
        new_depth = depth[current] + 1
        for step in current.orthogonals():
            if step not in grid:
                continue
            if step in depth:
                continue
            reached = grid[step]
            depth[step] = new_depth
            if reached in destinations:
                found.add(reached)
                edges[(name, reached)] = new_depth
                edges[(reached, name)] = new_depth
                if len(found) == how_many:
                    return
            queue.append(step)


def parse_input(data):
    """Parse the input data"""
    destinations = {}
    grid = {}
    for row, line in enumerate(data.splitlines()):
        for col, char in enumerate(line):
            if char == '#':
                continue
            if char in '0123456789':
                destinations[char] = Point(row, col)
            grid[Point(row, col)] = char
    edges = {}
    for name, start in destinations.items():
        find_edges(grid, edges, name, start, destinations)
    return edges, destinations


def solve(part='a'):
    """Solve puzzle"""
    edges, destinations = parse_input(PUZZLE.input)

    unvisited = [d for d in destinations if d != '0']
    totals = []
    for path in itertools.permutations(unvisited):
        full_path = ('0',) + path
        if part == 'b':
            full_path = full_path + ('0',)
        total = 0
        for offset in range(len(full_path)-1):
            pair = tuple(full_path[offset:offset+2])
            total += edges[pair]
        totals.append(total)
    return min(totals)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
