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
        insertion_letter = get_rule_instertion_dic(current_letter + next_letter, rules)
        res += current_letter + insertion_letter
        # res = f'{res}{current_letter}{insertion_letter}'
    return res + polymer[-1]


def get_rule_instertion(letters, rules):
    for rule in rules:
        if rule[0] == letters:
            return rule[1]
    return ""

def get_rule_instertion_dic(letters, rules):
    if letters in rules.keys():
        return rules[letters]
    else:
        return ""
def get_tranformation(letters, rules, count):
    if count == 0:
        return letters
    else:
        letter_inserted = get_rule_instertion_dic(letters, rules)
        return get_tranformation(letters[0] + letter_inserted, rules, count - 1)[0:-1] + get_tranformation(
            letter_inserted + letters[1], rules, count - 1)

def get_rules(data):
    rules = {}
    for line in data:
        l = line.rsplit(" -> ")
        left_el = l[0]
        right_el = l[1]
        if left_el not in rules.keys():
            rules[left_el] = right_el
        else:
            rules[left_el] = right_el
    return rules

if __name__ == '__main__':
    start_time = time.time()

    # Part 1
    data = read_file("inputs/part1.example")
    # data = read_file("inputs/part1.input")

    polymer = data[0]
    # rules = [line.rsplit(" -> ") for line in data[2:]]
    rules = get_rules(data[2:])

    print(get_tranformation("NN", rules, 30))
    # for i in range(20):
    #     polymer = insertion(polymer, rules)
    occurences = Counter(polymer)
    print(max(occurences.values()) - min(occurences.values()))
    print("--- %s seconds ---" % (time.time() - start_time))
