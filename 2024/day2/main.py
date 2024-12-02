#!/usr/bin/env python3
import time

def read_file(file_name):
    with open(file_name) as input_file:
        return [[int(row) for row in line.split(" ")] for line in input_file]


def check_increase_decrease_range(liste, min_diff=1, max_diff=3, tolerate=False):
    sign = 0  # 1 for increase, -1 for decrease
    for i in range(len(liste) - 1):
        diff = liste[i + 1] - liste[i]

        if diff != 0:
            new_sign = int(diff / abs(diff))

        # Check that increase/decrease is under the min/max range and always the same direction
        if abs(diff) < min_diff or abs(diff) > max_diff or new_sign * sign < 0:
            if tolerate:
                return (check_increase_decrease_range(liste[:i] + liste[i + 1:])
                        or (i > 0 and check_increase_decrease_range(liste[:i - 1] + liste[i:]))
                        or ((i < len(liste) - 1) and check_increase_decrease_range(liste[:i + 1] + liste[i + 2:])))
            else:
                return False
        sign = new_sign
    return True


def solve_part(data, tolerate=False):
    return len([row for row in data if check_increase_decrease_range(row, tolerate=tolerate)])


if __name__ == '__main__':
    # Parse input file
    # data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part(data, tolerate=True)))
    print("-> Part2 solved in: ", (time.time() - start_time))
