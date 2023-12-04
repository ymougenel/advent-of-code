#!/usr/bin/env python3
import time
import math


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def parse_cards(data):
    cards = []
    for line in data:
        card_number = int(line.split(':')[0].split(" ")[-1])
        numbers = line.split(":")[1].split("|")
        winning_numbers = [int(d) for d in numbers[0].strip().split(" ") if d != ""]
        drawn_numbers = [int(d) for d in numbers[1].strip().split(" ") if d != ""]
        cards.append((card_number, winning_numbers, drawn_numbers))
    return cards


def solve_part1(cards):
    total = 0
    for card in cards:
        match_found = [d for d in card[2] if d in card[1]]
        if match_found:
            total += math.pow(2, len(match_found) - 1)
    return total


def solve_part2(data):
    return data


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    # data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    cards = parse_cards(data)
    print("Part 1: " + str(solve_part1(cards)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    data = read_file("inputs/example2.txt")
    # data = read_file("inputs/input.txt")
    print("Part 2: " + str(solve_part2(cards)))
