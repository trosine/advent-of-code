#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/19
"""
import collections
import re
import aoc
import lark

PUZZLE = aoc.Puzzle(day=19, year=2015)
ELEMENT = re.compile('[A-Z][a-z]?')


def calibrate(rules, original):
    """Generate a set of potential results"""
    results = set()
    for orig, new in rules:
        for match in re.finditer(orig, original):
            results.add(
                original[:match.start()]
                + new
                + original[match.end():]
                )
    return len(results)


def count(tree):
    """Counts lark trees with children"""
    # trees without children are simply individual elements, so we only care
    # about the trees that "change" the number of elements
    if len(tree.children) > 0:
        return 1 + sum(count(c) for c in tree.children)
    return 0


def solve(part='a'):
    """Solve puzzle"""
    data, medicine = PUZZLE.input.split('\n\n')
    data = [x.split(' => ') for x in data.splitlines()]
    if part == 'a':
        return calibrate(data, medicine)

    # create basic ruleset structure based on provided data
    rules = collections.defaultdict(list)
    for rule in data:
        elements = ELEMENT.findall(rule[1])
        rules[rule[0]].append(x.lower() for x in elements)

    grammar = ''
    # add grammar rules for elements that don't have their own rule
    constants = set(ELEMENT.findall(medicine)) - set(rules.keys())
    for elem in constants:
        grammar += f'{elem.lower()}: "{elem}"\n'

    # add grammar rules for elements that do have their own rules
    for elem, ruleset in rules.items():
        grammar += f'{elem.lower()}: '
        grammar += ' | '.join([' '.join(r) for r in ruleset])
        grammar += f' | "{elem}"\n'

    parser = lark.Lark(grammar, start='e', parser='lalr')
    return count(parser.parse(medicine))


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
