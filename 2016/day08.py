#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/8
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=8, year=2016)


def rect(display, cols, rows):
    """Turn on the pixels in the rectangle defined"""
    cols = int(cols)
    rows = int(rows)
    for row in range(rows):
        for col in range(cols):
            display[row][col] = True


def rotate_row(display, row, cols):
    """Rotate a specific row by the number of columns"""
    row = int(row)
    cols = int(cols)
    display[row] = display[row][-cols:] + display[row][:-cols]


def rotate_column(display, col, rows):
    """Rotate a column by the number of rows"""
    col = int(col)
    rows = int(rows)
    column = [row[col] for row in display]
    column = column[-rows:] + column[:-rows]
    for row in range(6):
        display[row][col] = column[row]


def solve(part='a'):
    """Solve puzzle"""
    display = []
    parse_rect = re.compile(r'rect (\d+)x(\d+)')
    parse_rotate = re.compile(r'rotate (?:row|column) [xy]=(\d+) by (\d+)')
    for _ in range(6):
        display.append([False]*50)
    for line in PUZZLE.input.splitlines():
        if line.startswith('rect'):
            rect(display, *parse_rect.match(line).groups())
        else:
            match = parse_rotate.match(line).groups()
            if line.startswith('rotate row'):
                rotate_row(display, *match)
            elif line.startswith('rotate column'):
                rotate_column(display, *match)
    total = 0
    for row in display:
        total += sum(row)
        print(''.join('#' if x else ' ' for x in row))
    if part == 'b':
        print()
        total = input('Please re-enter the code above: ').upper()
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
