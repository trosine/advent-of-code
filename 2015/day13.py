#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/13
"""
import collections
import itertools
# import json
import re
import aoc

PUZZLE = aoc.Puzzle(day=13, year=2015)
PARSE = re.compile(
    r'(?P<person1>\w+) would gain '
    r'(?P<modifier>-?\d+).* to '
    r'(?P<person2>\w+)\.'
    )


def solve(part='a'):
    """Solve puzzle"""
    neighbors = collections.defaultdict(int)
    people = set()
    for line in PUZZLE.input.splitlines():
        line = line.replace(' lose ', ' gain -')
        parsed = PARSE.match(line).groupdict()
        pair = (parsed['person1'], parsed['person2'])
        modifier = int(parsed['modifier'])
        neighbors[pair] += modifier
        neighbors[pair[::-1]] += modifier
        people.add(parsed['person1'])
    if part == 'b':
        for person in people:
            neighbors[('self', person)] = 0
            neighbors[(person, 'self')] = 0
        people.add('self')
    deltas = set()
    # pick a "head" of the of the table
    # since (0, 1, 2, 3); (1, 2, 3, 0); and (2, 3, 0, 1) are identical
    # if this needed to be scaled farther, could also ignore reversed seatings
    head = people.pop()
    for seating in itertools.permutations(people):
        previous = head
        delta = neighbors[(previous, seating[-1])]
        for person in seating:
            delta += neighbors[(previous, person)]
            previous = person
        deltas.add(delta)
    return max(deltas)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
