#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/23
"""
import aoc

PUZZLE = aoc.Puzzle(day=23, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    cups = list(map(int, PUZZLE.input.strip()))
    if part == 'a':
        moves = 100
    else:
        cups.extend(range(10, 1000001))
        moves = 10000000
    total_cups = len(cups)
    for move in range(moves):
        if move % 10000 == 0:
            print(move)
        index = 1
        removed = [cups.pop(index) for _ in range(3)]
        destination = (cups[0] - 1) % total_cups or total_cups
        while destination in removed:
            destination = (destination - 1) % total_cups or total_cups
        index = cups.index(destination) + 1
        if index == len(cups):
            cups.extend(removed)
        else:
            for offset, cup in enumerate(removed):
                cups.insert((index + offset) % len(cups), cup)
        cups.append(cups.pop(0))
    if part == 'a':
        while cups[8] != 1:
            cups.append(cups.pop(0))
        return ''.join(map(str, cups[:-1]))
    index = cups.index(1) + 1
    product = 1
    for index in range(index, index+2):
        product *= cups[index % len(cups)]
    return product


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
