#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/17
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=17, year=2021)
PARSE = re.compile(r'(-?\d+)')


class Target:
    """The target area"""

    def __init__(self, range_):
        self.x_min, self.x_max, self.y_min, self.y_max = range_
        self.x_range = range(self.x_min, self.x_max + 1)
        self.y_range = range(self.y_min, self.y_max + 1)

    def __contains__(self, location):
        return location[0] in self.x_range and location[1] in self.y_range

    def possible_x_values(self):
        """Generate a list of valid X values"""
        for test_x in range(1, self.x_max + 1):
            distance = 0
            for current_velocity in range(test_x, -1, -1):
                distance += current_velocity
                if distance in self.x_range:
                    yield test_x
                    break
                if distance > self.x_max:
                    break


def digit_sum(number):
    """Return the sum of all numbers from 1..number"""
    return number * (number + 1) // 2


def solve(part='a'):
    """Solve puzzle"""
    target = Target(map(int, PARSE.findall(PUZZLE.input)))
    max_height = 0
    valid_velocities = 0
    for test_x in target.possible_x_values():
        for test_y in range(target.y_min, abs(target.y_min) + 1):
            velocity = [test_x, test_y]
            # print(velocity, end='\r')
            pos = [0, 0]
            while pos[0] <= target.x_max and pos[1] >= target.y_min:
                pos[0] += velocity[0]
                pos[1] += velocity[1]
                if pos in target:
                    max_height = max(max_height, digit_sum(test_y))
                    valid_velocities += 1
                    break
                velocity[0] -= int(velocity[0] > 0)
                velocity[1] -= 1
            if pos[0] > target.x_max and pos[1] > target.y_max:
                # overshot, move to next x value
                break
    if part == 'a':
        return max_height
    return valid_velocities


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
