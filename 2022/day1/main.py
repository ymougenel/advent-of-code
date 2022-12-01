#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]

def get_weights(data):
    total = 0
    weights = []
    for line in data:
        if line == "":
            weights.append(total)
            total = 0
        else:
            total += int(line)
    return weights

if __name__ == '__main__':
    # Part 1
    #data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    res = get_weights(data)
    res.sort()
    print(res[-1])
    print(sum(res[-3:]))
    # Part 2
    # data = read_file("inputs/part2.example")
    data = read_file("inputs/part2.input")
    print(data)
