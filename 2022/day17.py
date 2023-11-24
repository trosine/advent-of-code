#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/17
"""
from itertools import cycle
import aoc

PUZZLE = aoc.Puzzle(day=17, year=2022)


class Rock:
    """Implementation of the rocks that fall"""

    def __init__(self, style):
        self.bits = []
        self.width = len(style[0])
        self.height = len(style)
        for row in reversed(style):
            self.bits.append([bit == "#" for bit in row])

    def __getitem__(self, key):
        return self.bits[key]

    def __len__(self):
        return len(self.bits)

    def col(self, col):
        """Get a vertical slice of the rock"""
        return [
            row[col]
            for row in self.bits
        ]


class Chamber:
    """Implementation of the chamber"""
    rock = None  # The falling rock
    pos = None  # Where the left side of the rock is
    height = None  # Where the bottom of the rock is

    def __init__(self, pushes, width=7):
        self.width = width
        self.pushes = pushes
        self.chamber = [[True] * width]

    def __len__(self):
        self.trim()
        return len(self.chamber) - 1

    def add(self, rock):
        """Add a rock to the chamber"""
        self.trim()
        # Add 4 rows above the highest rock to simplify `solidify()`
        for _ in range(3):
            self.chamber.append([False]*self.width)
        # print(self.chamber)
        self.rock = rock
        self.pos = 2
        self.height = len(self.chamber)
        for _ in range(4):
            self.chamber.append([False]*self.width)

    def drop(self):
        """Drop the rock"""
        for row in range(self.rock.height):
            mesh = self.chamber[self.height + row - 1][self.pos:]
            for top, bottom in zip(self.rock[row], mesh):
                if top and bottom:
                    self.solidify()
                    return False
        self.height -= 1
        return True

    def print(self):
        """Print the full chamber"""
        convert = {
            False: " ",
            True: "#",
        }
        for num, row in enumerate(reversed(self.chamber)):
            if num > 15:
                break
            print("|", end="")
            for bit in row:
                print(convert[bit], end="")
            print("|")

    def push(self, direction):
        """Push the rock to the left (<) or right (>)"""
        if direction == "<":
            if self.pos == 0:
                # print("Collided with left wall")
                return  # collision with chamber wall
            slide = -1
        else:
            if self.pos + self.rock.width >= self.width:
                # print("Collided with right wall")
                return  # collision with chamber wall
            slide = 1
        # check for collisions with other rocks
        for col in range(self.rock.width):
            neighbor = [
                row[self.pos + col + slide]
                for row in self.chamber[self.height:]
            ]
            for left, right in zip(self.rock.col(col), neighbor):
                if left and right:
                    # print("Collided with another rock")
                    return  # collision with other rock detected
        self.pos += slide

    def solidify(self):
        """Lock the falling rock in its current place"""
        for row, rock in enumerate(self.rock):
            chamber = self.chamber[self.height + row]
            # print(row, rock)
            # print(" ", chamber)
            for col, pair in enumerate(zip(rock, chamber[self.pos:])):
                # print(f"  {col}  {pair}")
                chamber[self.pos + col] = any(pair)

    def trim(self):
        """Remove empty rows from the top"""
        while not any(self.chamber[-1]):
            self.chamber.pop()


ROCKS = [
    Rock(["####"]),
    Rock([
        " # ",
        "###",
        " # ",
    ]),
    Rock([
        "  #",
        "  #",
        "###",
    ]),
    Rock([
        "#",
        "#",
        "#",
        "#",
    ]),
    Rock([
        "##",
        "##",
    ]),
]


def solve(part='a'):
    """Solve puzzle"""
    count = 2022
    if part == 'b':
        count = 1000000000000
        count = 10000
    jets = PUZZLE.input.strip()
    jet = cycle(iter(jets))
    chamber = Chamber(jets)
    previous = 0
    pushes = 0
    for rock in range(count):
        # if rock % 1760 == 0:
        if pushes >= 10091:
            print(rock, pushes, len(chamber)-previous)
            previous = len(chamber)
            pushes = 0
        # if rock % 1760 == 0:
        #     print("\n-------------")
        #     # print(current, chamber.pos, chamber.height)
        #     chamber.print()
        #     input()
        if rock % 1000 == 0:
            print(rock, end="\r")
        chamber.add(ROCKS[rock % 5])
        while True:
            pushes += 1
            current = next(jet)
            # print(current, end="")
            chamber.push(current)
            if not chamber.drop():
                break
    return len(chamber)

# repetition every 1760

if __name__ == "__main__":
    # PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
