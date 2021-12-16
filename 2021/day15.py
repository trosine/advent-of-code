#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/15
"""
from itertools import product
import operator

import aoc

PUZZLE = aoc.Puzzle(day=15, year=2021)
DIRECTIONS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    )


def neighbors(pos, end):
    """Return a list of neighboring positions"""
    for direction in DIRECTIONS:
        neighbor = tuple(map(operator.add, direction, pos))
        if 0 <= neighbor[0] <= end[0] and 0 <= neighbor[1] <= end[1]:
            yield neighbor


# https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
# modified: there's no need for edge relaxation
# there's also no need to return to a location we've already been to because
# we've already taken the fastest (or equivalent) route to get there
def dijkstra(grid, start, end):
    """Find the shortest path cost from start to end"""
    shortest_paths = {start: 0}  # value is previous node, weight
    current_node = start
    total = len(grid)
    cycle = 0

    while current_node != end:
        cycle += 1
        if cycle % 1000 == 0:
            print(f'{cycle} / {total}', end='\r')
        del grid[current_node]
        # no need to return here
        current_weight = shortest_paths.pop(current_node)

        for neighbor in neighbors(current_node, end):
            if neighbor not in grid:
                # never return to anywhere we've been
                continue
            weight = grid[neighbor] + current_weight
            if neighbor not in shortest_paths:
                shortest_paths[neighbor] = weight

        # find the next node (with the shortest path)
        next_neighbors = {
            node: weight
            for node, weight in shortest_paths.items()
            if node in grid
            }
        current_node = min(next_neighbors, key=lambda x: next_neighbors[x])

    print(cycle)
    return shortest_paths[end]


def solve(part='a'):
    """Solve puzzle"""
    tiles = 1 if part == 'a' else 5
    grid = {}
    data = [
        tuple(map(int, row))
        for row in PUZZLE.input.splitlines()
        ]
    rows_per_tile = len(data)
    cols_per_tile = len(data[0])
    for row, weights in enumerate(data):
        for col, risk in enumerate(weights):
            for tile_row, tile_col in product(range(tiles), repeat=2):
                insert_row = row + tile_row * rows_per_tile
                insert_col = col + tile_col * cols_per_tile
                insert_risk = (risk + tile_row + tile_col) % 9
                if insert_risk == 0:
                    insert_risk = 9
                grid[(insert_row, insert_col)] = insert_risk
    return dijkstra(grid, (0, 0), max(grid.keys()))


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
