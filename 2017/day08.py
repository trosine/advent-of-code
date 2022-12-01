#!/usr/bin/env python3
"""
https://adventofcode.com/2017/day/8
"""
import operator
import re
from collections import defaultdict

import aoc

PUZZLE = aoc.Puzzle(day=8, year=2017)
PARSE = re.compile(
    r'(?P<register>[a-z]+)\s+'
    r'(?P<operation>inc|dec)\s+'
    r'(?P<amount>[-0-9]+)\s+'
    r'if\s+'
    r'(?P<cond_reg>[a-z]+)\s+'
    r'(?P<cond_op>[<>=!]+)\s+'
    r'(?P<const>[-0-9]+)$'
)
OPERATIONS = {
    'inc': operator.add,
    'dec': operator.sub,
}
CONDITIONS = {
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    '==': operator.eq,
    '!=': operator.ne,
}


def solve(part='a'):
    """Solve puzzle"""
    registers = defaultdict(int)
    largest = 0
    for instruction in PUZZLE.input.splitlines():
        parsed = PARSE.match(instruction).groupdict()
        condition = CONDITIONS[parsed['cond_op']]
        if condition(registers[parsed['cond_reg']], int(parsed['const'])):
            operation = OPERATIONS[parsed['operation']]
            registers[parsed['register']] = operation(
                registers[parsed['register']],
                int(parsed['amount'])
            )
            # keep track of the largest register value at any point
            largest = max(largest, registers[parsed['register']])
    if part == 'a':
        return max(registers.values())
    return largest


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
