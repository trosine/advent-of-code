#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/8

 AAAA    ....    AAAA    AAAA    ....
B    C  .    C  .    C  .    C  B    C
B    C  .    C  .    C  .    C  B    C
 ....    ....    DDDD    DDDD    DDDD
E    F  .    F  E    .  .    F  .    F
E    F  .    F  E    .  .    F  .    F
 GGGG    ....    GGGG    GGGG    ....

 AAAA    AAAA    AAAA    AAAA    AAAA
B    .  B    .  .    C  B    C  B    C
B    .  B    .  .    C  B    C  B    C
 DDDD    DDDD    ....    DDDD    DDDD
.    F  E    F  .    F  E    F  .    F
.    F  E    F  .    F  E    F  .    F
 GGGG    GGGG    ....    GGGG    GGGG
"""
import itertools
import aoc

PUZZLE = aoc.Puzzle(day=8, year=2021)
# key=segments lit, value=digit
LEN_DIGIT = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
    }
# these particular segments show up a unique number of times when displaying
# all 10 digits
SEGMENT_FREQUENCY = {
    4: 'E',
    6: 'B',
    9: 'F',
    }
# key=which segments are lit, value=digit
DIGITS = {
    'ABCEFG': 0,
    'CF': 1,
    'ACDEG': 2,
    'ACDFG': 3,
    'BCDF': 4,
    'ABDFG': 5,
    'ABDEFG': 6,
    'ACF': 7,
    'ABCDEFG': 8,
    'ABCDFG': 9,
    }


def get_unique(superset, known):
    """Get the item in the superset that is not in known"""
    for char in superset:
        if char not in known:
            return char
    raise ValueError(f'no unique char in {superset} vs {known}')


def solve(part='a'):
    """Solve puzzle"""
    part_a = 0
    part_b = 0
    for line in PUZZLE.input.splitlines():
        signals, display = line.split('|')
        segment_map = {}
        for segment, group in itertools.groupby(sorted(signals)):
            group_len = len(list(group))
            if group_len in SEGMENT_FREQUENCY:
                segment_map[segment] = SEGMENT_FREQUENCY[group_len]
        signals = sorted(signals.split(), key=len)
        segment_map[get_unique(signals[1], signals[0])] = 'A'
        segment_map[get_unique(signals[0], segment_map.keys())] = 'C'
        segment_map[get_unique(signals[2], segment_map.keys())] = 'D'
        segment_map[get_unique(signals[9], segment_map.keys())] = 'G'

        output = 0
        for digit in display.split():
            if len(digit) in LEN_DIGIT:
                part_a += 1
            real_digit = ''.join(sorted(segment_map[x] for x in digit))
            output = output * 10 + DIGITS[real_digit]
        part_b += output
    if part == 'a':
        return part_a
    return part_b


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
