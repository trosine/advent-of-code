#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/4
"""
import itertools
import re
import string

import aoc

PUZZLE = aoc.Puzzle(day=4, year=2016)


def checksum(encrypted):
    """Generate a room's checksum"""
    groups = [
        (-len(list(group)), letter)
        for letter, group in itertools.groupby(sorted(encrypted))
        if letter != '-'
        ]
    groups.sort()
    letters = ''.join(letter for count, letter in groups)
    return letters[:5]


# based on https://blog.finxter.com/how-to-use-rot13-in-python/
def decrypt(encrypted, sector):
    """Decrypt a room name"""
    rotations = int(sector) % 26
    key = string.ascii_lowercase
    val = key[rotations:] + key[:rotations]
    transform = dict(zip(key, val))
    return ''.join(transform.get(char, ' ') for char in encrypted)


def solve(part='a'):
    """Solve puzzle"""
    parser = re.compile(
        r'(?P<encrypted>[a-z-]+)-'
        r'(?P<sector>\d+)'
        r'\[(?P<checksum>[a-z]+)\]'
        )
    valid_sum = 0
    for room in PUZZLE.input.splitlines():
        room = parser.match(room)
        actual_sum = checksum(room['encrypted'])
        if actual_sum != room['checksum']:
            continue
        if part == 'a':
            valid_sum += int(room['sector'])
            continue
        decrypted = decrypt(room['encrypted'], room['sector'])
        if 'northpole object storage' == decrypted:
            return room['sector']
    return valid_sum


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
