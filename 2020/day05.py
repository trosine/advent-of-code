#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/5
"""
import operator
import aoc

PUZZLE = aoc.Puzzle(day=5, year=2020)


class Seat():
    """Seat on a plane"""

    def __init__(self, board_pass):
        self.boarding_pass = board_pass

        start = 0
        end = 127
        total = 128
        for select in board_pass[0:7]:
            total //= 2
            if select == 'F':
                end -= total
            else:
                start += total
        self.row = start

        start = 0
        end = 7
        total = 8
        for select in board_pass[7:]:
            total //= 2
            if select == 'L':
                end -= total
            else:
                start += total
        self.col = start

    def __repr__(self):
        return f'<Seat({self.boarding_pass})>'

    def __str__(self):
        return f'{repr(self)}: {self.pos()}, {self.id()})'

    def pos(self):
        """The seat coordinates (row, col)"""
        return self.row, self.col

    def id(self):
        """The numeric seat identifier"""
        # pylint: disable=invalid-name
        return self.row * 8 + self.col


def solve(part='a'):
    """Solve puzzle"""
    data = PUZZLE.input.splitlines()
    # data = ('FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL')
    data = list(map(Seat, data))
    data.sort(key=operator.methodcaller('id'))
    # for seat in data:
    #     print(seat)
    if part == 'a':
        return data[-1].id()
    expected = data[0].id()
    for seat in data:
        if seat.id() != expected:
            return expected
        expected += 1
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
