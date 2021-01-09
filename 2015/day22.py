#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/22
"""
import copy
import aoc

PUZZLE = aoc.Puzzle(day=22, year=2015)


class Player:
    """Class to handle an individual player"""

    hitpoints = 50
    mana = 500
    used_mana = 0

    _effects = {}
    _spells = {
        'missile': 53,
        'drain': 73,
        'shield': 113,
        'poison': 173,
        'recharge': 229,
        }

    def __init__(self, boss_hp, boss_damage):
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage

    def __repr__(self):
        effects = ''.join(x[0] for x in self._effects)
        result = 'Player(' + ', '.join([
            f'I:{id(self)}',
            f'H:{self.hitpoints}',
            f'M:{self.mana}',
            f'U:{self.used_mana}',
            f'E:{effects})',
            f'  Boss(H:{self.boss_hp}, D:{self.boss_damage})',
            ])
        return result

    def allowed_spells(self):
        """Reduces spell list to what can be currently cast"""
        return [
            spell
            for spell, cost in self._spells.items()
            if cost < self.mana and spell not in self._effects
            ]

    def boss_attack(self):
        """Take the attack from the boss"""
        damage = self.boss_damage
        if 'shield' in self._effects:
            damage -= 7
        self.hitpoints -= max(1, damage)

    def cast(self, spell):
        """Cast a spell"""
        cost = self._spells[spell]
        getattr(self, f'_{spell}')()
        self.mana -= cost
        self.used_mana += cost

    def clone(self):
        """Clone this player"""
        cloned = copy.copy(self)
        # pylint: disable=protected-access
        cloned._effects = self._effects.copy()
        return cloned

    def run_effects(self):
        """Execute the current effects in play"""
        expired = []
        for effect in self._effects:
            effect_function = f'_{effect}_effect'
            getattr(self, effect_function)()
            self._effects[effect] -= 1
            if self._effects[effect] <= 0:
                expired.append(effect)
        for effect in expired:
            del self._effects[effect]

    def _missile(self):
        self.boss_hp -= 4

    def _drain(self):
        self.hitpoints += 2
        self.boss_hp -= 2

    def _shield(self):
        self._effects['shield'] = 6

    def _shield_effect(self):
        pass

    def _poison(self):
        self._effects['poison'] = 6

    def _poison_effect(self):
        self.boss_hp -= 3

    def _recharge(self):
        self._effects['recharge'] = 5

    def _recharge_effect(self):
        self.mana += 101


def find_wins(winners, player, hard=False):
    """Find the possible winning attack combos"""
    if hard:
        player.hitpoints -= 1
        if player.hitpoints <= 0:
            return
    if winners and player.used_mana > min(winners):
        # already found a better solution
        return
    player.run_effects()
    if player.boss_hp <= 0:
        winners.append(player.used_mana)
        return
    available = player.allowed_spells()
    if len(available) == 0:
        # no more spells available to cast
        return

    for spell in available:
        new_player = player.clone()
        new_player.cast(spell)
        # now, it's the boss's turn
        new_player.run_effects()
        if new_player.boss_hp <= 0:
            # this could have been from spell cast, or an effect
            winners.append(new_player.used_mana)
            continue
        new_player.boss_attack()
        if new_player.hitpoints <= 0:
            continue
        find_wins(winners, new_player, hard)


def solve(part='a'):
    """Solve puzzle"""
    boss_hp, boss_damage = [
        int(x.split(':')[1])
        for x in PUZZLE.input.splitlines()
        ]
    player = Player(boss_hp, boss_damage)
    winners = []
    find_wins(winners, player, part == 'b')
    return min(winners)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
