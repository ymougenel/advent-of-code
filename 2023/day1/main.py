#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def read_digit(line, forward=True, digit_letters=False):
    DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    if forward:  # Read from left to right
        order = (0, len(line), 1)
    else:  # Read from right to left
        order = (len(line) - 1, -1, -1)

    i = order[0]
    # Search for the digit (finish at the end/begining of line)
    while i != order[1]:
        if line[i].isnumeric():  # Digit found
            return int(line[i])

        if digit_letters:
            for digit in DIGITS:
                if order[2] == 1:
                    begin = i
                    end = i + len(digit)
                else:
                    end = i + 1
                    begin = i - len(digit) + 1

                if begin >= 0 and end <= len(line) and digit == line[begin:end]:
                    return DIGITS.index(digit) + 1
        i += order[2]


def solve_part1(data):
    total = 0
    for line in data:
        res = str(read_digit(line, True)) + str(read_digit(line, False))
        total += int(res)
    return total


def solve_part2(data):
    total = 0
    for line in data:
        res = str(read_digit(line, True, True)) + str(read_digit(line, False, True))
        total += int(res)
    return total


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    # data = read_file("inputs/example1.txt")
    data = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(data)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    data = read_file("inputs/part1.input")
    print("Part 2: " + str(solve_part2(data)))
