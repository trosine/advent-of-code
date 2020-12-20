#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/18
"""
import operator
import aoc

PUZZLE = aoc.Puzzle(day=18, year=2020)


def evaluate(line):
    """Evaluate a given expression"""
    # print(f'Evaluating: {line}')
    index = 0
    total = 0
    operation = operator.add
    while index < len(line):
        if line[index] == ')':
            return total, index
        if line[index] == '(':
            result, offset = evaluate(line[index+1:])
            total = operation(total, result)
            index += offset + 1
            # print(f'got {result}, {offset} -- remaining: {line[index+1:]}')
        elif line[index] == ' ':
            pass
        elif line[index] == '+':
            operation = operator.add
        elif line[index] == '*':
            operation = operator.mul
        else:
            # print(f'{operation}({total}, {line[index]})')
            total = operation(total, int(line[index]))
        index += 1
    return total, index


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        pass
    total = 0
    for line in PUZZLE.input.splitlines():
        result, _ = evaluate(line)
        print(f'{result} == {line}')
        total += result
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
