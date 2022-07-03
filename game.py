import os
from snake import Snake
from snake import Coord
from random import random

BOARD_TILE = '.'
SNAKE_TILE = ' '
PELLET_TILE = '0'

class Game:
    def __init__(self, board_width, board_height):
        self.game_over = False
        self.board_width = board_width
        self.board_height = board_height
        self.board = [['.' for _ in range(board_width)] for _ in range(board_height)]
        self.snake = Snake(board_width, board_height)

        self.spawn_pellet()
        self.draw_snake()

        os.system('clear')

    def spawn_pellet(self):
        pellet_coord = Coord(int(random() * self.board_width), int(random() * self.board_height))

        # checks if a coordinate overlaps with snake body
        def coord_on_snake(coord: Coord):
            for b in self.snake.body:
                if coord.__eq__(b):
                    return True

            return False

        while coord_on_snake(pellet_coord):
            pellet_coord = Coord(int(random() * self.board_width), int(random() * self.board_height))

        self.pellet = pellet_coord

    def draw_snake(self):
        """
        Reset the board and draw the snake on it again
        """
        self.board = [['.' for _ in range(self.board_width)] for _ in range(self.board_height)]

        for coord in self.snake.body:
            self.board[coord.y][coord.x] = SNAKE_TILE

    def check_pellet_eaten(self):
        """
        If the head of the snake is on the pellet, make the snake bigger and respawn the pellet
        """
        if self.snake.body[-1].x == self.pellet.x and self.snake.body[-1].y == self.pellet.y:
            self.spawn_pellet()
            self.snake.grow()

    def update_board(self):
        collided = self.snake.update()

        if collided:
            self.game_over = True
            return

        self.check_pellet_eaten()
        
        # draw the snake and pellet on the board
        self.board = [['.' for _ in range(self.board_width)] for _ in range(self.board_height)]

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
        def print_blank_lines():
            for _ in range(int(self.board_height / 2)):
                print()

        print_blank_lines()
        print('\033[2J', end='')
        print(f'\033[1;1f', end='')
        print_blank_lines()
        print('\033[31mGAME OVER\033[0m')
        print_blank_lines()
