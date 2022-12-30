#!/usr/bin/env python3
import time
import ast
import functools


def read_file(file_name):
    with open(file_name) as input_file:
        return [ast.literal_eval(line) for line in input_file.read().splitlines() if line != ""]


def solve_part1(data):
    right_order = []
    for i in range(0, len(data), 2):
        res = check_list(data[i], data[i + 1])
        if res > 0:
            right_order.append(1 + i // 2)
    print(right_order)
    return sum(right_order)


def solve_part2(data):
    data.append([[2]])
    data.append([[6]])
    organized = sorted(data, key=functools.cmp_to_key(check_list), reverse=True)
    return (1 + organized.index([[2]])) * (1 + organized.index([[6]]))


def min(data):
    mini = data[0]
    for elt in data:
        if check_list(mini, elt) == 1:
            mini = elt
    return elt


def check_integers(i1, i2):
    if i1 < i2:
        return 1
    elif i1 > i2:
        return -1
    else:
        return 0


def check_list(l1, l2):
    for i in range(len(l1)):
        if i >= len(l2):  # L2 run out of items
            return -1
        elt1, elt2 = l1[i], l2[i]
        if isinstance(elt1, int) and isinstance(elt2, int):
            res = check_integers(elt1, elt2)
            if res != 0:
                return res

        elif isinstance(elt1, int) and isinstance(elt2, list):
            elt1 = [elt1]

        elif isinstance(elt1, list) and isinstance(elt2, int):
            elt2 = [elt2]

        if isinstance(elt1, list):
            res = check_list(elt1, elt2)
            if res != 0:
                return res

    return len(l2) - len(l1)


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(data)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    print("Part 2: " + str(solve_part2(data)))
