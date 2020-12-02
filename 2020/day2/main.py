#!/usr/bin/env python3


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def validate(line):
    parts = line.split(" ")
    min = parts[0].split("-")[0]
    max = parts[0].split("-")[1]
    letter = parts[1][0]
    occurence = parts[2].count(letter)
    return int(min) <= occurence and occurence <= int(max)



if __name__ == '__main__':
    # data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    valid_pass = 0
    for line in data:
        if (validate(line)):
            valid_pass += 1
    print(valid_pass)
