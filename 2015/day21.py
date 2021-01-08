#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/21
"""
import itertools
import aoc

PUZZLE = aoc.Puzzle(day=21, year=2015)
WEAPONS = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
    ]
ARMOR = [
    (0, 0, 0),  # no armor
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
    ]
RINGS = [
    (0, 0, 0),  # no ring
    (0, 0, 0),  # no ring
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    ]


class Character:
    """An RPG player or NPC"""

    equipment = []

    def __init__(self, hitpoints, damage, armor):
        self.hitpoints = hitpoints
        self._damage = damage
        self._armor = armor

    def _equip_total(self, offset):
        """Total an individual stat from all equipment"""
        return sum(x[offset] for x in self.equipment)

    @property
    def cost(self):
        """Cost of all equipment"""
        return self._equip_total(0)

    @property
    def damage(self):
        """Total damage"""
        return self._damage + self._equip_total(1)

    @property
    def armor(self):
        """Total armor"""
        return self._armor + self._equip_total(2)

    def __repr__(self):
        return f'<Character({self.hitpoints}, {self._damage}, {self._armor})>'


def solve(part='a'):
    """Solve puzzle"""
    player = Character(100, 0, 0)
    boss = Character(
        *[
            int(x.split(':')[1])
            for x in PUZZLE.input.splitlines()
            ]
        )
    weapons = itertools.combinations(WEAPONS, 1)
    armor = itertools.combinations(ARMOR, 1)
    rings = itertools.combinations(RINGS, 2)
    winners = []
    losers = []
    # equip 4 items - 1 weapon, 1 armor, 2 rings
    # the armor and rings can be worthless
    for equipment in itertools.product(weapons, armor, rings):
        player.equipment = list(itertools.chain.from_iterable(equipment))
        player_hits = boss.hitpoints // max(1, player.damage - boss.armor)
        boss_hits = player.hitpoints // max(1, boss.damage - player.armor)
        if player_hits <= boss_hits:
            winners.append(player.cost)
        else:
            losers.append(player.cost)
    if part == 'a':
        return min(winners)
    return max(losers)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
