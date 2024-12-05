#!/usr/bin/env python3
"""
https://adventofcode.com/2024/day/1
"""
import aoc

PUZZLE = aoc.Puzzle(day=1, year=2024)


def load_data(data=PUZZLE.input):
    """Parse puzzle input into 2 lists"""
    list1 = []
    list2 = []
    for line in data.splitlines():
        # print(line)
        (left, right) = map(int, line.split())
        list1.append(left)
        list2.append(right)
    return list1, list2


def solve(part="a"):
    """Solve puzzle"""
    left_list, right_list = load_data()
    left_list.sort()
    right_list.sort()
    total = 0
    if part == "a":
        for left, right in zip(left_list, right_list):
            total += abs(left - right)
    else:
        for num in left_list:
            total += num * right_list.count(num)
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
