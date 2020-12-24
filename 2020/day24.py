#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/24
"""
import collections
import itertools
import operator
import re
import aoc

PUZZLE = aoc.Puzzle(day=24, year=2020)
MOVES = re.compile(r'(n[ew]|s[ew]|e|w)')
VECTORS = {
    'e': (0, 1),
    'w': (0, -1),
    'se': (-1, 0),
    'sw': (-1, -1),
    'ne': (1, 1),
    'nw': (1, 0),
    }


# http://roguebasin.roguelikedevelopment.org/index.php?title=Hexagonal_Tiles#Coordinate_systems_with_a_hex_grid
# I think the input will work with the skewed axis coordinates.
# False == white, True == black
def solve(part='a'):
    """Solve puzzle"""
    tiles = collections.defaultdict(bool)
    for line in PUZZLE.input.splitlines():
        pos = (0, 0)
        for move in MOVES.findall(line):
            pos = tuple(map(operator.add, pos, VECTORS[move]))
        # print(f'{pos} -- {line}')
        tiles[pos] = not tiles[pos]
    if part == 'a':
        return sum(tiles.values())
    for day in range(100):
        new_tiles = collections.defaultdict(bool)
        xvalues = [pos[0] for pos in tiles]
        yvalues = [pos[1] for pos in tiles]
        x_range = range(min(xvalues)-1, max(xvalues)+2)
        y_range = range(min(yvalues)-1, max(yvalues)+2)
        for pos in itertools.product(x_range, y_range):
            black = 0
            for neighbor in VECTORS.values():
                npos = tuple(map(operator.add, pos, neighbor))
                black += tiles[npos]
            if tiles[pos]:
                if black in (1, 2):
                    new_tiles[pos] = True
            else:
                if black == 2:
                    new_tiles[pos] = True
        tiles = new_tiles
        # print(f'Day {day+1}: {sum(tiles.values())}')
    del day
    return sum(tiles.values())


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
