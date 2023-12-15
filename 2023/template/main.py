#!/usr/bin/env python3
import time

def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]

def solve_part1(data):
    return data

def solve_part2(data):
    return data

if __name__ == '__main__':

    # Parse input file
    data = read_file("inputs/example1.txt")
    #data = read_file("inputs/input.txt")

    # Part 1
    data = read_file("inputs/example1.txt")
    #data = read_file("inputs/input.txt")
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    # data = read_file("inputs/example2.txt")
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))

