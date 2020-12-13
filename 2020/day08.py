#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/8
"""
import aoc

PUZZLE = aoc.Puzzle(day=8, year=2020)
COMMANDS = {
    'acc': lambda x: (1, int(x)),
    'jmp': lambda x: (int(x), 0),
    'nop': lambda x: (1, 0),
    }
REPLACEMENTS = {
    'acc': 'acc',
    'jmp': 'nop',
    'nop': 'jmp',
    }


def swap(instruction):
    """Swap jmp<->nop commands"""
    command, number = instruction.split()
    return f'{REPLACEMENTS[command]} {number}'


def parse(instruction):
    """Returns updates to the instruction and acc"""
    command, number = instruction.split()
    return COMMANDS[command](number)


def execute(commands):
    """Execute commands, return the value of acc"""
    instr = 0
    acc = 0
    total = len(commands)
    seen = [False] * total
    while True:
        if instr == total:
            raise IndexError(acc)
        if seen[instr]:
            return acc
        command = parse(commands[instr])
        seen[instr] = True
        instr += command[0]
        acc += command[1]


def solve(part='a'):
    """Solve puzzle"""
    commands = PUZZLE.input.splitlines()
    if part == 'a':
        return execute(commands)
    for index, backup in enumerate(commands):
        if backup.startswith('acc'):
            # no sense in running this: the program would still have a loop
            continue
        commands[index] = swap(backup)
        try:
            execute(commands)
        except IndexError as err:
            print(f'Program terminated after swapping instruction {index}')
            return err.args[0]
        commands[index] = backup
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
