#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        content = input_file.read().splitlines()
        content = [c.split("-") for c in content[0].split(",")]
        return [(int(c[0]), int(c[1])) for c in content]


def solve_part1(data):
    return sum([sum(test_range_validity(c[0],c[1])) for c in data])


def solve_part2(data):
    return sum([sum(test_range_validity(c[0],c[1], False)) for c in data])


def test_range_validity(begin_range, end_range, part1=True):
    return [i for i in range(begin_range, end_range + 1) if not is_valid(i, part1)]

def is_valid(digit, part1=True):
    return part1 and is_valid_part1(digit) or not part1 and is_valid_part2(digit)

def is_valid_part1(digit):
    s = str(digit)
    if len(s) % 2 != 0:
        return True
    middle = len(s) // 2
    for i in range(middle):
        if s[i] != s[middle + i]:
            return True
    return False

def is_valid_part2(digit):
    s = str(digit)
    middle = len(s) // 2
    for i in range(0,middle):
        pattern = s[:i+1]
        if len(pattern) * s.count(pattern) == len(s):
            return False
    return True

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
