#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/5
"""
import aoc

PUZZLE = aoc.Puzzle(day=5, year=2015)


def validate_a(word):
    """Is the word nice enough for part A"""
    for disallowed in ('ab', 'cd', 'pq', 'xy'):
        if disallowed in word:
            return False
    last = ''
    doubles = 0
    vowels = 0
    for letter in word:
        vowels += letter in 'aeiou'
        doubles += last + letter == letter + letter
        last = letter
    return doubles >= 1 and vowels >= 3


def validate_b(word):
    """Is the word nice enough for part B"""
    letter_repetition = False
    substring_repetition = False
    word_length = len(word)
    for index, letter in enumerate(word):
        if index+2 < word_length:
            if letter == word[index+2]:
                letter_repetition = True
        if word[index:index+2] in word[index+2:]:
            substring_repetition = True
    return letter_repetition and substring_repetition


def solve(part='a'):
    """Solve puzzle"""
    words = PUZZLE.input.splitlines()
    if part == 'a':
        validator = validate_a
    else:
        validator = validate_b
    return sum([validator(word) for word in words])


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
