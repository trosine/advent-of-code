#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/2

Check passwords against their policy

policy is:
    <min>-<max> <char>: <password
"""
import aoc

PUZZLE = aoc.Puzzle(day=2, year=2020)


def parse_record(line):
    """Parse password record"""
    policy, char, password = line.split(' ')
    minimum, maximum = map(int, policy.split('-'))
    return minimum, maximum, char[0], password


def check_password_count(line):
    """Check password based on count policy"""
    minimum, maximum, char, password = parse_record(line)
    count = password.count(char)
    if minimum <= count <= maximum:
        return True
    return False


def check_password_positions(line):
    """Check passwords based on position policy"""
    first, second, char, password = parse_record(line)
    count = 0
    # print first, second, char, password[first-1], password[second-1]
    if password[first-1] == char:
        count += 1
    if password[second-1] == char:
        count += 1
    return count == 1


def solve(part='a'):
    """Solve puzzle"""
    count = 0
    validation = check_password_count
    if part == 'b':
        validation = check_password_positions
    for line in PUZZLE.input.splitlines():
        if validation(line.strip('\n')):
            count += 1
    return count


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
