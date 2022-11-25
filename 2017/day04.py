#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/4
"""
import aoc

PUZZLE = aoc.Puzzle(day=4, year=2017)


def anagram(word):
    """Sort the characters to test anagrams"""
    return ''.join(sorted(word))


def solve(part='a'):
    """Solve puzzle"""
    sanitize = str
    if part == 'b':
        sanitize = anagram
    total = 0
    for line in PUZZLE.input.splitlines():
        words = set()
        valid = True
        for word in map(sanitize, line.split()):
            if word in words:
                valid = False
                break
            words.add(word)
        if valid:
            total += 1
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
