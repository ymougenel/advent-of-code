#!/usr/bin/env python3


def read_file(file_name):
    with open(file_name) as input_file:
        return [int(line) for line in input_file.read().splitlines()]


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    # data = read_file("inputs/part1.input")
    print(data)

    # Part 2
    # data = read_file("inputs/part2.example")
    data = read_file("inputs/part2.input")
    print(data)
