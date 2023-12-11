#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        lines = [line for line in input_file.read().splitlines()]
        values = []
        for line in lines:
            values.append([int(i) for i in line.split()])
        return values


def generate_next_diff(line):
    res = []
    for i in range(0, len(line) - 1):
        res.append(line[i + 1] - line[i])
    return res


def generate_line_diff(line):
    diffs = [line]
    while len([i for i in diffs[-1] if i != 0]) != 0:
        diff = generate_next_diff(diffs[-1])
        diffs.append(diff)
    return diffs


def predict_next_value(diffs):
    for i in range(len(diffs) - 1, 0, -1):
        diffs[i - 1].append(diffs[i - 1][-1] + diffs[i][-1])
    return diffs[0][-1]

def deduce_previous_value(diffs):
    for i in range(len(diffs) - 1, 0, -1):
        diffs[i - 1][0] = diffs[i - 1][0] - diffs[i][0]
    return diffs[0][0]
def solve_parts(data):
    total_before = 0
    total_after = 0
    for line in data:
        diffs = generate_line_diff(line)
        total_after += predict_next_value(diffs)
        total_before += deduce_previous_value(diffs)
    return total_before, total_after


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    part2, part1 = solve_parts(data)
    print("Part 1: " + str(part1))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    print("Part 2: " + str(part2))
