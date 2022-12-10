#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/7
"""
# pylint: disable=too-few-public-methods
import aoc

PUZZLE = aoc.Puzzle(day=7, year=2022)


class Directory:
    """Handles directories within the file system"""
    name = None
    parent = None
    subdirs = None
    files = None

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirs = {}
        self.files = {}

    # pylint: disable=invalid-name
    def du(self):
        """Calculates the total size of the directory"""
        total = 0
        for subdir in self.subdirs.values():
            total += subdir.du()
        for file in self.files.values():
            total += file.size
        return total


class File:
    """Handles files within the file system"""
    name = None
    parent = None
    size = 0

    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size


def parse_input():
    """Parse puzzle input"""
    root = Directory('/', None)
    dirs = [root]
    cwd = root
    for line in PUZZLE.input.splitlines():
        if line == '$ cd /':
            cwd = root
        elif line == '$ cd ..':
            cwd = cwd.parent
        elif line.startswith('$ cd'):
            _, _, directory = line.split()
            cwd = cwd.subdirs[directory]
        elif line == '$ ls':
            pass
        else:
            size, name = line.split()
            if size == 'dir':
                new = Directory(name, cwd)
                cwd.subdirs[name] = new
                dirs.append(new)
            else:
                cwd.files[name] = File(name, cwd, int(size))
    return dirs


def solve(part='a'):
    """Solve puzzle"""
    dirs = parse_input()
    sizes = []
    small_total = 0
    for directory in dirs:
        size = directory.du()
        sizes.append(size)
        if size <= 100000:
            small_total += size
    if part == 'a':
        return small_total

    sizes.sort()
    used = dirs[0].du()
    free = 70000000 - used
    needed = 30000000 - free
    print(f"  Used: {used}")
    print(f"  Free: {free}")
    print(f"  Need: {needed}")
    for size in sizes:
        if size >= needed:
            return size
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
