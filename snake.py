from enum import Enum
from coord import Coord

class Directions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Snake:
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height

        # calculate where to put the snake, initially right in the center of the board
        x = int(board_width / 2)
        y = int(board_height / 2)

        # last item is the head of the snake
        self.body = [
            Coord(x - 1, y),
            Coord(x, y),
            Coord(x + 1, y)
        ]

        # keep track of previous tail position 
        # this is where a new tail will be added when the snake eats a pellet
        self.prev_tail_pos = Coord(self.body[0].x, self.body[0].y)

        self.direction = Directions.RIGHT

    def update(self) -> bool:
        """
        Moves the head of the snake in the direction of movement

        returns:
            bool - True if snake collided with itself or its own body, else false
        """
        self.prev_tail_pos = Coord(self.body[0].x, self.body[0].y)
        collided = False

        # update the body - not including the head
        for i in range(len(self.body) - 1):
            self.body[i].x = self.body[i + 1].x
            self.body[i].y = self.body[i + 1].y
        
        # then move the head based on direction of movement
        if self.direction == Directions.UP:
            self.body[-1].y -= 1
        elif self.direction == Directions.DOWN:
            self.body[-1].y += 1
        elif self.direction == Directions.LEFT:
            self.body[-1].x -= 1
        elif self.direction == Directions.RIGHT:
            self.body[-1].x += 1

        if self.body[-1].x < 0 or self.body[-1].y < 0 or self.body[-1].x >= self.board_width or self.body[-1].y >= self.board_height:
            collided = True

        return collided

    def turn_up(self):
        self.direction = Directions.UP

    def turn_down(self):
        self.direction = Directions.DOWN
        
    def turn_left(self):
        self.direction = Directions.LEFT

    def turn_right(self):
        self.direction = Directions.RIGHT

    def grow(self):
        # Makes the snake bigger by one tile. Call this method when the snake eats a pellet        
        self.body.insert(0, Coord(self.prev_tail_pos.x, self.prev_tail_pos.y))
