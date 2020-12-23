#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/23
"""
import aoc

PUZZLE = aoc.Puzzle(day=23, year=2020)


class Cup():
    """A numbered cup with a link to its clockwise neighbor"""
    # pylint: disable=too-few-public-methods

    def __init__(self, num):
        self.num = num
        self.next = None


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        total_cups = 9
        moves = 100
    else:
        total_cups = 1000000
        moves = 10000000
    start = None
    previous = None
    cups = [None] * (total_cups + 1)
    for num in PUZZLE.input.strip():
        this = Cup(int(num))
        if start is None:
            start = this
        else:
            previous.next = this
        cups[this.num] = this
        previous = this
    for num in range(10, total_cups + 1):
        this = Cup(num)
        previous.next = cups[num] = this
        previous = this
    previous.next = start

    for _ in range(moves):
        removed = start.next
        start.next = removed.next.next.next
        removed_nums = (removed.num, removed.next.num, removed.next.next.num)
        destination = (start.num - 1) or total_cups
        while destination in removed_nums:
            destination = (destination - 1) or total_cups
        # print(f'S={start.num}, R={removed_nums} D={destination}')
        removed.next.next.next = cups[destination].next
        cups[destination].next = removed
        start = start.next

    start = cups[1].next
    if part == 'b':
        return start.num * start.next.num
    result = ''
    while start.num != 1:
        result += str(start.num)
        start = start.next
    return result


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
