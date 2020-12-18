#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/16
"""
import collections
import re
import aoc

PUZZLE = aoc.Puzzle(day=16, year=2020)


def parse_input(content):
    """Parse the puzzle input"""
    parser = re.compile(r'(.+):\s+(\d+)-(\d+) or (\d+)-(\d+)')
    raw_rules, ticket, nearby = content.split('\n\n')
    ticket = list(map(int, ticket.splitlines()[1].split(',')))
    nearby = nearby.splitlines()[1:]

    fields = set()
    rules = collections.defaultdict(set)
    for rule in raw_rules.splitlines():
        match = parser.match(rule)
        groups = match.groups()
        fields.add(groups[0])
        for valid in range(int(groups[1]), int(groups[2])+1):
            rules[valid].add(groups[0])
        for valid in range(int(groups[3]), int(groups[4])+1):
            rules[valid].add(groups[0])
    return rules, fields, ticket, nearby


def solve(part='a'):
    """Solve puzzle"""
    rules, fields, my_ticket, nearby = parse_input(PUZZLE.input)
    valid_fields = [fields.copy() for _ in my_ticket]
    error_rate = 0

    for ticket in nearby:
        values = list(map(int, ticket.split(',')))
        for value in values:
            if value not in rules:
                # print(f'rejecting ({value}) {ticket}')
                error_rate += value
                break
        else:
            for index, value in enumerate(values):
                valid_fields[index].intersection_update(rules[value])
    if part == 'a':
        return error_rate
    product = 1
    for _, index in sorted([(len(f), i) for i, f in enumerate(valid_fields)]):
        field = valid_fields[index].pop()
        if field.startswith('departure'):
            product *= my_ticket[index]
        for fields in valid_fields:
            fields.discard(field)
    return product


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
