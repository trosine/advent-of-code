#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/4

Passport Processing

Count the number of valid passports (`cid` is optional, but all others
required.
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=4, year=2020)
REQUIRED = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    ])
VALID_ECLS = 'amb blu brn gry grn hzl oth'.split()
VALID_HCL = re.compile('#[0-9a-f]{6}$')


def parse_passport(passport):
    """Parse a passport into data"""
    fields = passport.split()
    parsed = {}
    for field in fields:
        key, val = field.split(':', 1)
        parsed[key] = val
    return parsed


def validate_height(value):
    """Determine if the height is correct"""
    height = int(value[0:-2])
    if value.endswith('cm'):
        return validate_number(height, 150, 193)
    if value.endswith('in'):
        return validate_number(height, 59, 76)
    return False


def validate_number(number, minimum, maximum):
    """Confirm that the number is parsable and with in the min/max"""
    integer = int(number)
    return minimum <= integer <= maximum


def validate_trivial(passport):
    """Determine if a passport is valid or not"""
    keys = set(passport.keys())
    return len(REQUIRED - keys) == 0


def validate_full(passport):
    """Determine if a passport is valid or not"""
    if validate_trivial(passport) == 0:
        return 0
    tests = [
        validate_number(passport['byr'], 1920, 2002),
        validate_number(passport['iyr'], 2010, 2020),
        validate_number(passport['eyr'], 2020, 2030),
        validate_height(passport['hgt']),
        VALID_HCL.match(passport['hcl']),
        passport['ecl'] in VALID_ECLS,
        len(passport['pid']) == 9,
        ]
    for test in tests:
        if not test:
            return 0
    return 1


def solve(part='a'):
    """Find the number of valid passports"""
    is_valid = validate_trivial
    if part == 'b':
        is_valid = validate_full
    passport = ''
    valid = 0
    data = PUZZLE.input.splitlines()
    data.append('')  # ensure the last passport is validated
    for line in data:
        if line == '':
            valid += is_valid(parse_passport(passport))
            passport = ''
        else:
            passport = passport + ' ' + line
    return valid


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
