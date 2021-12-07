#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/11
"""
import collections
import itertools
import re

import aoc

PUZZLE = aoc.Puzzle(day=11, year=2016)
CONTAIN = re.compile(r'a (\w+)(?:-compatible)? (microchip|generator)')
GENERATORS = 0
MICROCHIPS = 0


class Building():
    """Represents the building containing microchips and generators"""
    elevator = 0
    floors = [0] * 4

    def __init__(self, floors=None, elevator=0):
        if floors:
            self.floors = floors.copy()
        self.elevator = elevator

    def __iter__(self):
        yield self.elevator
        for floor in self.floors:
            yield floor

    def copy(self):
        """Create a copy of the building"""
        return Building(floors=self.floors, elevator=self.elevator)

    # note, this doesn't check to see that there are exactly 1 of each item
    def validate(self):
        """Validate that chips aren't get fried"""
        if self.elevator < 0 or self.elevator > 3:
            return False
        for floor in self.floors:
            generators = floor & GENERATORS
            chips = floor & MICROCHIPS
            if chips and generators:
                # do all chips have generators?
                if (generators << 1) & chips != chips:
                    return False
        return True

    def next_floors(self):
        """Generate a list of floors that the elevator can go to"""
        if self.elevator > 0:
            yield self.elevator - 1
        if self.elevator < 3:
            yield self.elevator + 1

    def moves(self):
        """Provide a list of possible next moves"""
        # extra=0 simplifies choosing either 1 or 2 items to move
        all_items = bits(self.floors[self.elevator], extra=0)
        picked = itertools.combinations(all_items, 2)
        for elevator, items in itertools.product(self.next_floors(), picked):
            # print(elevator, items)
            building = self.copy()
            building.elevator = elevator
            building.floors[self.elevator] ^= sum(items)
            building.floors[elevator] |= sum(items)
            if building.validate():
                yield building

    def __str__(self):
        result = ''
        for num, floor in enumerate(self.floors):
            shaft = 'E ' if self.elevator == num else '  '
            result += shaft + format_floor(floor) + '\n'
        return result


# https://stackoverflow.com/questions/8898807/pythonic-way-to-iterate-over-bits-of-integer
# the "extra" is added, to allow to easily use itertools.combinations() to pick
# 1 or 2 objects to move
def bits(number, extra=None):
    """Generate a list of set bits"""
    while number:
        set_bit = number & (~number+1)
        yield set_bit
        number ^= set_bit
    if extra is not None:
        yield extra


def format_floor(floor):
    """Format a floor as a string that's easier to read"""
    result = ''
    for index, char in enumerate(format(floor, '014b').replace('0', '.')):
        result += char
        if index % 2 == 1:
            result += ' '
    result += f'  ({floor})'
    return result


def search(start, end):
    """Return the shortest distance between start and end"""
    distance = {tuple(start): 0}
    queue = collections.deque([start])

    last_distance = 0
    while queue:
        current = queue.popleft()
        cur_distance = distance[tuple(current)]
        if cur_distance != last_distance:
            print(f'distance={cur_distance}, queue={len(queue)}', end='\r')
            last_distance = cur_distance

        for neighbor in current.moves():
            serialized = tuple(neighbor)
            if serialized == end:
                return cur_distance + 1
            if serialized not in distance:
                queue.append(neighbor)
                distance[serialized] = cur_distance + 1
    return None


# a building is a tuple of 5 integers: the elevator and 4 floors
# each type of item is represented as a single bit on the floor
# generators are the "even" bits (0, 2, 4, etc)
# microchips are the "odd" bits (1, 3, 5, etc)
def solve(part='a'):
    """Solve puzzle"""
    global GENERATORS, MICROCHIPS  # pylint: disable=global-statement

    floors = [0] * 4
    isotopes = {}
    if part == 'b':
        isotopes = {
            'elerium generator': 1 << 0,
            'elerium microchip': 1 << 1,
            'dilithium generator': 1 << 2,
            'dilithium microchip': 1 << 3,
            }
        floors[0] = sum(isotopes.values())

    for floor, contents in enumerate(PUZZLE.input.splitlines()):
        # floors.append([0, 0])
        for isotope, kind in CONTAIN.findall(contents):
            if f'{isotope} {kind}' not in isotopes:
                isotopes[f'{isotope} generator'] = 1 << len(isotopes)
                isotopes[f'{isotope} microchip'] = 1 << len(isotopes)
            floors[floor] |= isotopes[f'{isotope} {kind}']

    GENERATORS = sum(v for k, v in isotopes.items() if 'generator' in k)
    MICROCHIPS = sum(v for k, v in isotopes.items() if 'microchip' in k)
    building = Building(floors)
    end = (3, 0, 0, 0, MICROCHIPS | GENERATORS)
    return search(building, end)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
