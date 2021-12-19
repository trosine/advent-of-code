#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/19
"""
import collections
from itertools import product, combinations
from math import sin, cos, radians  # pylint: disable=no-name-in-module

from numpy import array, subtract

import aoc

PUZZLE = aoc.Puzzle(day=19, year=2021)
ROTATIONS = []


class Scanner:
    """Scanner details"""

    def __init__(self, data=None):
        if data:
            beacons = data.splitlines()
            self.scanner = beacons.pop(0).split()[2]
            self.beacons = set(
                tuple(map(int, beacon.split(',')))
                for beacon in beacons
                )
        else:
            self.scanner = 'MAP'
            self.beacons = set()

    def __str__(self):
        return f'Scanner<#{self.scanner}, {len(self.beacons)} beacons>'

    def rotate(self, rotation, shift=(0, 0, 0)):
        """Rotate each of the beacons by the rotation matrix, then shift"""
        for beacon in self.beacons:
            yield tuple(rotation @ beacon + shift)


def x_rotations():
    """Generate the possible rotations around the x axis"""
    # cos/sin should each return (-1, 0, 1), but floating point precision using
    # radians means that these actually come out as floats
    for angle in (0, 90, 180, 270):
        rad = radians(angle)
        rcos = round(cos(rad))
        rsin = round(sin(rad))
        yield array((
            (1, 0, 0),
            (0, rcos, -rsin),
            (0, rsin, rcos),
        ))


def y_rotations():
    """Generate the possible rotations around the y axis"""
    for angle in (0, 90, 180, 270):
        rad = radians(angle)
        rcos = round(cos(rad))
        rsin = round(sin(rad))
        yield array((
            (rcos, 0, rsin),
            (0, 1, 0),
            (-rsin, 0, rcos),
        ))


def z_rotations():
    """Generate the possible rotations around the z axis"""
    for angle in (0, 90, 180, 270):
        rad = radians(angle)
        rcos = round(cos(rad))
        rsin = round(sin(rad))
        yield array((
            (rcos, -rsin, 0),
            (rsin, rcos, 0),
            (0, 0, 1),
        ))


def rotations():
    """Generate all possible 3D rotations"""
    prod = product(x_rotations(), y_rotations(), z_rotations())
    yielded = set()
    for x_rot, y_rot, z_rot in prod:
        rotation = z_rot @ y_rot @ x_rot
        hashable = tuple(rotation.flatten())
        if hashable not in yielded:
            yield rotation
            yielded.add(hashable)


def solve(part='a'):
    """Solve puzzle"""
    ROTATIONS.clear()
    ROTATIONS.extend(tuple(rotations()))
    if part == 'a':
        pass
    scanners = [
        Scanner(scanner_data)
        for scanner_data in PUZZLE.input.split('\n\n')
        ]
    queue = collections.deque(scanners)
    grid = Scanner()
    grid.beacons.update(queue.popleft().beacons)
    scanners = []
    while queue:
        print(f'There are {len(queue)} scanners left to fit: {grid}', end='\r')
        scanner = queue.popleft()
        found = False
        for rotation in ROTATIONS:
            rotated = tuple(scanner.rotate(rotation))
            for static, test in product(grid.beacons, rotated):
                shift = subtract(static, test)
                shifted = [
                    tuple(beacon + shift)
                    for beacon in rotated
                    ]
                intersect = grid.beacons.intersection(shifted)
                if len(intersect) >= 12:
                    grid.beacons.update(shifted)
                    scanners.append(shift)
                    found = True
                    break
            if found:
                break
        if not found:
            # try again later
            queue.append(scanner)
    print()
    if part == 'a':
        return len(grid.beacons)
    distances = [
        sum(abs(subtract(*pair)))
        for pair in combinations(scanners, 2)
        ]
    return max(distances)


if __name__ == "__main__":
    # PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
