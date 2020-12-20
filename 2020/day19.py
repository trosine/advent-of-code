#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/19
"""
import re
import aoc
import lark

PUZZLE = aoc.Puzzle(day=19, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    grammar, data = PUZZLE.input.split('\n\n')
    if part == 'b':
        grammar = grammar.replace('\n8: 42', '\n8: 42 | 42 8')
        grammar = grammar.replace('\n11: 42 31', '\n11: 42 31 | 42 11 31')
    # rules in lark must start with a letter
    grammar = re.sub(r'\b(\d)', r'r\1', grammar)
    # Note, that parser=lalr is not possible due to the input having ambiguity
    validator = lark.Lark(grammar, start='r0')
    total = 0
    for line in data.splitlines():
        try:
            validator.parse(line)
            total += 1
        except lark.exceptions.LarkError:
            pass
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
