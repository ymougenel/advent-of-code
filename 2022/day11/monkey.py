class Monkey:
    def __init__(self, starting_items, operator, operation, test, if_true, if_false):
        self.items = starting_items
        self.operator = operator
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspection = {}
        self.count = 1

    def next_round(self):
        give_away = []
        for item in self.items:
            self.inspect(item)
            worry = item[1]
            if self.operation == "old":
                operation = worry
            else:
                operation = int(self.operation)
            if self.operator == "*":
                worry *= operation
            elif self.operator == "+":
                worry += operation
            elif self.operator == "-":
                worry -= operation
            elif self.operator == "/":
                worry /= operation
            worry = worry // 3
            if worry % self.test == 0:
                give_away.append(([item[0], worry], self.if_true))
            else:
                give_away.append(([item[0], worry], self.if_false))
        self.items = []
        return give_away

    def receive(self, item):
        self.items.append(item)

    def inspect(self, item):
        if item[0] in self.inspection:
            self.inspection[item[0]] += 1
        else:
            self.inspection[item[0]] = 1
