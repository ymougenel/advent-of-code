#!/usr/bin/env python3
import time
import re
from functools import reduce
from operator import mul

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
        for i in range(1, len(numbers)):
            if operations[j] == "*":
                res[j] *= numbers[i][j]
            elif operations[j] == "+":
                res[j] += numbers[i][j]
    return sum(res)


def read_file_part2(file_name):
    operations = []
    operations_indexes = []
    numbers = []

    with open(file_name) as input_file:
        content = [line for line in input_file.read().splitlines()]

        # Step1: Get all the symboles and their indexes
        for j in range(len(content[-1])):
            symbole = content[-1][j]
            if symbole in ["*", "+"]:
                operations.append(symbole)
                operations_indexes.append(j)

        # Step2: Make each digit line the same size
        longest_line_size = max([len(line) for line in content[:-1]])
        operations_indexes.append(longest_line_size+1) # This is for the last digits
        for i in range(len(content)-1):
            content[i] += ' ' * (longest_line_size - len(content[i]))

        # Step3: Process all the line digits WITH the spaces (based on the previous indexes)
        for j in range(len(operations_indexes) - 1):
            column = []
            for line in content[:-1]:
                str_number = line[operations_indexes[j]:operations_indexes[j + 1] - 1]
                column.append(str_number)
            numbers.append(column)

    return numbers, operations


def solve_part2(numbers, operations):
    res = 0
    for k in range(len(operations)):
        group= numbers[k]
        digital_values = []
        # Horizontal reading
        for j in range(len(group[0])):
            str_digit = ""
            # Vertical reading
            for i in range(len(group)):
                str_digit+=group[i][j]
            digital_values.append(int(str_digit))

        # Calculate sum or product of previous digits
        if operations[k] == "+":
            res += sum(digital_values)
        elif operations[k] == "*":
            res += reduce(mul, digital_values, 1)
    return res

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

    numbers, operations = read_file_part2("inputs/example1.txt")
    numbers, operations = read_file_part2("inputs/input.txt")
    print("Part 2: " + str(solve_part2(numbers, operations)))
    print("-> Part2 solved in: ", (time.time() - start_time))
