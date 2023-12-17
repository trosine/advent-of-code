#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/14
"""
import numpy
import aoc

PUZZLE = aoc.Puzzle(day=14, year=2023)


def tilt(platform, direction):
    """Tilt the platform and let smooth rocks roll"""
    view = platform
    if direction == "n":
        view = platform.T
    elif direction == "s":
        view = platform[::-1].T
    elif direction == "e":
        view = platform[:, ::-1]

    for row in view:
        pivot = 0
        while pivot < len(row):
            if row[pivot] in "#O":
                pivot += 1
                continue
            for offset in range(pivot+1, len(row)):
                if row[offset] == "#":
                    pivot = offset
                    break
                if row[offset] == "O":
                    row[pivot], row[offset] = row[offset], row[pivot]
                    pivot += 1
            pivot += 1


def load(platform):
    """Determine the load of the platform on the north side"""
    size = len(platform)
    total = 0
    for row, values in enumerate(platform):
        total += sum(values == "O") * (size - row)
    return total


def solve(part='a'):
    """Solve puzzle"""
    count = 1
    cycle = "n"
    if part == 'b':
        count = 1000000000
        cycle = "nwse"
    platform = numpy.array([list(x) for x in PUZZLE.input.splitlines()])
    history = []
    frequency = None
    for iteration in range(1, count+1):
        for direction in cycle:
            tilt(platform, direction)
        history.append(load(platform))
        if iteration < 20:
            continue  # need to wait until there's at least enough to compare
        if len(history) > 50:
            history.pop(0)
        last = history[-10:]
        for offset in range(len(history)-10, 10, -1):
            prev = history[offset-10:offset]
            if last == prev:
                frequency = len(history) - offset
                break
        if frequency is not None:
            break

    if part == "a":
        return history[-1]
    while len(history) > frequency:
        history.pop(0)
    # rotate history, to match modulus below
    #   if there are 0 to go, we want the load we most recently calculated
    history.insert(0, history.pop())
    print(history)
    remaining = count - iteration
    remaining = remaining % frequency
    print(f"i={iteration}, freq={frequency}, to-go={remaining}")
    return history[remaining]


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
