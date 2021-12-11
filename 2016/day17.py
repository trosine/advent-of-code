#!/usr/bin/env python3
"""
https://adventofcode.com/2016/day/17
"""
from collections import deque
from hashlib import md5
import operator

import aoc

PUZZLE = aoc.Puzzle(day=17, year=2016)
DIRECTIONS = {
    b'U': (0, -1),
    b'D': (0, 1),
    b'L': (-1, 0),
    b'R': (1, 0),
    }


def open_doors(pos, salt, path):
    """Generate the possible open doors"""
    # pulling an individual item from bytes() returns an int
    new_directions = (b'U', b'D', b'L', b'R')
    open_directions = md5(salt + path).hexdigest()
    for index, door_open in enumerate(open_directions[:4]):
        if door_open > 'a':
            next_direction = new_directions[index]
            # print(f'  i={index}, o={door_open}, n={next_direction}')
            new_x, new_y = map(operator.add, pos, DIRECTIONS[next_direction])
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                yield (new_x, new_y), path + next_direction


def solve(part='a'):
    """Solve puzzle"""
    salt = PUZZLE.input.encode()
    start = ((0, 0), b'')
    seen = set([start])
    queue = deque([start])
    valid_paths = []
    while queue:
        location, path = queue.popleft()
        for neighbor in open_doors(location, salt, path):
            if neighbor[0] == (3, 3):
                if part == 'a':
                    return neighbor[1].decode()
                valid_paths.append(len(neighbor[1]))
            elif neighbor not in seen:
                queue.append(neighbor)
            seen.add(neighbor)
    return max(valid_paths)  # part b


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
