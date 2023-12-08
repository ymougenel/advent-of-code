#!/usr/bin/env python3
import math
import time

part1 = True


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def parse_card(c):
    if c.isnumeric():
        return int(c)
    elif c == "T":
        return 10
    elif c == "J":
        if part1:
            return 11
        else:
            return 0
    elif c == "Q":
        return 12
    elif c == "K":
        return 13
    elif c == "A":
        return 14


def parse_cards(data):
    hands = []
    for line in data:
        bet = int(line.split(" ")[-1])
        cards = [parse_card(c) for c in line.split(" ")[0]]
        hands.append((cards, get_strength(cards), bet))
    return hands


def get_strength(cards):
    count = {}
    for c in cards:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    maxi = 0
    pairs = 0
    J_count = 0
    for key, val in count.items():
        if val > maxi and (part1 or key != 0):
            maxi = val
        if val == 2 and (part1 or key != 0):
            pairs += 1
        if key == 0:
            J_count += val
    if not part1:
        maxi += J_count
    if J_count == 5:
        return 5
    else:
        if (maxi == 2 and pairs == 2) or (maxi == 3 and pairs == 1 and (part1 or J_count == 0)) or (
                not part1 and pairs == 2 and J_count > 0):
            maxi += 0.5
        return maxi


def solve_part1(cards):
    cards.sort(key=lambda x: (x[1], *x[0]))
    total = 0
    for i in range(len(cards)):
        total += (i + 1) * cards[i][2]
    return total


def solve_part2(data):
    return data


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    cards = parse_cards(data)
    print("Part 1: " + str(solve_part1(cards)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    part1 = False
    cards = parse_cards(data)
    print("Part 2: " + str(solve_part1(cards)))
