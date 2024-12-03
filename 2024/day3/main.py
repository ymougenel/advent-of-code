#!/usr/bin/env python3
import time
import re

def read_file(file_name):
    with open(file_name) as input_file:
        return input_file.read()

def solve_part1(data):
    matches = re.findall(r'mul\((\d+),(\d+)\)', data)
    return sum([int(elt[0])* int(elt[1]) for elt in matches])

def solve_part2(data):
    print(data)
    matches = re.findall(r'(do\(\))|(don\'t\(\))|mul\((\d+,\d+)\)', data)
    enabled = True
    res = 0
    for group in matches:
        for elt in group:
            if elt == "do()":
                enabled = True
            elif elt == "don't()":
                enabled = False
            elif enabled and len(elt)>2: # Len check -> Fix for double quote capture
                m = elt.split(",")
                res += int(m[0]) * int(m[1])
    return res

if __name__ == '__main__':

    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/example2.txt")
    # data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))

