import os
from snake import Snake
from snake import Coord
from random import random

BOARD_TILE = '.'
SNAKE_TILE = ' '
PELLET_TILE = '0'

class Game:
    def __init__(self, board_rows, board_cols, snake: Snake):
        self.game_over = False
        self.board_rows = board_rows
        self.board_cols = board_cols
        self.board = [['.' for _ in range(board_rows)] for _ in range(board_cols)]
        self.snake = snake
        self.pellet = Coord(int(random() * board_rows), int(random() * board_cols))

        self.draw_snake()

        os.system('clear')

    def draw_snake(self):
        """
        Reset the board and draw the snake on it again
        """
        self.board = [['.' for _ in range(self.board_rows)] for _ in range(self.board_cols)]

        for coord in self.snake.body:
            self.board[coord.y][coord.x] = SNAKE_TILE

    def check_pellet_eaten(self):
        """
        If the head of the snake is on the pellet, make the snake bigger and respawn the pellet
        """
        if self.snake.body[-1].x == self.pellet.x and self.snake.body[-1].y == self.pellet.y:
            self.pellet = Coord(int(random() * self.board_rows), int(random() * self.board_cols))
            self.snake.grow()

    def update_board(self):
        collided = self.snake.update()

        if collided:
            self.game_over = True
            return

        self.check_pellet_eaten()
        
        # draw the snake and pellet on the board
        self.board = [['.' for _ in range(self.board_rows)] for _ in range(self.board_cols)]

        self.board[self.pellet.y][self.pellet.x] = PELLET_TILE

        for coord in self.snake.body:
            self.board[coord.y][coord.x] = SNAKE_TILE

        print('\033[1;1f', end='')
        for i in range(len(self.board)):
            print('\033[2K', end='') # clear the line
            
            for j in range(len(self.board[i])):
                if self.board[i][j] == SNAKE_TILE:
                    print('\033[2;0;41m', end='')
                elif self.board[i][j] == PELLET_TILE:
                    print('\033[1;36m', end='')

                print(self.board[i][j], end=' ')
                print('\033[0m', end='')

            print()

        print('\033[2K', end='') # clear the line

    def show_game_over(self):
        print('\033[2J', end='')
        print(f'\033[1;1f', end='')
        print('\033[31mGAME OVER\033[0m')
