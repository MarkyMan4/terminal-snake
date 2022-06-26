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
        head = self.body[-1]

        # update the body - not including the head
        for i in range(len(self.body) - 1):
            self.body[i].x = self.body[i + 1].x
            self.body[i].y = self.body[i + 1].y
        
        # then move the head based on direction of movement
        if self.direction == Directions.UP:
            head.y -= 1
        elif self.direction == Directions.DOWN:
            head.y += 1
        elif self.direction == Directions.LEFT:
            head.x -= 1
        elif self.direction == Directions.RIGHT:
            head.x += 1

        def collided_with_self():
            for i in range(len(self.body) - 1):
                if head.__eq__(self.body[i]):
                    return True

            return False

        if (
            head.x < 0 
            or head.y < 0 
            or head.x >= self.board_width 
            or head.y >= self.board_height
            or collided_with_self()
        ):
            collided = True
        

        return collided

    # never allow snake to turn in opposite direction
    def turn_up(self):
        if self.direction != Directions.DOWN:
            self.direction = Directions.UP

    def turn_down(self):
        if self.direction != Directions.UP:
            self.direction = Directions.DOWN
        
    def turn_left(self):
        if self.direction != Directions.RIGHT:
            self.direction = Directions.LEFT

    def turn_right(self):
        if self.direction != Directions.LEFT:
            self.direction = Directions.RIGHT

    def grow(self):
        # Makes the snake bigger by one tile. Call this method when the snake eats a pellet        
        self.body.insert(0, Coord(self.prev_tail_pos.x, self.prev_tail_pos.y))
