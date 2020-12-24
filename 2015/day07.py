#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/7
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=7, year=2015)
INT_MAX = 2**16-1
GATES = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'NOT': lambda x, y: ~y & INT_MAX,
    'LSHIFT': lambda x, y: (x << y) & INT_MAX,
    'RSHIFT': lambda x, y: (x >> y),
    None: lambda x, y: y,
    }
PARSE = re.compile(
    r'(?:(?P<input1>[a-z0-9]+)\s+)?'
    r'(?:(?P<gate>[A-Z]+)\s+)?'
    r'(?P<input2>[a-z0-9]+)\s+'
    r'->\s+(?P<result>\w+)'
    )


def solve(part='a'):
    """Solve puzzle"""
    operations = {}
    results = {None: None}
    if part == 'b':
        results['b'] = solve('a')
    for line in PUZZLE.input.splitlines():
        parsed = PARSE.match(line).groupdict()
        for key in ('input1', 'input2'):
            if isinstance(parsed[key], str) and parsed[key].isnumeric():
                parsed[key] = int(parsed[key])
                results[parsed[key]] = parsed[key]
        operations[parsed['result']] = parsed
    while 'a' not in results:
        for key, parsed in operations.items():
            if key in results:
                continue
            if parsed['input1'] not in results:
                continue
            if parsed['input2'] not in results:
                continue
            operation = GATES[parsed['gate']]
            input1 = results[parsed['input1']]
            input2 = results[parsed['input2']]
            results[parsed['result']] = operation(input1, input2)
    return results['a']


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
