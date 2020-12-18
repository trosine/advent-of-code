#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/14
"""
import collections
import re
import aoc

PUZZLE = aoc.Puzzle(day=14, year=2020)
ADDR_MAX = (2 ** 36) - 1
PARSER = re.compile(
    r'(?P<command>mask|mem)(?:\[(?P<address>\d+)\])? = (?P<value>.+)'
    )


def mem_version2(register, mask, address, value):
    """Update the value in the registry using part B method"""
    index = mask.find('X')
    if index >= 0:
        address = address & (ADDR_MAX - 2 ** (35-index))
        for bit in ('0', '1'):
            mask = mask[0:index] + bit + mask[index+1:]
            mem_version2(register, mask, address, value)
    else:
        # print(f'{address}|{mask}: {int(mask, 2) | address} == {value}')
        register[int(mask, 2) | address] = value


def mem_version1(register, mask, address, value):
    """Update the value in the registry using part A method"""
    value |= int(mask.replace('X', '0'), 2)
    value &= int(mask.replace('X', '1'), 2)
    register[address] = value


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        mem = mem_version1
    else:
        mem = mem_version2
    mask = ''
    register = collections.defaultdict(int)
    for line in PUZZLE.input.splitlines():
        match = PARSER.match(line)
        if match.group('command') == 'mask':
            mask = match.group('value')
        else:
            address = int(match.group('address'))
            value = int(match.group('value'))
            mem(register, mask, address, value)
            # print(f'mem[{address}] = {value}')
    return sum(register.values())


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
