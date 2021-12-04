#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/3
"""
import operator

import aoc

PUZZLE = aoc.Puzzle(day=3, year=2021)


def calc_common(data):
    """Calculate the most common bits in data"""
    lines = len(data)
    sums = map(int, data[0])
    for number in data[1:]:
        bits = map(int, number)
        sums = map(operator.add, sums, bits)
    most_common = [1 if x >= lines/2 else 0 for x in sums]
    least_common = [1-x for x in most_common]
    return ''.join(map(str, most_common)), ''.join(map(str, least_common))


def get_rating(data, use_most=True):
    """Get oxygen rating from data"""
    bit = 0
    while len(data) > 1:
        most, least = calc_common(data)
        filter_value = most[bit] if use_most else least[bit]
        data = list(filter(lambda x: x[bit] == filter_value, data))
        bit += 1
    return int(data[0], 2)


def solve(part='a'):
    """Solve puzzle"""
    data = PUZZLE.input.splitlines()
    if part == 'a':
        gamma, epsilon = map(lambda x: int(x, 2), calc_common(data))
        return gamma * epsilon
    oxygen = get_rating(data)
    co2 = get_rating(data, use_most=False)
    return oxygen * co2


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
