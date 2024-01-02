#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/25
"""
from collections import defaultdict
import aoc

PUZZLE = aoc.Puzzle(day=25, year=2023)


def load_input():
    """Load the puzzle input"""
    nodes = defaultdict(set)
    for line in PUZZLE.input.splitlines():
        name, connected = line.split(": ")
        connected = connected.split()
        for dest in connected:
            nodes[dest].add(name)
            nodes[name].add(dest)
    return nodes


def find_starters(nodes, group=None, depth=3):
    """Find groups of 3 nodes that loop back on each other"""
    if group is None:
        group = []
    if group == []:
        candidates = set(nodes.keys())
    else:
        candidates = nodes[group[-1]] - set(group)

    if len(group) < depth:
        for node in candidates:
            if len(group) > 1 and group[0] in nodes[node]:
                yield frozenset(group + [node])
            else:
                yield from find_starters(nodes, group + [node], depth)


def reachable(nodes, group):
    """Combine the connections of all nodes in the group"""
    result = set()
    for node in group:
        result |= nodes[node]
    return result


def expand(nodes, start):
    """Expand a group by adding nodes that can see at least 2 existing nodes"""
    group = set(start)
    reach = reachable(nodes, group)
    found = True
    while found:
        found = False
        candidates = reach.copy()
        for node in candidates:
            if node in group:
                continue
            intersect = nodes[node] & group
            if len(intersect) >= 2:
                # print(f"Adding {node}: intersection={intersect}")
                found = True
                group.add(node)
                reach |= nodes[node]
    return group


def merge_groups(nodes, groups, start):
    """Merge multiple groups together"""
    group = set(start)
    found = True
    while found:
        found = False
        remove = []
        for candidate in groups:
            intersect = reachable(nodes, candidate) & group
            if len(intersect) >= 2:
                found = True
                remove.append(candidate)
                group |= candidate
        for candidate in remove:
            groups.remove(candidate)
    return group


def solve(part="a"):
    """Solve puzzle"""
    if part == "b":
        return None
    nodes = load_input()
    starters = set(find_starters(nodes, depth=6))  # set of frozensets
    print("Number of starter groups:", len(starters))
    groups = []
    for group in starters:
        expanded = expand(nodes, group)
        groups.append(expanded)
    group_iter = groups.copy()
    group_orig = groups.copy()
    groups = set()
    for group in group_iter:
        merged = merge_groups(nodes, group_orig, group)
        merged = frozenset(expand(nodes, merged))
        groups.add(merged)

    print("Number of merged groups:", len(groups))
    groups = sorted(groups, key=len, reverse=True)
    group1 = len(groups[0])
    group2 = len(nodes) - group1
    print(group1, group2)
    return group1 * group2


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
