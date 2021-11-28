#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/7
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=7, year=2016)


def check_abba(word):
    """Checks for ABBA sequences"""
    if word[0] == word[1]:
        return False
    return word[0] == word[3] and word[1] == word[2]


def validate_tls(line):
    """Validate an IPv7 address using ruleset A"""
    hypernet = False
    tls = False
    for offset in range(len(line)-3):
        if line[offset] in '[]':
            hypernet = not hypernet
        abba = check_abba(line[offset:offset+4])
        if hypernet and abba:
            return False
        if abba:
            tls = True
    return tls


def validate_ssl(line):
    """Validate an IPv7 address using ruleset b"""
    networks = [[], []]
    for offset, network in enumerate(re.split(r'[\[\]]', line)):
        networks[offset % 2].append(network)
    supernets = '::'.join(networks[0])
    hypernets = '::'.join(networks[1])
    for offset, char in enumerate(supernets[:-2]):
        if supernets[offset+1] != char and supernets[offset+2] == char:
            bab = supernets[offset+1] + char + supernets[offset+1]
            if bab in hypernets:
                return True
    return False


def solve(part='a'):
    """Solve puzzle"""
    validator = validate_tls if part == 'a' else validate_ssl
    support = 0
    for line in PUZZLE.input.splitlines():
        support += validator(line)
    return support


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
