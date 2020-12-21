#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/20
"""
import collections
import itertools
import re
import aoc

PUZZLE = aoc.Puzzle(day=20, year=2020)
MONSTER = (
    '                  #',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #',
    )
MONSTER_SIZE = (len(MONSTER), max(len(x) for x in MONSTER))
MONSTER_ROUGHNESS = sum(x.count('#') for x in MONSTER)
MONSTER = tuple(re.compile(x.replace(' ', '.')) for x in MONSTER)


class Tile():
    """An image tile"""

    num = 0
    top = property(lambda self: self.image[0])
    right = property(lambda self: ''.join([x[-1] for x in self.image]))
    bottom = property(lambda self: self.image[-1])
    left = property(lambda self: ''.join([x[0] for x in self.image]))

    def __init__(self, tile_data):
        lines = tile_data.splitlines()
        if 'Tile' in lines[0]:
            self.num = int(lines.pop(0)[5:-1])
        self.image = lines

    @property
    def sides(self):
        """A list of each of the sides - T,R,B,L"""
        return self.top, self.right, self.bottom, self.left

    def mirror(self):
        """Mirrors the tile left<->right"""
        self.image = [x[::-1] for x in self.image]

    def flip(self):
        """Flips the tile top<->bottom"""
        self.image.reverse()

    def rotate_right(self):
        """Rotate the tile clockwise"""
        size = len(self.image)
        new = [[None]*size for x in range(size)]
        # pylint: disable=invalid-name
        for x, y in itertools.product(range(size), repeat=2):
            new[y][size-1-x] = self.image[x][y]
        self.image = [''.join(x) for x in new]

    def orient(self, target, face):
        """Orient this tile so the target side faces the desired face"""
        rotations = {
            'top': (self.left, self.right),
            'left': (self.top, self.bottom),
            }
        if target in rotations[face] or target[::-1] in rotations[face]:
            self.rotate_right()
        if target[::-1] in (self.top, self.bottom):
            self.mirror()
        if target[::-1] in (self.left, self.right):
            self.flip()
        if target == self.bottom:
            self.flip()
        if target == self.right:
            self.mirror()

    def search(self):
        """Find sea monsters in the tile image"""
        size = len(self.image)
        monsters = 0
        for row in range(size+1-MONSTER_SIZE[0]):
            for col in range(size+1-MONSTER_SIZE[1]):
                for offset, test in enumerate(MONSTER):
                    if not test.match(self.image[row+offset][col:]):
                        break
                else:
                    monsters += 1
        # print(f'Searched until {row,col}, {MONSTER_SIZE}')
        return monsters

    def water_roughness(self):
        """Determine how rough the water is, minus sea monsters"""
        roughness = sum([x.count('#') for x in self.image])
        orientations = [
            int,  # a noop from the perspective of the tile
            self.flip,
            self.mirror,
            self.flip,
            self.rotate_right,
            self.flip,
            self.mirror,
            self.flip,
            ]
        for orientation in orientations:
            # print(f'Testing {orientation}...')
            orientation()
            sea_monsters = self.search()
            if sea_monsters != 0:
                break
        return roughness - sea_monsters * MONSTER_ROUGHNESS

    def __str__(self):
        return ' '.join([f'{self.num}:'] + list(self.sides))


def solve(part='a'):
    """Solve puzzle"""
    tiles = list(map(Tile, PUZZLE.input.split('\n\n')))
    # find how many matches there are per side (either orientation)
    # and build a way to find the tiles matching a given side
    matches = collections.Counter()
    finder = collections.defaultdict(list)
    for tile in tiles:
        for side in tile.sides:
            matches[side] += 1
            matches[side[::-1]] += 1
            finder[side].append(tile)
            finder[side[::-1]].append(tile)
    # find the corners and multiply their ids (corners=6, edges=7, interior=8)
    product = 1
    for tile in tiles:
        total = 0
        for side in tile.sides:
            total += matches[side]
        if total == 6:
            # print(tile)
            corner = tile
            product *= tile.num
    if part == 'a':
        return product

    if matches[corner.top] == 2:
        corner.flip()
    if matches[corner.left] == 2:
        corner.mirror()
    tile_map = build_map(corner, finder)
    lines = []
    for row in tile_map:
        for index in range(1, len(corner.image)-1):
            lines.append(''.join([x.image[index][1:-1] for x in row]))
    tile = Tile('\n'.join(lines))
    return tile.water_roughness()


def build_map(corner, finder):
    """Build the map of tiles"""
    tile_map = [[] for _ in range(12)]
    for row, col in itertools.product(range(12), repeat=2):
        if (row, col) == (0, 0):
            tile_map[row].append(corner)
            continue
        if col == 0:
            neighbor = tile_map[row-1][col]
            target = neighbor.bottom
            face = 'top'
        else:
            neighbor = tile_map[row][col-1]
            target = neighbor.right
            face = 'left'
        for tile in finder[target]:
            if tile.num != neighbor.num:
                break
        # pylint: disable=undefined-loop-variable
        tile.orient(target, face)
        tile_map[row].append(tile)
    return tile_map


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
