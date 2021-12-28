#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/12
"""

import aoc

PUZZLE = aoc.Puzzle(day=25, year=2016)
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
    del part
    # reset registers
    for reg in REGISTERS:
        REGISTERS[reg] = 0
    instructions = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
        'tgl': tgl,
        }
    program = []
    for command in PUZZLE.input.splitlines():
        command = [
            c if not c.isnumeric() else int(c)
            for c in command.split()
            ]
        command[0] = instructions.get(command[0], command[0])
        program.append(command)
    return slow_solve(program)


def slow_solve(program):
    """Solve using the real program"""
    start = 0
    while True:
        start += 1
        print(f'Testing {start}', end='\r')
        for reg in REGISTERS:
            REGISTERS[reg] = 0
        REGISTERS['a'] = start
        valid = True
        compare = 0
        while REGISTERS['p'] < len(program):
            command = program[REGISTERS['p']]
            if command == program[-1]:
                break  # do not restart the loop
            if command[0] == 'out':
                if REGISTERS['b'] != compare:
                    valid = False
                    break
                compare = 1 - compare
                REGISTERS['p'] += 1
            else:
                command[0](program, *command[1:])
        if valid and REGISTERS['b'] == 1:
            return start
    return None


def fast_solve(program):
    """Solve via simple math"""
    offset = program[1][1] * program[2][1]
    # make sure we start testing even numbers
    # if the offset is odd, we add odd numbers
    # if the offset is even, we add even numbers
    start = offset % 2
    while True:
        start += 2
        test = start + offset
        compare = 0
        valid = True
        while test:
            last = test % 2
            if last != compare:
                valid = False
                break
            test //= 2
            compare = 1 - compare
        if valid and last == 1:
            return start
    return REGISTERS['a']


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    # PUZZLE.report_b(solve('b'))
