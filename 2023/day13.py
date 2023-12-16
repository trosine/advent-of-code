#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/13
"""
import aoc
import numpy

PUZZLE = aoc.Puzzle(day=13, year=2023)


def find_mirrors(image, smudge=0):
    """Find horizontal mirrors in the image"""
    end = len(image)
    for center in range(end-1):  # -1: center cannot be "below" the image
        differences = 0
        # loop from the center to the closest edge
        for offset in range(min(end-center-1, center+1)):
            left = center - offset
            right = center + offset + 1
            # with numpy.array, this is an element-wise comparison
            differences += sum(image[left] != image[right])
            if differences > smudge:
                break
        if differences == smudge:
            return center
    return None


def solve(part='a'):
    """Solve puzzle"""
    smudge = 0
    if part == 'b':
        smudge = 1
    summary = 0
    for image in PUZZLE.input.split("\n\n"):
        image = numpy.array([list(x) for x in image.splitlines()])
        center = find_mirrors(image, smudge)
        if center is not None:
            summary += 100 * (center + 1)
        center = find_mirrors(image.T, smudge)
        if center is not None:
            summary += center + 1
    return summary


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
