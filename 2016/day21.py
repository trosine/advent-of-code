#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/21
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=21, year=2016)
PARSE = re.compile(
    r'(?:'
    r'(swap (?:position|letter)) (\w+) with (?:position|letter) (\w+)'
    r'|(rotate (?:left|right)).*(\d+)'
    r'|(rotate based) on position of letter (\w)'
    r'|(reverse positions) (\d+) through (\d+)'
    r'|(move position) (\d+) to position (\d+)'
    r')'
    )
# how many times to rotate right when reversing a string based on a letter
REVERSE_BASE_MAP = [7, 7, 2, 6, 1, 5, 0, 4]


def swap_position(password, reverse, one, two):
    """Swap the characters as indices one and two"""
    del reverse
    one, two = sorted([one, two])
    return ''.join([
        password[:one],
        password[two],
        password[one+1:two],
        password[one],
        password[two+1:],
        ])


def swap_letter(password, reverse, *chars):
    """Swap the characters"""
    del reverse
    chars = ''.join(chars)
    table = str.maketrans(chars, chars[::-1])
    return password.translate(table)


def reverse_positions(password, reverse, first, last):
    """Reverse the characters between start and end (inclusive)"""
    del reverse
    # because password[x:-1:-1] doesn't work
    start = None if first == 0 else first - 1
    return ''.join([
        password[:first],
        password[last:start:-1],
        password[last+1:],
        ])


def move_position(password, reverse, source, dest):
    """Move character at source to dest"""
    if reverse:
        source, dest = dest, source
    new_password = list(password)
    char = new_password.pop(source)
    new_password.insert(dest, char)
    return ''.join(new_password)


def rotate_based(password, reverse, char):
    """Rotate the password based on the position of char"""
    index = password.index(char)
    if reverse:
        actual = REVERSE_BASE_MAP[index]
    else:
        actual = 1 + index + (1 if index >= 4 else 0)
        actual = actual % len(password)
    return rotate_right(password, False, actual)


def rotate_left(password, reverse, chars):
    """Rotate the characters in the password left"""
    if not reverse:
        chars = len(password) - chars
    return rotate_right(password, False, chars)


def rotate_right(password, reverse, chars):
    """Rotate the characters in the password right"""
    if reverse:
        chars = len(password) - chars
    return password[-chars:] + password[:-chars]


def solve(part='a'):
    """Solve puzzle"""
    data = PUZZLE.input.splitlines()
    if part == 'a':
        password = 'abcdefgh'
    else:
        password = 'fbgdceah'
        # password = 'gcedfahb'
        data = data[::-1]
    reverse = part == 'b'
    commands = {
        'swap position': swap_position,
        'swap letter': swap_letter,
        'rotate left': rotate_left,
        'rotate right': rotate_right,
        'rotate based': rotate_based,
        'reverse positions': reverse_positions,
        'move position': move_position,
        }
    for command in data:
        match = PARSE.match(command)
        command = [
            int(x) if x.isnumeric() else x
            for x in match.groups()
            if x is not None
            ]
        password = commands[command[0]](password, reverse, *command[1:])
    return password


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
