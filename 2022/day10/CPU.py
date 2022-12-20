class CPU:
    def __init__(self):
        self.register = 1
        self.cycle = 1
        self.remaining_cycle = 0
        self.counts = []
        self.crt = [["."] * 40 for i in range(6)]

    def noop(self, value):
        pass

    def addx(self, value):
        self.register += value

    def run(self, operation, value):
        self.cycle += 1
        self.draw()
        if self.remaining_cycle == 0:
            if operation == "addx":
                self.remaining_cycle = 2
            elif operation == "noop":
                self.remaining_cycle = 1

        self.remaining_cycle -= 1
        if self.remaining_cycle == 0:
            if operation == "addx":
                self.addx(int(value))
            elif operation == "noop":
                self.noop("value")

        if self.cycle % 40 == 20:
            self.counts.append(self.cycle * self.register)
        return self.remaining_cycle

    def draw(self):
        position = (self.cycle - 2) % 40
        print(self.cycle, position)
        if 0 <= self.register < 40:
            row = (self.cycle - 2) // 40
            if self.register - 1 <= position <= self.register + 1:
                self.crt[row][position] = "#"
