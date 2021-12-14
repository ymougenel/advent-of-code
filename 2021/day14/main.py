#!/usr/bin/env python3
import time
from collections import Counter


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def insertion(polymer, rules):
    res = ""
    for i in range(0, len(polymer) - 1):
        current_letter = polymer[i]
        next_letter = polymer[i + 1]
        res += current_letter
        res += get_rule_instertion(current_letter + next_letter, rules)
    return res + polymer[-1]


def get_rule_instertion(letters, rules):
    for rule in rules:
        if rule[0] == letters:
            return rule[1]
    return ""


def get_tranformation(letters, rules, count):
    if count == 0:
        return letters
    else:
        letter_inserted = get_rule_instertion(letters, rules)
        return get_tranformation(letters[0] + letter_inserted, rules, count) + get_tranformation(
            letter_inserted + letters[1], rules, count)


if __name__ == '__main__':
    start_time = time.time()

    # Part 1
    data = read_file("inputs/part1.example")
    # data = read_file("inputs/part1.input")

    polymer = data[0]
    rules = [line.rsplit(" -> ") for line in data[2:]]

    for i in range(10):
        polymer = insertion(polymer, rules)
    occurences = Counter(polymer)
    print(max(occurences.values()) - min(occurences.values()))
