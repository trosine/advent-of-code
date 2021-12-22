#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/20
"""
import itertools
import operator

import aoc

PUZZLE = aoc.Puzzle(day=20, year=2021)
WINDOW = tuple(itertools.product(range(-1, 2), repeat=2))


class Image:
    """An image of pixels"""

    def __init__(self, enhancer, data):
        self.default = '0'
        self.enhancer = enhancer
        self.toggle_default = enhancer[0] == '1'
        self.image = {}
        for row, line in enumerate(data):
            for col, char in enumerate(line):
                self.image[(row, col)] = char

    def __str__(self):
        last_row = None
        image = ''
        for pixel in self.pixels_to_enhance():
            if last_row != pixel[0]:
                image += '\n'
            bit = self.image.get(pixel, self.default)
            image += '#' if bit == '1' else '.'
            last_row = pixel[0]
        image += '\n'
        return image

    def enhance(self):
        """Enhance the image by 1 iteration"""
        new_image = {}
        for pixel in self.pixels_to_enhance():
            window = ''.join(
                self.image.get(w_pixel, self.default)
                for w_pixel in self.window(pixel)
                )
            new_image[pixel] = self.enhancer[int(window, 2)]
        self.image = new_image
        if self.toggle_default:
            self.default = '1' if self.default == '0' else '0'

    def lit(self):
        """Count the number of lit pixels"""
        total = 0
        for pixel in self.image.values():
            total += pixel == '1'
        return total

    def pixels_to_enhance(self):
        """Which pixels to enhance"""
        start = min(self.image.keys())
        end = max(self.image.keys())
        x_range = range(start[0]-1, end[0]+2)
        y_range = range(start[1]-1, end[1]+2)
        for pixel in itertools.product(x_range, y_range):
            yield pixel

    @staticmethod
    def window(pixel):
        """Generate a list of pixels for the given window"""
        for direction in WINDOW:
            yield tuple(map(operator.add, pixel, direction))


def solve(part='a'):
    """Solve puzzle"""
    iterations = 2 if part == 'a' else 50
    table = str.maketrans('.#', '01')
    data = PUZZLE.input.translate(table).splitlines()
    image = Image(data[0], data[2:])
    for _ in range(iterations):
        image.enhance()
    return image.lit()


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
