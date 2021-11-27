#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/5
"""
import functools
import hashlib

import aoc

PUZZLE = aoc.Puzzle(day=5, year=2016)


@functools.cache
def md5_hash(data):
    """Efficiently create a hash object"""
    if len(data) > 1:
        new_hash = md5_hash(data[:-1]).copy()
        new_hash.update(data[-1:])
    else:
        new_hash = hashlib.md5(data)
    return new_hash


def solve(part='a'):
    """Solve puzzle"""
    password = ' ' * 8
    door = PUZZLE.input.encode()
    number = 0
    pos = 0
    while True:
        md5 = md5_hash(door + str(number).encode())
        hexdigest = md5.hexdigest()
        if hexdigest.startswith('00000'):
            if part == 'a':
                password = password[:pos] \
                    + hexdigest[5] \
                    + password[pos+1:]
                pos += 1
            else:
                if hexdigest[5] < '8':
                    pos = int(hexdigest[5])
                    if password[pos] == ' ':
                        password = password[:pos] \
                            + hexdigest[6] \
                            + password[pos+1:]
            print(f'"{password}"', end='\r')
            if ' ' not in password:
                break
        number += 1
    print()
    return password


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
