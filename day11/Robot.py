from Direction import Direction


class Robot:
    def __init__(self, x, y, direction=Direction.UP):
        self.x = x
        self.y = y
        self.direction = direction

    def paint(self, panel, value):
        panel[self.x][self.y] = value

    def move(self, rotation):
        currentValue = self.direction.value
        if rotation == 0:  # Turn Left
            self.direction = Direction((currentValue - 1) % 4)
        else:  # Turn Right
            self.direction = Direction((currentValue + 1) % 4)

        if self.direction == Direction.LEFT:
            self.x -= 1
        elif self.direction == Direction.RIGHT:
            self.x += 1
        elif self.direction == Direction.UP:
            self.y += 1
        elif self.direction == Direction.DOWN:
            self.y -= 1
        else:
            raise NotImplementedError

    def debug(self):
        print("Robot is: x=" + self.x + " y=" + self.y + " facing:" + self.direction)
