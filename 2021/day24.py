#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/24
"""
import itertools
import re

import aoc

PUZZLE = aoc.Puzzle(day=24, year=2021)
REGISTERS = {
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
    }


def inp(dest, value):
    """Input a value into the register"""
    REGISTERS[dest] = value


def add(dest, value):
    """Multiply two numbers"""
    REGISTERS[dest] += REGISTERS.get(value, value)


def mul(dest, value):
    """Multiply two numbers"""
    REGISTERS[dest] *= REGISTERS.get(value, value)


def div(dest, value):
    """Divide two numbers, rounding towards zero"""
    REGISTERS[dest] = int(REGISTERS[dest] / REGISTERS.get(value, value))


def mod(dest, value):
    """Get the modulus"""
    REGISTERS[dest] %= REGISTERS.get(value, value)


def eql(dest, value):
    """Compare equality: 1 if equal, 0 if unequal"""
    REGISTERS[dest] = int(REGISTERS[dest] == REGISTERS.get(value, value))


def run_function(function, digit, previous):
    """Run the function with the digit"""
    REGISTERS['z'] = previous
    inp(function[0][1], digit)
    for command in function[1:]:
        command[0](*command[1:])


def valid_models(program):
    """Get a list of models that evaluate to z=0"""
    models = [('', 0)]
    for offset, function in enumerate(program):
        print(f'Calculating digit {offset}: m={len(models)}')
        new_models = [[], []]
        for previous, digit in itertools.product(models, range(9, 0, -1)):
            # print(f'{previous} -- {digit}')
            run_function(function, digit, previous[1])
            model = previous[0] + str(digit)
            new_models[REGISTERS['x']].append((model, REGISTERS['z']))
        models = new_models[0] or new_models[1]
    return models


def solve(part='a'):
    """Solve puzzle"""
    program = []
    for line in PUZZLE.input.splitlines():
        instr = [int(x) if re.match(r'-?\d+$', x) else x for x in line.split()]
        if instr[0] == 'inp':
            program.append([instr])
        else:
            instr[0] = globals()[instr[0]]
            program[-1].append(instr)

    models = valid_models(program)
    if part == 'a':
        return max(models)[0]
    return min(models)[0]


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
