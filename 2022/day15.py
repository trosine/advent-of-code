#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/15
"""
import re

import aoc
from point import Point2D

PUZZLE = aoc.Puzzle(day=15, year=2022)
PARSE = re.compile(
    r"Sensor at x=([-0-9]+), y=([-0-9]+): "
    r"closest beacon is at x=([-0-9]+), y=([-0-9]+)"
)


def line_range(line, sensor, distance):
    """Provide a start/end that this sensor can see on the line"""
    adjusted = distance - abs(line - sensor.y)
    if adjusted < 0:
        return None
    result = (sensor.x - adjusted, sensor.x + adjusted)
    return result


def solve(part='a'):
    """Solve puzzle"""
    row = 2000000
    sensors = {}
    beacons = set()
    for line in PUZZLE.input.splitlines():
        groups = tuple(map(int, PARSE.search(line).groups()))
        sensor = Point2D(*groups[:2])
        beacon = Point2D(*groups[2:])
        sensors[sensor] = sensor.distance(beacon)
        beacons.add(beacon)
    line = {}
    if part == "a":
        for sensor, distance in sensors.items():
            adjusted = distance - abs(row - sensor.y)
            for col in range(sensor.x - adjusted, sensor.x + adjusted + 1):
                line[col] = True
        for beacon in beacons:
            if beacon.y == row:
                line.pop(beacon.x, None)
        return len(line)
    grid_max = 4000000
    for line in range(0, grid_max):
        # print(line, end="\r")
        ranges = []
        for sensor, distance in sensors.items():
            range_ = line_range(line, sensor, distance)
            if range_:
                ranges.append(range_)
        end = 0
        for range_ in sorted(ranges):
            if range_[0] > end+1:
                print(f"Found gap at {Point2D(end+1, line)}")
                return grid_max*(end+1) + line
            if range_[1] > end:
                end = range_[1]
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
