#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/5
"""
import re

import aoc

PUZZLE = aoc.Puzzle(day=5, year=2023)
NAME_PARSE = re.compile(r"(\w+)-to-(\w+)")


class PlantingRow():
    """Details a specific row in a mapping"""
    source = None
    dest = None
    shift = None
    count = None

    def __init__(self, dest, source, count):
        self.source = source
        self.dest = dest
        self.count = count
        self.shift = dest - source

    def __str__(self):
        return f"<PlantingRow({self.dest}, {self.source}, {self.count})>"

    def __contains__(self, source):
        offset = source - self.source
        if 0 <= offset < self.count:
            return True
        return False

    def get(self, source):
        """Return the destination value for the source or None"""
        if source in self:
            return source + self.shift
        return None


class PlantingMap():
    """Provides a source type to destination type mapping"""
    source = None
    dest = None
    table = None

    def __init__(self, desc, *table):
        self.source, self.dest = NAME_PARSE.match(desc).groups()
        self.table = []
        for row in table:
            self.table.append(PlantingRow(*map(int, row.split())))

    def get(self, source):
        """Return the destination value for the source item"""
        for row in self.table:
            if source in row:
                # print(f" (found {source} in {row}) ")
                return row.get(source)
        return source

    def fill_gaps(self):
        """Fill any gaps in the middle of the map"""
        table = list(sorted(self.table, key=lambda x: x.source))
        for index in range(len(table)-1):
            cur = table[index]
            next_ = table[index+1]
            if next_.source > cur.source + cur.count:
                cur_end = cur.source + cur.count
                new = PlantingRow(
                    dest=cur_end,
                    source=cur_end,
                    count=next_.source - cur_end,
                )
                self.table.append(new)

    def ensure_coverage(self, source, count):
        """Make sure this map covers both the start and end of the range"""
        self.table.sort(key=lambda x: x.source)
        my_start = self.table[0].source
        my_end = self.table[-1].source + self.table[-1].count - 1
        end = source + count - 1
        if source < my_start:
            new = PlantingRow(source, source, my_start-source)
            # print(f"Adding {new} to the start of {self.source} map")
            self.table.insert(0, new)
        if end > my_end:
            new = PlantingRow(my_end+1, my_end+1, end-my_end)
            # print(f"Adding {new} to the end of {self.source} map")
            self.table.append(new)

    def adjust_range(self, start, count):
        """Yields 1 or more ranges that have been shifted"""
        for row in self.table:
            if start in row:
                row_end = row.source + row.count - 1
                end = start + count - 1
                if end <= row_end:
                    yield (row.get(start), count)
                    return
                # split the range: the next row will continue the next section
                yield (row.get(start), row_end - start + 1)
                count -= (row_end - start + 1)
                start = row_end + 1

    def adjust_ranges(self, seeds):
        """Return an adjusted set of ranges after looking up items"""
        new_seeds = []
        for seed in seeds:
            self.ensure_coverage(*seed)
            added = list(self.adjust_range(*seed))
            # print(f"adjusting seed {seed} to {added}")
            new_seeds.extend(added)
        return new_seeds


def parse_seeds(seeds, part="a"):
    """Parse the line of seeds, returning a list of ranges"""
    data = [int(seed) for seed in seeds.split(": ")[1].split()]
    if part == "a":
        return [(seed, 1) for seed in data]
    result = []
    for offset in range(0, len(data), 2):
        start = data[offset]
        # end = start + data[offset+1]
        result.append((start, data[offset+1]))
    return result


def solve(part='a'):
    """Solve puzzle"""
    seeds = []

    for group in PUZZLE.input.split("\n\n"):
        if group.startswith("seeds:"):
            seeds = parse_seeds(group, part)
            continue
        mapping = PlantingMap(*group.splitlines())
        mapping.fill_gaps()
        seeds = mapping.adjust_ranges(seeds)

    return min(x[0] for x in seeds)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
