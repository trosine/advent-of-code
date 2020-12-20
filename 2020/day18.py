#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/18
"""
import operator
import aoc
import lark

PUZZLE = aoc.Puzzle(day=18, year=2020)
GRAMMAR_SIMPLE = """
    ?start: sum
    // Addition and multiplication have the same precedence.
    ?sum : atom
         | sum "+" atom -> add
         | sum "*" atom -> mul
    ?atom: NUMBER       -> number
         | "(" sum ")"

    %import common.NUMBER
    %import common.WS
    %ignore WS
"""
GRAMMAR_REVERSE = """
    ?start: product
    // Because a product comes from a sum, the sum has a higher precedence.
    ?product: sum
         | product "*" sum -> mul
    ?sum : atom
         | sum "+" atom    -> add
    ?atom: NUMBER          -> number
         | "(" product ")"

    %import common.NUMBER
    %import common.WS
    %ignore WS
"""


@lark.v_args(inline=True)
class CalcTree(lark.Transformer):
    """Converts the grammar to a value"""
    # pylint: disable=too-few-public-methods
    number = int
    mul = operator.mul
    add = operator.add


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        grammar = GRAMMAR_SIMPLE
    else:
        grammar = GRAMMAR_REVERSE
    calculator = lark.Lark(grammar, parser='lalr', transformer=CalcTree())
    total = 0
    for line in PUZZLE.input.splitlines():
        result = calculator.parse(line)
        # print(f'{result} == {line}')
        total += result
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
