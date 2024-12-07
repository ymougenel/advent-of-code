#!/usr/bin/env python3
import time


def read_file(file_name):
    inputs = []
    with open(file_name) as input_file:
        lines = [line for line in input_file.read().splitlines()]
        for line in lines:
            tests_values = int(line.split(":")[0])
            numbers = [int(i) for i in line.split(":")[1].split(" ") if i != '']
            inputs.append((tests_values, numbers))
    return inputs


def solve_part1(data):
    res = 0
    for line in data:
        expected = line[0]
        operations = generate_operations(line[1])
        for op in operations:
            if expected == solve_operation(op, expected):
                res += expected
                break

    return res


def generate_operations(values, concatenation_activated=False, inputs=[[]]):
    outputs = []
    if len(values) == 1:
        for inp in inputs:
            outputs.append(inp + [values[0]])
        return outputs
    else:
        for inp in inputs:
            outputs.append(inp + [values[0], "+"])
            outputs.append(inp + [values[0], "*"])
            if concatenation_activated:
                outputs.append(inp + [values[0], "|"])

    return generate_operations(values[1:], concatenation_activated, outputs)


def solve_operation(operation, max= None):
    res = operation[0]
    for i in range(1, len(operation)):
        if operation[i] == "+":
            res += operation[i + 1]
        elif operation[i] == "*":
            res *= operation[i + 1]
        elif operation[i] == "|":
            res = int(str(res)+ str(operation[i+1]))
        if max and res > max:
            return res
    return res

def solve_part2(data):
    res = 0
    for line in data:
        expected = line[0]
        operations = generate_operations(line[1], True)
        for op in operations:
            if expected == solve_operation(op, expected):
                res += expected
                break

    return res


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
