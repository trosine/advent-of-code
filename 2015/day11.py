#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/11
"""
import re
import string
import aoc

PUZZLE = aoc.Puzzle(day=11, year=2015)
PAIRS = re.compile(r'((\w)\2)')


def increment_string(password):
    """Increment the password - rolling z over to a"""
    if password.endswith('z'):
        return increment_string(password[:-1]) + 'a'
    return password[:-1] + chr(ord(password[-1])+1)


def verify(password):
    """Verify a simple password"""
    for invalid in 'iol':
        if invalid in password:
            return False
    if len(PAIRS.findall(password)) < 2:
        return False
    straight = False
    for index in range(len(password)-2):
        if password[index:index+3] in string.ascii_lowercase:
            straight = True
    return straight


def solve(part='a'):
    """Solve puzzle"""
    password = PUZZLE.input.strip()
    if part == 'b':
        password = solve()
    while True:
        password = increment_string(password)
        if verify(password):
            return password
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
