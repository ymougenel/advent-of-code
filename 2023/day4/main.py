#!/usr/bin/env python3
import time
import math


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


"""
Parse the lines into a list of cards
Each Cards contains:
    * The cards 1
    * The winning numbers
    * The drawn numbers
"""
def parse_cards(data):
    cards = []
    for line in data:
        card_number = int(line.split(':')[0].split(" ")[-1])
        numbers = line.split(":")[1].split("|")
        winning_numbers = list(map(int, numbers[0].split()))
        drawn_numbers = list(map(int, numbers[1].split()))
        cards.append((card_number, winning_numbers, drawn_numbers))
    return cards


def solve_part1(cards):
    total = 0
    for card in cards:
        # Count the winning numbers
        match_found = [d for d in card[2] if d in card[1]]
        if match_found:
            total += math.pow(2, len(match_found) - 1)
    return total


def solve_part2(cards):
    scratchcards = {}
    winning = {}

    # initialize scratchcards count to 1 and found winning number per cards
    for card in cards:
        winning[card[0]] = len([d for d in card[2] if d in card[1]])
        scratchcards[card[0]] = 1

    # Iterate over cards (waterfall)
    for number, winning_count in winning.items():
        for i in range(1, winning_count + 1):
            scratchcards[number + i] += 1 * scratchcards[number]

    return sum(scratchcards.values())


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    # data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    cards = parse_cards(data)
    print("Part 1: " + str(solve_part1(cards)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    # data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    cards = parse_cards(data)
    print("Part 2: " + str(solve_part2(cards)))
