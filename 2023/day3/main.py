#!/usr/bin/env python3
import time

processed = []
def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def is_in_range(data, i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0])


def detect_number(data, i, j):
    global processed
    if (i, j) not in processed and is_in_range(data, i, j) and data[i][j].isnumeric():
        processed.append((i, j))
        return detect_number(data, i, j - 1) + data[i][j] + detect_number(data, i, j + 1)
    else:
        return ""


def detect_number_neighbour(data, i, j):
    res = []
    res.append(detect_number(data, i, j - 1))
    res.append(detect_number(data, i, j + 1))
    if i - 1 >= 0 and data[i - 1][j].isnumeric():
        res.append(detect_number(data, i - 1, j))
    else:
        res.append(detect_number(data, i - 1, j - 1))
        res.append(detect_number(data, i - 1, j + 1))
    if i + 1 < len(data) and data[i + 1][j].isnumeric():
        res.append(detect_number(data, i + 1, j))
    else:
        res.append(detect_number(data, i + 1, j - 1))
        res.append(detect_number(data, i + 1, j + 1))
    return [int(val) for val in res if val != ""]


def solve_part1(data):
    numbers_found = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if not data[i][j].isnumeric() and data[i][j] != ".":  # Special character found
                numbers_found += detect_number_neighbour(data, i, j)
    total = 0
    for v in numbers_found:
        total += v
    return total

def solve_part2(data):
    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "*":  # Special character found
                numbers_found = detect_number_neighbour(data, i, j)
                if len(numbers_found) == 2:
                    total += numbers_found[0] * numbers_found[1]
    return total


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    print("Part 1: " + str(solve_part1(data)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    processed = []
    print("Part 2: " + str(solve_part2(data)))
