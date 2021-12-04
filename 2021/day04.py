#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/4
"""
import itertools

import aoc

PUZZLE = aoc.Puzzle(day=4, year=2021)


class Board():
    """Bingo board"""
    def __init__(self, board):
        self.board = board
        self.marked = [
            [False] * 5
            for _ in range(5)
            ]

    def mark(self, number):
        """Mark a number on the board"""
        for row, values in enumerate(self.board):
            if number in values:
                column = values.index(number)
                self.marked[row][column] = True
                break

    def is_bingo(self):
        """Check to see if bingo has been found"""
        for row in self.marked:
            if sum(row) == 5:
                return True
        for col in range(5):
            column = [self.marked[row][col] for row in range(5)]
            if sum(column) == 5:
                return True
        return False
        # According to the rules of the puzzle, diagonals don't count, but this
        # is how it would be implemented
        # diagonal = [self.marked[row][row] for row in range(5)]
        # if sum(diagonal) == 5:
        #     return True
        # diagonal = [self.marked[row][4-row] for row in range(5)]
        # return sum(diagonal) == 5

    def sum_unmarked(self):
        """Get sum of unmarked numbers"""
        total = 0
        for row, col in itertools.product(range(5), repeat=2):
            if not self.marked[row][col]:
                total += self.board[row][col]
        return total


def parse_board(board):
    """Parse bingo board"""
    new_board = []
    for row in board.splitlines():
        new_board.append(list(map(int, row.split())))
    return new_board


def solve(part='a'):
    """Solve puzzle"""
    boards = PUZZLE.input.split('\n\n')
    numbers = boards[0]
    boards = [Board(parse_board(b)) for b in boards[1:]]
    for drawn in map(int, numbers.split(',')):
        to_remove = []
        for board in boards:
            board.mark(drawn)
            if board.is_bingo():
                if part == 'a' or len(boards) == 1:
                    return board.sum_unmarked() * drawn
                # can't simply remove the board within the loop because it
                # messes up the iteration
                to_remove.append(board)
        for board in to_remove:
            boards.remove(board)
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
