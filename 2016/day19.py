#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/19
"""
import aoc

PUZZLE = aoc.Puzzle(day=19, year=2016)


class Elf:
    """Represents an elf with a pointer to the elf at thier left"""
    # pylint: disable=too-few-public-methods

    def __init__(self, number, left=None):
        self.number = number
        self.left = left

    def steal(self, part, elves):
        """Steal a present"""
        if part == 'a':
            self.left = self.left.left
        else:
            steal_from = elves // 2 - 1
            steal_5 = steal_from // 5
            steal_rem = steal_from % 5
            right_elf = self
            for _ in range(steal_5):
                right_elf = self.left.left.left.left.left
            for _ in range(steal_rem):
                right_elf = self.left
            # stolen = right_elf.left.number
            # print(f'{self.number}/{elves} - stealing from {stolen}')
            right_elf.left = right_elf.left.left
        return elves - 1


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        pass
    elves = int(PUZZLE.input)
    # elves = 5
    last = Elf(elves)
    previous = last
    for elf in range(elves - 1, 0, -1):
        new = Elf(elf, previous)
        previous = new
    last.left = previous
    # previous == Elf(1) at this point
    rounds = 0
    while previous.left != previous:
        if rounds % 100 == 0:
            print(rounds, end='\r')
        elves = previous.steal(part, elves)
        previous = previous.left
        rounds += 1
    return previous.number


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
