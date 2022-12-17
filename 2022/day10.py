#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/10
"""
import aoc

PUZZLE = aoc.Puzzle(day=10, year=2022)


def solve(part='a'):
    """Solve puzzle"""
    cycle = 0
    total = 0
    register = 1
    crt = [" "] * 240
    lines = iter(PUZZLE.input.splitlines())
    line = next(lines)
    defer = line.startswith("addx")
    try:
        while True:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                strength = cycle * register
                total += strength
            if abs(((cycle-1) % 40) - register) <= 1:
                crt[cycle-1] = "#"
            if defer:
                defer = False
                continue
            if line.startswith("addx"):
                register += int(line.split()[1])
            line = next(lines)
            defer = line.startswith("addx")
    except StopIteration:
        pass
    if part == "a":
        return total
    for offset in range(0, 240, 40):
        print(''.join(crt[offset:offset+40]))
    return input("Please enter the code:").upper()


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
