#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/12
"""
from math import factorial  # pylint: disable=no-name-in-module

import aoc

PUZZLE = aoc.Puzzle(day=23, year=2016)
REGISTERS = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'p': 0,
    }


def cpy(program, source, dest):
    """Copy integer/register to a register"""
    del program
    if isinstance(dest, str):
        REGISTERS[dest] = REGISTERS.get(source, source)
    REGISTERS['p'] += 1


def dec(program, reg):
    """Increment register by 1"""
    del program
    if isinstance(reg, str):
        REGISTERS[reg] -= 1
    REGISTERS['p'] += 1


def inc(program, reg):
    """Increment register by 1"""
    del program
    if isinstance(reg, str):
        REGISTERS[reg] += 1
    REGISTERS['p'] += 1


def jnz(program, reg, offset):
    """If reg is not zero, move instruction pointer by offset"""
    del program
    if REGISTERS.get(reg, reg) != 0:
        REGISTERS['p'] += int(REGISTERS.get(offset, offset))
    else:
        # print(f'jnz {reg} {offset}: {REGISTERS}')
        REGISTERS['p'] += 1


def tgl(program, dest):
    """Toggle a given command"""
    target = REGISTERS['p'] + REGISTERS.get(dest, dest)
    REGISTERS['p'] += 1
    if target in range(len(program)):
        # print(f'tgl {dest} ({target}:{program[target]}): {REGISTERS}')
        instr = program[target][0]
        if instr in ('dec', 'tgl'):
            program[target][0] = 'inc'
        elif instr == 'inc':
            program[target][0] = 'dec'
        elif instr == 'cpy':
            program[target][0] = 'jnz'
        else:
            program[target][0] = 'cpy'


def solve(part='a'):
    """Solve puzzle"""
    # reset registers
    for reg in REGISTERS:
        REGISTERS[reg] = 0
    REGISTERS['a'] = 7
    instructions = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
        'tgl': tgl,
        }
    program = []
    for command in PUZZLE.input.splitlines():
        if '#' in command:
            continue
        command = command.strip()
        program.append([
            c if not c.isnumeric() else int(c)
            for c in command.split()
            ])
    if part == 'b':
        return factorial(12) + program[19][1] * program[20][1]
    commands = len(program)
    while REGISTERS['p'] < commands:
        command = program[REGISTERS['p']]
        instructions[command[0]](program, *command[1:])
    return REGISTERS['a']


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
