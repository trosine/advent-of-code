#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/23
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=23, year=2015)
SPLIT = re.compile(r'[, ]+')


def solve(part='a'):
    """Solve puzzle"""
    program = [SPLIT.split(x) for x in PUZZLE.input.splitlines()]
    # print(len(program))
    register = {'a': 0, 'b': 0}
    if part == 'b':
        register['a'] = 1
    instr = 0
    while 0 <= instr < len(program):
        cmd = program[instr]
        # print(instr, register, cmd)
        if cmd[0] == 'jmp':
            instr += int(cmd[1])
        elif cmd[0] == 'jio':
            instr += int(cmd[2]) if register[cmd[1]] == 1 else 1
        elif cmd[0] == 'jie':
            instr += int(cmd[2]) if register[cmd[1]] % 2 == 0 else 1
        else:
            if cmd[0] == 'hlf':
                register[cmd[1]] /= 2
            elif cmd[0] == 'tpl':
                register[cmd[1]] *= 3
            elif cmd[0] == 'inc':
                register[cmd[1]] += 1
            instr += 1
    return register['b']


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
