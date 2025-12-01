#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        lines = [line for line in input_file.read().splitlines()]
        return [(l[0], int(l[1:])) for l in lines]


def solve_part1(data):
    current = 50
    max = 100
    encountered_zero = 0
    for a, v in data:
        if a == 'L':
            current = (current - v) % max
        elif a == 'R':
            current = (current + v) % max
        if current == 0:
            encountered_zero += 1
        # print(a,v,current)
    return encountered_zero


def solve_part2(data):
    current = 50
    max = 100
    encountered_zero = 0
    for a, v in data:
        for i in range(0,v):
            if a == 'L':
                current -= 1
            elif a == 'R':
                current += 1
            current = current % max
            if current == 0:
                encountered_zero += 1
    return encountered_zero

if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
