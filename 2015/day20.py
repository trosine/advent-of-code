#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/20
"""
import itertools
import math
import aoc

PUZZLE = aoc.Puzzle(day=20, year=2015)


def sieve(maximum):
    """Initialize the known list of primes using Eratosthene sieve
    methodology
    """
    known_primes = []
    possible = [True] * maximum
    limit = int(math.sqrt(maximum))
    for candidate in range(2, limit):
        if possible[candidate]:
            known_primes.append(candidate)
            # using candidate**2 as start, because all prior have already
            # been marked as False
            # for example, when marking composites of 3, 6 is already marked
            # composites of 5: 10(2), 15(3), 20(2) are already marked
            for composite in range(candidate**2, maximum, candidate):
                possible[composite] = False
    # every candidate >= sqrt(maximum) is prime
    for candidate in range(limit, maximum):
        if possible[candidate]:
            known_primes.append(candidate)
    return known_primes


def factor(number):
    """Returns a list of prime factors that this number is composed of"""
    factors = []
    root = math.sqrt(number)
    for prime in PRIMES:
        if prime > number:
            break
        # reduce the total iterations
        if prime > root:
            factors.append(number)
            break
        while not number % prime:
            number //= prime
            factors.append(prime)
    return factors


# https://math.stackexchange.com/questions/22721/is-there-a-formula-to-calculate-the-sum-of-all-proper-divisors-of-a-number
def sum_of_factors(number, proper=False):
    """Returns the sum of all factors for number. If proper=False, includes
    number in the sum.
    """
    factors = number
    if isinstance(number, int):
        factors = factor(number)
    divisor_sum = 1
    for prime, group in itertools.groupby(factors):
        exponent = len(list(group))
        divisor_sum *= (prime ** (exponent + 1) - 1) // (prime - 1)
    if proper:
        divisor_sum -= number
    return divisor_sum


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        delivered = 10
    else:
        delivered = 11
    target = int(PUZZLE.input)
    house = 100000  # don't need to start at the very beginning
    while True:
        presents = delivered * sum_of_factors(house)
        if presents >= target and part == 'b':
            # because this is so costly, only do this when we're "close"
            removed = sum(x for x in range(1, house//50 + 1) if house % x == 0)
            presents -= delivered * removed

        if presents >= target:
            break
        house += 1
    return house


PRIMES = sieve(10000)
if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
