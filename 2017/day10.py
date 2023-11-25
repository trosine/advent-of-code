#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/10
"""
from functools import reduce
from operator import xor

import aoc

PUZZLE = aoc.Puzzle(day=10, year=2017)


def rotate(ring, offset):
    """Rotate the list by the given offset"""
    if offset < 0:
        offset = len(ring) + offset
    head = ring[:offset]
    tail = ring[offset:]
    return tail + head


def reverse_subset(ring, length):
    """Reverse the first `length` items in the list"""
    tail = ring[length:]
    head = ring[length-1::-1]
    return head + tail


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        instructions = PUZZLE.input.split(',')
        mapping = int
        append = []
        rounds = 1
    else:
        instructions = list(PUZZLE.input.strip())
        mapping = ord
        append = [17, 31, 73, 47, 23]
        rounds = 64
    instructions = list(map(mapping, instructions))
    instructions.extend(append)

    skip = 0
    offset = 0
    ring = list(range(256))
    for _ in range(rounds):
        for length in instructions:
            if length > 1:
                # reversing a length of 0 or 1 does nothing
                temp = rotate(ring, offset)
                temp = reverse_subset(temp, length)
                ring = rotate(temp, -offset)
            offset = (offset + length + skip) % len(ring)
            skip += 1
    if part == 'a':
        return ring[0] * ring[1]
    hex_string = ''
    for offset in range(0, 256, 16):
        number = reduce(xor, ring[offset:offset+16])
        hex_string += f'{number:02x}'
    return hex_string


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
