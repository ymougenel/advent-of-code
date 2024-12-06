#!/usr/bin/env python3
import time


def read_file(file_name):
    order_rules = {}
    updates = []
    with open(file_name) as input_file:
        lines = input_file.read().splitlines()

        updating = False
        for line in lines:
            if line == "":
                updating = True
            elif updating:
                updates.append([int(i) for i in line.split(',')])
            else:
                line = line.split('|')
                e1 = int(line[0])
                e2 = int(line[1])
                if e2 in order_rules:
                    order_rules[e2].append(e1)
                else:
                    order_rules[e2] = [e1]
    return order_rules, updates


def solve_part1(ordering_rules, updates):
    count = 0
    for update in updates:
        valid = True
        for i in range(len(update)):
            cur_elt = update[i]
            if valid and cur_elt in ordering_rules:
                elements_before = ordering_rules[cur_elt]
                for j in range(i, len(update)):
                    if update[j] in elements_before:
                        valid = False
        if valid:
            count += update[len(update) // 2]
    return count


def solve_part2(ordering_rules, updates):
    count = 0
    invalids = []
    for update in updates:
        valid = True
        for i in range(len(update)):
            cur_elt = update[i]
            if valid and cur_elt in ordering_rules:
                elements_before = ordering_rules[cur_elt]
                for j in range(i, len(update)):
                    if valid and update[j] in elements_before:
                        invalids.append(update)
                        valid = False

    for update in invalids:
        i = 0
        while i < len(update):
            smallest = i
            for j in range(i + 1, len(update)):
                if smallest == i and update[i] in ordering_rules and update[j] in ordering_rules[update[i]]:
                    smallest = j
            if smallest != i:
                update[i], update[smallest] = update[smallest], update[i]
            else:
                i += 1
        count += update[len(update) // 2]
    return count


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    ordering_rules, updates = data
    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(ordering_rules, updates)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(ordering_rules, updates)))
    print("-> Part2 solved in: ", (time.time() - start_time))
