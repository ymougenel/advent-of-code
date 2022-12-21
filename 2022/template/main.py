#!/usr/bin/env python3
import time

def read_file(file_name):
    with open(file_name) as input_file:
        return [int(line) for line in input_file.read().splitlines()]

def solve_part1(data):
    return data

def solve_part2(data):
    return data

if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/part1.example")
    #data = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(data)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    data = read_file("inputs/part2.example")
    #data = read_file("inputs/part2.input")
    print("Part 2: " + str(solve_part2(data)))
