#!/usr/bin/env python3
"""
https://adventofcode.com/2024/day/5
"""
import collections

import aoc

PUZZLE = aoc.Puzzle(day=5, year=2024)


class Rule:
    """Details from the perspective of a single digit"""
    # pylint: disable=too-few-public-methods

    def __init__(self):
        self.before = set()
        self.after = set()


def is_valid(update, rules):
    """Determine if this particular update is valid"""
    for pivot, value in enumerate(update):
        before = set(update[:pivot])
        after = set(update[pivot+1:])
        rule = rules[value]
        if before - rule.before:
            return False
        if after - rule.after:
            return False
    return True


# this assumes that there is only 1 proper ordering of the pages
def reorder(update, rules):
    """Reorder the update"""
    update = set(update)  # copy by converting to a set
    scoped = {}
    result = []
    # scope the rule set to just the pages in the update
    # only the "before" side of the rules matters
    for page in update:
        scoped[page] = rules[page].before & update

    while scoped:
        # find the next page from the scoped rules (.before is empty)
        for page, rule in scoped.items():
            if not rule:
                result.append(page)
                break
        del scoped[page]
        # remove this page from all other rules
        for rule in scoped.values():
            rule.discard(page)

    return result


def solve(part="a"):
    """Solve puzzle"""
    ordering, updates = PUZZLE.input.split("\n\n")
    rules = collections.defaultdict(Rule)

    for line in ordering.splitlines():
        before, after = line.split("|")
        rules[before].after.add(after)
        rules[after].before.add(before)

    total = 0
    for line in updates.splitlines():
        update = line.split(",")
        middle = len(update) // 2
        if is_valid(update, rules):
            if part == "a":
                total += int(update[middle])
        else:
            if part == "b":
                update = reorder(update, rules)
                total += int(update[middle])
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
