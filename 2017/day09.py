#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/9
"""
import aoc

PUZZLE = aoc.Puzzle(day=9, year=2017)


class Group:
    """Holds the different groups within the stream of characters"""

    def __init__(self, depth):
        self.groups = []
        self.garbage = []
        self.depth = depth

    def sum_depths(self):
        """Recursively add the depths of the various groups"""
        total = self.depth
        for group in self.groups:
            total += group.sum_depths()
        return total

    def count_garbage(self):
        """Recursively count the non-cancelled characters"""
        total = 0
        for string in self.garbage:
            total += len(string)
        for group in self.groups:
            total += group.count_garbage()
        return total


def parse_input(data):
    """Parse puzzle input into groups"""
    groups = [Group(1)]
    current = 0
    offset = 1
    while offset < len(data):
        if data[offset] == '<':
            # read garbage until '>'
            offset += 1
            garbage = []
            while data[offset] != '>':
                if data[offset] == '!':
                    offset += 2
                    continue
                garbage += data[offset]
                offset += 1
            groups[current].garbage.append(''.join(garbage))
        elif data[offset] == ',':
            # skip comma delimiters between groups or garbage
            pass
        elif data[offset] == '{':
            # new group; add to groups and the current group's children
            groups[current].groups.append(Group(current+2))
            groups.append(groups[current].groups[-1])
            current += 1
        elif data[offset] == '}':
            # end of group; trim the stack
            final = groups.pop(-1)
            current -= 1
        offset += 1
    return final


def solve(part='a'):
    """Solve puzzle"""
    root = parse_input(PUZZLE.input)
    if part == 'a':
        return root.sum_depths()
    return root.count_garbage()


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
