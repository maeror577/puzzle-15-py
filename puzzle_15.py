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
        print('┌───' + '───┬───' * (self.size - 1) + '───┐')

        for row in range(self.size):
            current_row = [f'{tile:02}' if tile != self.end_state[-1][-1]
                else '  ' for tile in self.current_state[row]]
            print('│   ' + '   │   ' * (self.size - 1) + '   │')
            print('│  ' + '  |  '.join(current_row) + '  │')
            print('│   ' + '   │   ' * (self.size - 1) + '   │')
            if row < self.size - 1:
                print('├───' + '───┼───' * (self.size - 1) + '───┤')

        print('└───' + '───┴───' * (self.size - 1) + '───┘')


def main():
    """ Main game function. """
    board = Board()
    board.draw()

if __name__ == '__main__':
    main()
