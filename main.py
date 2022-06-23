import sys
import time
from pynput.keyboard import Key, Listener, Controller
from board import Board
from snake import Snake

BOARD_WIDTH = 30
BOARD_HEIGHT = 20
key_pressed = None

def on_press(key):
    global key_pressed
    key_pressed = key

def on_release(key):
    return False

def main():
    board = Board(BOARD_WIDTH, BOARD_HEIGHT, Snake(BOARD_WIDTH, BOARD_HEIGHT))
    board.update_board()

    while True:
        l = Listener(on_press=on_press, on_release=on_release)
        l.start()
        time.sleep(0.1)

        if key_pressed == Key.up:
            board.snake.turn_up()
        elif key_pressed == Key.left:
            board.snake.turn_left()
        elif key_pressed == Key.down:
            board.snake.turn_down()
        elif key_pressed == Key.right:
            board.snake.turn_right()
        elif key_pressed == Key.esc:
            sys.exit()

        board.update_board()

if __name__ == '__main__': main()
