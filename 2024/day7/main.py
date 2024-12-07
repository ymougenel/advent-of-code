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
            if expected == solve_operation(op):
                res += expected
                break

    return res

def generate_operations(values, inputs=[[]]):
    outputs = []
    if len(values) == 1:
        for inp in inputs:
            outputs.append(inp + [values[0]])
        return outputs
    else:
        for inp in inputs:
            outputs.append(inp + [values[0], "+"])
            outputs.append(inp + [values[0], "*"])
    return generate_operations(values[1:], outputs)

def solve_operation(operation):
    res = operation[0]
    for i in range(1, len(operation)):
        if operation[i] == "+":
            res += operation[i+1]
        elif operation[i] == "*":
            res *= operation[i+1]
    return res
    # while operation:
    #     i = 0
        # while i < len(operation):
        #     if operation[i] == "*":
        #         operation[i] = operation[i-1] * operation[i+1]
        #         operation.pop(i-1)
        #         operation.pop(i+1)
        #     else:
        #         i += 1
    # return sum([i for i in operation if i != "+"])



def solve_part2(data):
    return data


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
