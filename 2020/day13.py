#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/13
"""
import aoc

PUZZLE = aoc.Puzzle(day=13, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    earliest, schedule = PUZZLE.input.splitlines()
    earliest = int(earliest)
    buses = []
    part_b_start = 0
    multiple = 1
    for offset, bus in enumerate(schedule.split(',')):
        if bus == 'x':
            continue
        bus = int(bus)
        # part A:
        # easily sorted list - (delay, bus id)
        buses.append((bus - earliest % bus, bus))
        # part B:
        # Once we find a match for the first N buses, the next potential time
        # will be at some multiple of their lowest common multiple
        # Since all of the bus numbers are prime, the lowest common multiple is
        # their product
        while True:
            if (part_b_start + offset) % bus == 0:
                # print(f'bus {bus} found at {part_b_start} (lcm={multiple})')
                multiple *= bus  # or math.lcm()
                break
            part_b_start += multiple
    if part == 'a':
        soonest = sorted(buses)[0]
        return soonest[0] * soonest[1]
    return part_b_start


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
