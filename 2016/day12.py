#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/12
"""
import aoc

PUZZLE = aoc.Puzzle(day=12, year=2016)
REGISTERS = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'p': 0,
    }


def cpy(source, dest):
    """Copy integer/register to a register"""
    REGISTERS[dest] = REGISTERS.get(source, source)
    REGISTERS['p'] += 1


def dec(reg):
    """Increment register by 1"""
    REGISTERS[reg] -= 1
    REGISTERS['p'] += 1


def inc(reg):
    """Increment register by 1"""
    REGISTERS[reg] += 1
    REGISTERS['p'] += 1


def jnz(reg, offset):
    """If reg is not zero, move instruction pointer by offset"""
    if REGISTERS.get(reg, reg) != 0:
        REGISTERS['p'] += int(offset)
    else:
        REGISTERS['p'] += 1


def solve(part='a'):
    """Solve puzzle"""
    # reset registers
    for reg in REGISTERS:
        REGISTERS[reg] = 0
    if part == 'b':
        REGISTERS['c'] = 1
    instructions = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
        }
    program = []
    for command in PUZZLE.input.splitlines():
        program.append([
            c if not c.isnumeric() else int(c)
            for c in command.split()
            ])
    commands = len(program)
    while REGISTERS['p'] < commands:
        command = program[REGISTERS['p']]
        instructions[command[0]](*command[1:])
    return REGISTERS['a']


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
