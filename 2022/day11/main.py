#!/usr/bin/env python3
import re

from monkey import Monkey


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def create_monkeys(data):
    re_digits = re.compile(r'\d+')
    monkeys = []

    for i in range(0, len(data), 7):
        starting_items = [(elt, elt) for elt in list(map(int, re_digits.findall(data[i + 1])))]
        operator = data[i + 2].split("=")[1].split(" ")[2]
        operation = data[i + 2].split("=")[1].split(" ")[3]
        test = int(re_digits.findall(data[i + 3])[0])
        if_true = int(re_digits.findall(data[i + 4])[0])
        if_false = int(re_digits.findall(data[i + 5])[0])
        monkeys.append(Monkey(starting_items, operator, operation, test, if_true, if_false))
    return monkeys


def solve_part1(data):
    monkeys = create_monkeys(data)
    for i in range(20):
        for monkey in monkeys:
            received = monkey.next_round()
            for item, monkey_dest in received:
                monkeys[monkey_dest].receive(item)
    counts = []
    for monkey in monkeys:
        count = 0
        for c in monkey.inspection:
            count += c
        counts.append(count)
    counts.sort()
    return counts[-1] * counts[-2]


def solve_part2(data):
    return data


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    # data = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(data)))

    # Part 2
    data = read_file("inputs/part2.example")
    # data = read_file("inputs/part2.input")
    print("Part 2: " + str(solve_part2(data)))
