#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/18
"""
from PIL import Image, ImageDraw
from point import Point2D, direction_cardinals
import aoc

PUZZLE = aoc.Puzzle(day=18, year=2023)


def transpose(point):
    """Swap the axes of point"""
    return Point2D(*point[::-1])


def display(corners, highlight=None):
    """Create and display a new image of the lagoon"""
    xmin = min(p.x for p in corners)
    ymin = min(p.y for p in corners)
    xmax = max(p.x for p in corners)
    ymax = max(p.y for p in corners)
    size = Point2D(ymax, xmax) - Point2D(ymin, xmin) + (10, 10)
    xshift = -min(0, xmin) + 5
    yshift = -min(0, ymin) + 5
    shift = Point2D(yshift, xshift)
    points = [transpose(x) + shift for x in corners]

    img = Image.new("RGB", size)
    draw = ImageDraw.Draw(img)
    draw.polygon(points, fill="red")
    if highlight:
        print(f" highlighting {highlight}")
        draw.point([transpose(highlight)], "red")
    img.show()


def solve(part="a"):
    """Solve puzzle"""
    directions = direction_cardinals
    if part == "b":
        directions = {
            "0123"[i]: direction_cardinals[d]
            for i, d in enumerate("RDLU")
        }
    corners = []
    current = Point2D(0, 0)
    # find all of the corners
    for line in PUZZLE.input.splitlines():
        dest, count, color = line.split()
        if part == "b":
            dest, count = color[-2], int(color[2:-2], 16)
        count = int(count)
        current += directions[dest] * count
        corners.append(current)
        # print(dest, count, current)

    # use shoelace formula to calculate the area
    # https://www.jamestanton.com/wp-content/uploads/2012/03/Cool-Math-Essay_June-2014_SHOELACE-FORMULA.pdf
    # add 1/2 of the perimeter to adjust for unit calculations
    #   rect(0,0 to 2,6) is really 3*7
    # not sure how to explain the final `+1` yet
    # the use of -1 as the start to enumerate allows this to "wrap around"
    total = 0
    perimeter = 0
    for prev, current in enumerate(corners, -1):
        previous = corners[prev]
        total += previous.x * current.y - previous.y * current.x
        perimeter += current.distance(previous)
    total = (abs(total) + perimeter) // 2
    return total + 1


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
