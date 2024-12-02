#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [[int(row) for row in line.split(" ")] for line in input_file.read().splitlines()]


def check_increase_decrease_range(liste, min_diff=1, max_diff=3):
    sign = None  # 1 for increase, -1 for decrease
    for i in range(len(liste) - 1):
        diff = liste[i + 1] - liste[i]

        if not sign and diff != 0:
            sign = diff / abs(diff)

        # Check that increase/decrease is under the min/max range and always the same direction
        if abs(diff) < min_diff or abs(diff) > max_diff or sign * diff < 0:
            return False
    return True


def solve_part1(data):
    return len([row for row in data if check_increase_decrease_range(row)])


def solve_part2(data):
    return data


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print(data)
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    # data = read_file("inputs/example2.txt")
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
