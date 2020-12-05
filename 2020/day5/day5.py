#!/usr/bin/env python3
import math


def split_range(range, letter):
    middle = math.floor(range[0] + (range[1] - range[0]) / 2)
    if letter == "F" or letter == "L":
        return range[0], middle
    else:
        return middle + 1, range[1]


def process_passport_translation(passport):
    range = (0, 127)
    for letter in passport[0:7]:
        range = split_range(range, letter)
    row = range[0]
    if range[0] != range[1]:
        print("Error:" + passport)
    range = (0, 7)
    for letter in passport[7:]:
        range = split_range(range, letter)
    col = range[0]
    if range[0] != range[1]:
        print("Error:" + passport)
    return row, col


def process_passport(passport):
    row, col = process_passport_translation(passport)
    return get_seat_id(row, col)


def get_seat_id(row, col):
    return row * 8 + col


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


if __name__ == '__main__':
    passports = read_file("inputs/part1.input")
    result = [process_passport(seat) for seat in passports]
    print(max(result))

    print([missing for missing in range(0, 922) if missing not in result])
