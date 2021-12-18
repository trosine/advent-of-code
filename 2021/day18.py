#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/18
"""
import itertools
import re

import aoc

PUZZLE = aoc.Puzzle(day=18, year=2021)
PARSE = re.compile(r'(?:\d+|\[)')
EXPLODE_PARSE = re.compile(r'(?:\d+|[\[\]])')


class Snail:
    """A snail number"""

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __add__(self, right):
        # print(f'{self} + {right}')
        new = Snail(self, right)
        new.reduce()
        return new

    def __int__(self):
        return 3 * int(self.left) + 2 * int(self.right)

    def __radd__(self, left):
        return self

    def __str__(self):
        return f'[{self.left},{self.right}]'

    def explode(self):
        """Explode a snailfish number"""
        data = [
            x if x in '[]' else int(x)
            for x in EXPLODE_PARSE.findall(str(self))
            ]
        depth = 0
        for offset, char in enumerate(data):
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
            if depth == 5:
                left, right = data[offset+1:offset+3]
                # print(self)
                # print(data)
                # print(f'o={offset}, l={left}, r={right}')
                for find_offset in range(offset-1, -1, -1):
                    if isinstance(data[find_offset], int):
                        data[find_offset] += left
                        break
                for find_offset in range(offset+4, len(data)):
                    if isinstance(data[find_offset], int):
                        data[find_offset] += right
                        break
                data = iter(data[:offset] + [0] + data[offset+4:])
                next(data)
                snail = self.from_iter(data)
                self.left = snail.left
                self.right = snail.right
                return True
        return False

    @classmethod
    def from_str(cls, string):
        """Create a new Snail from a string"""
        findall = iter(PARSE.findall(string))
        next(findall)  # skip the first '['
        return cls.from_iter(findall)

    @classmethod
    def from_iter(cls, data):
        """Create a new Snail from an iterator"""
        result = cls()
        for attr in ('left', 'right'):
            while True:
                item = next(data)
                if item != ']':
                    break
            if item == '[':
                value = cls.from_iter(data)
            else:
                value = int(item)
            setattr(result, attr, value)
        return result

    def split(self):
        """Split the first large regular number"""
        for attr in ('left', 'right'):
            current = getattr(self, attr)
            if isinstance(current, int):
                if current > 9:
                    value = Snail(current // 2, (current+1) // 2)
                    setattr(self, attr, value)
                    return True
            elif current.split():
                return True
        return False

    def reduce(self):
        """Reduce the Snail number"""
        while True:
            # print(f'reduce: {self}')
            if self.explode():
                continue
            if self.split():
                continue
            break


def solve(part='a'):
    """Solve puzzle"""
    snails = list(map(Snail.from_str, PUZZLE.input.splitlines()))
    if part == 'a':
        return int(sum(snails))
    magnitudes = []
    for pair in itertools.permutations(snails, 2):
        magnitudes.append(int(sum(pair)))
    return max(magnitudes)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
