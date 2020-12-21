#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/21
"""
import collections
import aoc

PUZZLE = aoc.Puzzle(day=21, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    all_ing = set()
    food = []
    counts = collections.Counter()
    # stage 1: preprocess, converting input data to a more usable form,
    # get the full set of ingredients, and the counts of each ingredient
    for line in PUZZLE.input.splitlines():
        ingredients, allergens = line.split(' (contains ')
        ingredients = set(ingredients.split())
        allergens = allergens.rstrip(')').split(', ')
        food.append((ingredients, allergens))
        all_ing.update(ingredients)
        counts.update(ingredients)

    # stage 2: determine the possibly allergenic ingredients
    # pylint: disable=unnecessary-lambda
    possible_ing = collections.defaultdict(lambda: all_ing.copy())
    # pylint: enable=unnecessary-lambda
    for ingredients, allergens in food:
        for allergen in allergens:
            # keep only ingredients that exist in all matching food lists
            possible_ing[allergen].intersection_update(ingredients)

    # stage 3: remove allergenic ingredients to find the safe ones
    non_allergenic = all_ing.copy()
    for uncertain_ing in possible_ing.values():
        non_allergenic.difference_update(uncertain_ing)
    if part == 'a':
        return sum([counts[safe] for safe in non_allergenic])

    # stage 4: determine which ingredient is which allergen
    result = []
    while len(possible_ing) > 0:
        allergens = [
            allergen
            for allergen, ingredients in possible_ing.items()
            if len(ingredients) == 1]
        for allergen in allergens:
            ingredients = possible_ing.pop(allergen)
            for remaining in possible_ing.values():
                remaining.difference_update(ingredients)
            result.append((allergen, ingredients.pop()))
    return ','.join([x[1] for x in sorted(result)])


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
