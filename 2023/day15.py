#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/15
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=15, year=2023)


class Lens:
    """A lens with both a label and focal length"""

    def __init__(self, label, length):
        self.label = label
        self.length = length

    # allows for list.remove and list.index
    def __eq__(self, other):
        if isinstance(other, Lens):
            return self.label == other.label
        return self.label == other

    def __str__(self):
        return f"[{self.length} {self.label}]"

    def __repr__(self):
        return str(self)


def generate_hash(string):
    """Return the HASH as defined in the puzzle"""
    value = 0
    for char in string:
        value += ord(char)
        value = (value * 17) % 256
    return value


def solve(part="a"):
    """Solve puzzle"""
    validation = 0
    boxes = [[] for _ in range(256)]
    for line in PUZZLE.input.splitlines():
        for step in line.split(","):
            validation += generate_hash(step)
            label, oper, length = re.split(r"([-=])", step)
            box_id = generate_hash(label)
            box = boxes[box_id]
            if oper == "=":
                lens = Lens(label, int(length))
                if label in box:
                    index = box.index(label)
                    box[index] = lens
                else:
                    box.append(lens)
            else:
                if label in box:
                    box.remove(label)
    if part == "a":
        return validation
    total = 0
    for box_id, box in enumerate(boxes, 1):
        for slot, lens in enumerate(box, 1):
            total += box_id * slot * lens.length
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
