#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/9
"""
import aoc

PUZZLE = aoc.Puzzle(day=9, year=2023)


def differences(data):
    """Return a list of all differences"""
    result = []
    for index, value in enumerate(data[:len(data)-1], 1):
        result.append(data[index] - value)
    return result


def solve(part='a'):
    """Solve puzzle"""
    total = 0
    for line in PUZZLE.input.splitlines():
        sequences = [[int(x) for x in line.split()]]
        # this uses python's implicit conversion of 0=>False, others=>True
        while any(sequences[-1]):
            sequences.append(differences(sequences[-1]))

        first = 0
        last = 0
        sequences = sequences[::-1]
        for sequence in sequences[1:]:
            last = sequence[-1] + last
            first = sequence[0] - first
            # no need to modify the sequences - only the final values matter

        if part == "a":
            total += last
        else:
            total += first

    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
