# Globals for the directions
# Change the values as you see fit
NORTH = "North"
EAST = "East"
SOUTH = "South"
WEST = "West"

SIDES = {
    NORTH: 1,
    EAST: 1,
    SOUTH: -1,
    WEST: -1,
}
SIDES_ROTATION = list(SIDES.keys())

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)

    def move(self, actions):
        for action in actions:
            if action == "R":
                self.turn_right()
            
            if action == "L":
                self.turn_left()
            
            if action == "A":
                self.do_advance()
        
    def turn_right(self):
        self._rotate(1)

    def turn_left(self):
        self._rotate(-1)

    def do_advance(self):
        if self.direction in [NORTH, SOUTH]:
            self.y_pos += SIDES[self.direction]

        if self.direction in [EAST, WEST]:
            self.x_pos += SIDES[self.direction]

        self.coordinates = (self.x_pos, self.y_pos)

    def _rotate(self, turn_step):
        self.direction = SIDES_ROTATION[
            (SIDES_ROTATION.index(self.direction) + turn_step) % len(SIDES_ROTATION)
        ]
