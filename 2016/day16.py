#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/16
"""
import aoc

PUZZLE = aoc.Puzzle(day=16, year=2016)


def solve(part='a'):
    """Solve puzzle"""
    disk_fill = 272 if part == 'a' else 35651584
    data = PUZZLE.input.strip()
    table = str.maketrans('01XY', '10YX')
    while len(data) < disk_fill:
        data += '0' + data[::-1].translate(table)
    data = data[:disk_fill]
    while True:
        checksum = ''
        for offset in range(0, len(data)-1, 2):
            if data[offset:offset+2] in ('00', '11'):
                checksum += '1'
            else:
                checksum += '0'
        if len(checksum) % 2 == 1:
            break
        data = checksum
    return checksum


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
