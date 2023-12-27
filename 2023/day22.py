#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/22
"""
from point import Point3D
from shapes import Linear as Cube
import aoc

PUZZLE = aoc.Puzzle(day=22, year=2023)


class SettledCube(Cube):
    """A cube that has settled, and keeps track of vertical neighbors"""

    def __init__(self, cube, settle_to):
        shift = Point3D(0, 0, 1) * (settle_to - cube.start.z)
        super().__init__(cube.start + shift, cube.end + shift)
        self.resting_on = set()
        self.supports = set()

    def support(self, other):
        """Link the two cubes together"""
        self.supports.add(other)
        other.resting_on.add(self)

    def would_drop(self):
        """Determine how many other cubes would drop if removed"""
        # if len(self.supports) == 0:
        #     return 0
        total = 0
        falling = [self]
        dropped = set()
        while falling:
            cube = falling.pop()
            dropped.add(cube)
            for supported in cube.supports:
                # if len(supported.resting_on) == 1:
                if len(supported.resting_on - dropped) == 0:
                    # was only resting on the cube that's falling
                    falling.append(supported)
                    total += 1
        return total


def settle(cubes):
    """Settle the cubes down"""
    result = []
    for cube in cubes:
        matched = []
        z_max = 0
        for settled in result:
            if settled.overlaps(cube, [0, 1]):
                matched.append(settled)
                z_max = max(z_max, settled.end.z)
        shifted = SettledCube(cube, z_max + 1)
        for match in matched:
            if match.end.z == z_max:
                match.support(shifted)
        result.append(shifted)
    return result


def removable(settled):
    """Determine ho many cubes can be removed safely"""
    total = 0
    for cube in settled:
        # print(cube)
        if len(cube.supports) == 0:
            total += 1
            continue
        total += all(
            len(supported.resting_on) > 1
            for supported in cube.supports
        )
    return total


def solve(part="a"):
    """Solve puzzle"""
    cubes = []
    for line in PUZZLE.input.splitlines():
        start, end = line.split("~")
        start = Point3D(*map(int, start.split(",")))
        end = Point3D(*map(int, end.split(",")))
        cubes.append(Cube(start, end))
    cubes.sort(key=lambda c: c.start.z)
    settled = settle(cubes)
    if part == "a":
        return removable(settled)
    total = 0
    for cube in settled:
        dropped = cube.would_drop()
        # print(dropped, cube)
        total += dropped
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
