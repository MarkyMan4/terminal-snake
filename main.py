import sys
import termios
import time
import tty
from pynput.keyboard import Key, Listener, Controller
from board import Board
from snake import Snake

BOARD_WIDTH = 30
BOARD_HEIGHT = 20
inp_queue = []

def get_char():
    """
    Get a single character from stdin without the user having to press enter
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

def on_press(key):
    if key != Key.space:
        inp_queue.append(key)

def on_release(key):
    return False

def main():
    board = Board(BOARD_WIDTH, BOARD_HEIGHT, Snake(BOARD_WIDTH, BOARD_HEIGHT))
    board.update_board()
    keyboard = Controller()

    while True:
        l = Listener(on_press=on_press, on_release=on_release)
        l.start()
        time.sleep(0.1)

        # if no input after 0.5 seconds, press space so the game can keep going
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        l.join()

        # get the next input from the queue
        inp = ''
        if len(inp_queue) > 0:
            inp = inp_queue.pop(0)

        if inp == Key.up:
            board.snake.turn_up()
        elif inp == Key.left:
            board.snake.turn_left()
        elif inp == Key.down:
            board.snake.turn_down()
        elif inp == Key.right:
            board.snake.turn_right()
        elif inp == Key.esc:
            sys.exit()

        board.update_board()

if __name__ == '__main__': main()
