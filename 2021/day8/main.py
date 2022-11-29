#!/usr/bin/env python3



def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


if __name__ == '__main__':
    # Part 1
    SIZE = 1000
    data = read_file("inputs/part1.example")
    #data = read_file("inputs/part1.input")
    print(count_unique_number_segments(data))

    # Part 2
    print(values)
