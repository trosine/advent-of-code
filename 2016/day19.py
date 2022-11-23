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

    def steal(self, elves):
        """Steal a present"""
        self.left = self.left.left
        return elves - 1


class Table:
    """A table of elves, to support faster deletes from anywhere in the list"""

    def __init__(self, elves, per_stripe):
        self.elves = []
        offset = 1
        while elves > per_stripe:
            self.elves.append(list(range(offset, offset+per_stripe)))
            offset += per_stripe
            elves -= per_stripe
        self.elves.append(list(range(offset, offset+elves)))
        self.len = sum(len(x) for x in self.elves)

    def __getitem__(self, index):
        offset = 0
        while index >= len(self.elves[offset]):
            index -= len(self.elves[offset])
            offset += 1
        return self.elves[offset][index]

    def __len__(self):
        return self.len

    def pop(self, index):
        """Remove and return the item at index"""
        offset = 0
        while index >= len(self.elves[offset]):
            index -= len(self.elves[offset])
            offset += 1
        result = self.elves[offset].pop(index)
        self.len -= 1
        return result


def solve_b(elves):
    """Solve puzzle part b using a list"""
    # Because it is really slow to remove an individual item from a 3MM item
    # linked-list, this is going to work as a list of lists (treated as a
    # single list)
    # elves = 15
    print(f'Creating table with {elves} elves')
    table = Table(elves, 50_000)
    print('Stealing presents...')
    stealer = 0
    while len(table) > 1:
        if len(table) % 1000 == 0:
            print(f'{len(table)} elves are left  ', end='\r')
        taken = (len(table) // 2 + stealer) % len(table)
        next_stealer = stealer
        if taken > stealer:
            next_stealer += 1
        # print(f'len={len(table)}, pos={stealer}, to={taken}, ', end='')
        # stealer_id = table[stealer]
        taken_from = table.pop(taken)
        # print(f'{stealer_id} takes the presents from {taken_from}')
        stealer = next_stealer
        if stealer >= len(table):
            stealer = 0
    print()
    for chunk in table.elves:
        if chunk:
            print(chunk)
    # del stealer_id
    del taken_from
    return table[0]


def solve(part='a'):
    """Solve puzzle"""
    elves = int(PUZZLE.input)
    # elves = 5
    if part == 'b':
        # Part B is really slow via linked-list, so use different algorithm
        return solve_b(elves)
    # Part A is best solved via linked-list
    last = Elf(elves)
    previous = last
    print(f'Creating table with {elves} elves')
    for elf in range(elves - 1, 0, -1):
        new = Elf(elf, previous)
        previous = new
    last.left = previous
    print('Stealing presents...')
    # previous == Elf(1) at this point
    while previous.left != previous:
        elves = previous.steal(elves)
        previous = previous.left
    return previous.number


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
