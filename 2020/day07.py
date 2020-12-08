#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/7

Handy Haversacks

A: How many different bags can contain at least 1 shiny gold bag.
B: How many total bags exist within a given bag.
"""
import re
import aoc

COLOR = re.compile(r'(\w+ \w+)')
COST = re.compile(r'(\d+) (\w+ \w+)')
PUZZLE = aoc.Puzzle(day=7, year=2020)
TEST_DATA = (
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.',
    )


def contains(data, color, depth=0, max_depth=100):
    """Find the bags that can contain 1 of the specified bags"""
    if depth > max_depth:
        return 0
    viable = set()
    for rule_color, children in data.items():
        if color in children:
            viable.add(rule_color)
            viable.update(contains(data, rule_color, depth+1, max_depth))
    return viable


def cost(costs, color, depth=0, max_depth=100):
    """Find the cost of a bag and its nested contents"""
    if depth > max_depth:
        return 0
    my_cost = 1
    for bag_color, number in costs[color].items():
        my_cost += number * cost(costs, bag_color, depth+1, max_depth)
    return my_cost


def solve(part='a'):
    """Solve puzzle"""
    data = PUZZLE.input.splitlines()
    # data = TEST_DATA
    color = 'shiny gold'

    costs = {}
    for rule in data:
        rule_color = COLOR.match(rule).group()
        matches = COST.findall(rule)
        costs[rule_color] = {match[1]: int(match[0]) for match in matches}

    if part == 'a':
        result = contains(costs, color)
        return len(result)
    return cost(costs, color) - 1


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
