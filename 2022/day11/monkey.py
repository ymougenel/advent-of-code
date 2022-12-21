class Monkey:
    def __init__(self, starting_items, operator, operation, test, if_true, if_false):
        self.items = starting_items
        self.operator = operator
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspection = 0
        self.count = 1

    def next_round(self, monkeys, division, reduction=False):
        give_away = []
        self.inspection += len(self.items)
        for item in self.items:
            worry = item
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
            if not reduction:
                worry = worry // division
            else:
                worry = worry % reduction
            if worry % self.test == 0:
                monkeys[self.if_true].receive(worry)
            else:
                monkeys[self.if_false].receive(worry)
        self.items = []
        return give_away

    def receive(self, item):
        self.items.append(item)
