#!/usr/bin/env python3
import time
import re


def read_file(file_name):
    with open(file_name) as input_file:
        content = [line for line in input_file.read().splitlines()]
        numbers = [[int(d) for d in parse_line(line)] for line in content[:-1]]
        operations = re.compile(r'[\+\*]').findall(content[-1])
    return numbers, operations

def parse_line(line):
    return re.compile(r'\d+').findall(line)

def solve_part1(numbers, operations):
    res = []
    for j in range(len(operations)):
        res.append(numbers[0][j])
        for i in range(1,len(numbers)):
            if operations[j] == "*":
                res[j] *= numbers[i][j]
            elif operations[j] == "+":
                res[j] += numbers[i][j]
    return sum(res)



def solve_part2(numbers, operations):
    return numbers, operations

if __name__ == '__main__':

    # Parse input file
    numbers, operations = read_file("inputs/example1.txt")
    numbers, operations = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(numbers, operations)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(numbers, operations)))
    print("-> Part2 solved in: ", (time.time() - start_time))

