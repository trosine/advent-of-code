#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/11
"""
import copy
import itertools
import aoc

PUZZLE = aoc.Puzzle(day=11, year=2020)


def nearest(layout, row, col, direction, search):
    """Find the nearest seat in a direction"""
    row += direction[0]
    col += direction[1]
    if row < 0 or col < 0:
        return ' '
    try:
        spot = layout[row][col]
    except IndexError:
        return ' '
    if spot == '.' and search:
        return nearest(layout, row, col, direction, search)
    return spot


def count_neighbors(layout, row, col, search):
    """Count the number of filled seats near row, col"""
    total = 0
    for direction in itertools.product(range(-1, 2), repeat=2):
        if direction == (0, 0):
            # don't count myself
            continue
        total += nearest(layout, row, col, direction, search) == '#'
    return total


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        tolerance = 4
        search = False
    else:
        tolerance = 5
        search = True
    layout = list(map(list, PUZZLE.input.splitlines()))
    new_layout = copy.deepcopy(layout)
    rows = range(len(layout))
    cols = range(len(layout[0]))
    while True:
        for row, col in itertools.product(rows, cols):
            if layout[row][col] == '.':
                continue
            neighbors = count_neighbors(layout, row, col, search)
            if layout[row][col] == 'L' and neighbors == 0:
                new_layout[row][col] = '#'
            elif layout[row][col] == '#' and neighbors >= tolerance:
                new_layout[row][col] = 'L'
            else:
                new_layout[row][col] = layout[row][col]
        # for row in new_layout:
        #     print(''.join(row))
        # print()
        # input()
        if new_layout == layout:
            break
        layout, new_layout = new_layout, layout
    total = 0
    for row in layout:
        total += row.count('#')
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
