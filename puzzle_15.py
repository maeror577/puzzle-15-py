""" The Game of Fifteen. """

import os
import random

CLEAR_SCREEN = 'cls' if os.name == 'nt' else 'clear'
SIZE = 4

class Board:
    """ Game Board class. """
    def __init__(self):
        self.size = SIZE
        self.end_state = [[(col + 1) + row*self.size
            for col in range(self.size)] for row in range(self.size)]
        self.current_state = self.setup()

    def setup(self):
        """ Initiation of the game board. """
        unwrapped = [tile for tiles in self.end_state for tile in tiles]
        random.shuffle(unwrapped)
        current_state = []
        for i in range(0, len(unwrapped), self.size):
            current_row = unwrapped[i:i+self.size]
            current_state.append(current_row)
        return current_state

    def draw(self):
        """ Draw current state of the game board. """
        os.system(CLEAR_SCREEN)
        screen_width = self.size * 8
        print('-' * screen_width)
        print('Game of Fifteen'.center(screen_width))
        print()
        print('controls: w a s d'.center(screen_width))
        print('-' * screen_width)

        for row in self.current_state:
            print('┌──────┐' * self.size)
            print('|      |' * self.size)
            for number in row:
                print('|  ', end='')
                print(f'{number:02}' if number != self.end_state[-1][-1]
                    else '  ', end='')
                print('  |', end='')
            print()
            print('|      |' * self.size)
            print('└──────┘' * self.size)

        print('-' * screen_width)
        print()

    def find_empty(self):
        """ Find coordinates of an empty cell. """
        for empty_x, row in enumerate(self.current_state):
            for empty_y, number in enumerate(row):
                if number == self.end_state[-1][-1]:
                    return empty_x, empty_y
        return None

    def make_move(self, direction):
        """ Move tile to an empty place. """
        if direction == 'w':
            shift_x, shift_y = 1, 0
        elif direction == 's':
            shift_x, shift_y = -1, 0
        elif direction == 'a':
            shift_x, shift_y = 0, 1
        elif direction == 'd':
            shift_x, shift_y = 0, -1
        empty_x, empty_y = self.find_empty()
        (self.current_state[empty_x][empty_y],
        self.current_state[empty_x + shift_x][empty_y + shift_y]) = \
        (self.current_state[empty_x + shift_x][empty_y + shift_y],
        self.current_state[empty_x][empty_y])

    def is_win(self):
        """ Check for a victory condition. """
        return self.current_state == self.end_state


def main():
    """ Main game function. """
    board = Board()
    while not board.is_win():
        board.draw()
        try:
            direction = input('Enter direction: ')
            board.make_move(direction)
        except (IndexError, ValueError, UnboundLocalError):
            pass
    board.draw()
    print('Puzzle solved!')

    restart = input('Do you want to play again? (y/n) ')
    if restart in ('y', 'Y'):
        main()

if __name__ == '__main__':
    main()
