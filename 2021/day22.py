#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/22

Using lines to simplify this (upper case indicates an overlap):
aaaaaaaaa      bbbbbbb  (no overlap, b-min > a-max)
bbbbbbb  aaaaaaaaa      (no overlap, b-max < a-min)
aaaaaaBBBbbb            (partial overlap, a-min <= b-min <= a-max,
                        [only 1 of b-min or b-max in a-range])
aaaBBBBBBBaaaa          (full overlap, a-min <= (b-min, b-max) <= a-max,
                        [BOTH b-min AND b-max in a-range])

"""
import collections
import re

import aoc

PUZZLE = aoc.Puzzle(day=22, year=2021)
INTEGERS = re.compile(r'-?\d+')


CuboidT = collections.namedtuple('CuboidT', (
    'xmin',
    'xmax',
    'ymin',
    'ymax',
    'zmin',
    'zmax',
    ))


class Cuboid(CuboidT):
    """Represents a cuboid in 3-dimentional space"""

    def volume(self):
        """Calculate the volume of the cuboid"""
        return (self.xmax + 1 - self.xmin) \
            * (self.ymax + 1 - self.ymin) \
            * (self.zmax + 1 - self.zmin)

    def overlaps(self, other):
        """Determine if this cuboid overlaps other"""

        if self.xmin > other.xmax or self.xmax < other.xmin:
            return False
        if self.ymin > other.ymax or self.ymax < other.ymin:
            return False
        if self.zmin > other.zmax or self.zmax < other.zmin:
            return False
        return True

    def shared(self, other):
        """Create a new cuboid to represent the portion shared with other"""

        if not self.overlaps(other):
            return None
        return Cuboid(
            xmin=max(self.xmin, other.xmin),
            xmax=min(self.xmax, other.xmax),
            ymin=max(self.ymin, other.ymin),
            ymax=min(self.ymax, other.ymax),
            zmin=max(self.zmin, other.zmin),
            zmax=min(self.zmax, other.zmax),
            )

    def extents(self, other):
        """Get the cubes that extend beyond other"""

        shared = self.shared(other)
        if self.xmin < shared.xmin:
            yield self._replace(xmax=shared.xmin-1)
        if self.xmax > shared.xmax:
            yield self._replace(xmin=shared.xmax+1)

        # don't repeat pieces already reported
        kwargs = {
            'xmin': shared.xmin,
            'xmax': shared.xmax,
            }
        if self.ymin < shared.ymin:
            yield self._replace(ymax=shared.ymin-1, **kwargs)
        if self.ymax > shared.ymax:
            yield self._replace(ymin=shared.ymax+1, **kwargs)

        kwargs['ymin'] = shared.ymin
        kwargs['ymax'] = shared.ymax
        if self.zmin < shared.zmin:
            yield self._replace(zmax=shared.zmin-1, **kwargs)
        if self.zmax > shared.zmax:
            yield self._replace(zmin=shared.zmax+1, **kwargs)


def inject(lit, turn_on, new):
    """Inject the new cuboid into the set of lit cuboids"""
    queue = collections.deque([new])
    while queue:
        new_lit = set()
        to_check = queue.popleft()
        for orig in lit:
            if to_check.overlaps(orig):
                shared = to_check.shared(orig)
                # these extents stay lit
                for ext in orig.extents(to_check):
                    new_lit.add(ext)
                # any of these extents need to be checked for other overlaps
                for ext in to_check.extents(orig):
                    queue.append(ext)
                to_check = shared  # should enforce no other overlaps
            else:
                new_lit.add(orig)
        if turn_on:
            new_lit.add(to_check)
        lit = new_lit
    return lit


def solve(part='a'):
    """Solve puzzle"""
    init_cube = Cuboid(-50, 50, -50, 50, -50, 50)
    lit = set()
    rules = PUZZLE.input.splitlines()
    rule_count = len(rules)
    for rule_num, rule in enumerate(rules):
        coords = list(map(int, INTEGERS.findall(rule)))
        cuboid = Cuboid(*coords)
        if part == 'a':
            if not cuboid.overlaps(init_cube):
                continue
        print(f'adding cube {rule_num}/{rule_count}: {cuboid}', end='\r')
        lit = inject(lit, rule.startswith('on'), cuboid)
    print()
    total = 0
    for cube in lit:
        total += cube.volume()
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
