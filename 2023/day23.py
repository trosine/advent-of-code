#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/23
"""
from collections import defaultdict
from point import Point2D
import aoc

PUZZLE = aoc.Puzzle(day=23, year=2023)
SLOPES = {
    ">": Point2D(0, 1),
    "<": Point2D(0, -1),
    "^": Point2D(-1, 0),
    "v": Point2D(1, 0),
}


def load_map():
    """Load the map from the puzzle"""
    grid = {}
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, char in enumerate(line):
            pos = Point2D(row, col)
            grid[pos] = char
    return grid


def walk_path(grid, vertex, direction, final):
    """Walk down a path until we find the the next vertex
    returns: (vertex, distance)
    """
    previous = vertex
    pos = vertex + direction
    distance = 1
    if grid[pos] in SLOPES:
        # skip the initial "gate"
        previous = pos
        pos += direction
        distance += 1
    # print("walk:", grid[pos], pos, direction, distance)
    while grid[pos] == ".":
        if pos == final:
            return pos, distance
        for neighbor in pos.neighbors(pos.cardinals):
            if neighbor == previous or grid[neighbor] == "#":
                continue
            previous = pos
            pos = neighbor
            distance += 1
            break  # only 1 neighbor should be possible
    end = pos + SLOPES[grid[pos]]
    distance += 1
    return end, distance


def make_graph(grid, acyclic=True):
    """Create a Directed Graph from the map"""
    final = max(grid) + (0, -1)
    pos = Point2D(0, 1)
    direction = Point2D(1, 0)
    edges = defaultdict(list)
    queue = [(pos, direction)]
    seen = set()
    seen.add(pos)
    while queue:
        vertex, direction = queue.pop()
        end, distance = walk_path(grid, vertex, direction, final)
        edges[vertex].append((end, distance))
        if not acyclic:
            edges[end].append((vertex, distance))
        if end == final:
            continue
        if end in seen:
            continue
        seen.add(end)
        for gate, direction in SLOPES.items():
            neighbor = end + direction
            if grid[neighbor] == gate:
                queue.append((end, direction))
    return edges


def possible_paths(edges, start, end, current_distance, seen):
    """Find the length of the possible paths"""
    if start in seen:
        return
    if start == end:
        yield current_distance
        return
    seen.add(start)
    for edge, distance in edges[start]:
        dist = current_distance + distance
        yield from possible_paths(edges, edge, end, dist, seen)
    seen.remove(start)


def solve(part="a"):
    """Solve puzzle"""
    grid = load_map()
    edges = make_graph(grid, part == "a")
    # for start, destinations in edges.items():
    #     for dest, distance in destinations:
    #         print(distance, start, dest)
    start = min(grid) + (0, 1)
    end = max(grid) + (0, -1)
    distances = list(possible_paths(edges, start, end, 0, set()))
    print(len(distances), len(edges))
    return max(distances)


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
