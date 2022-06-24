import sys
import time
from pynput.keyboard import Key, Listener, Controller
from game import Game
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
    game = Game(BOARD_WIDTH, BOARD_HEIGHT, Snake(BOARD_WIDTH, BOARD_HEIGHT))
    game.update_board()
    listeners = []

    while not game.game_over:
        listener = Listener(on_press=on_press, on_release=on_release)
        listener.start()
        listeners.append(listener)

        time.sleep(0.1)

        if key_pressed == Key.up:
            game.snake.turn_up()
        elif key_pressed == Key.left:
            game.snake.turn_left()
        elif key_pressed == Key.down:
            game.snake.turn_down()
        elif key_pressed == Key.right:
            game.snake.turn_right()
        elif key_pressed == Key.esc:
            sys.exit()

        game.update_board()
        
        if len(listeners) > 1:
            l = listeners.pop(0)
            l.stop()

    game.show_game_over()

if __name__ == '__main__': main()
