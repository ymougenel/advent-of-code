#!/usr/bin/env python3
import math
import time

directions = ""
steps_count = 0


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines() if line != ""]


def parse_nodes(data):
    global directions
    directions = data[0]
    elements = {}
    for i in range(1, len(data)):
        line = data[i]
        elements[line[0:3]] = (line[7:10], line[12:15])
    return elements


def forward(current, elements):
    dir = directions[steps_count % len(directions)]
    return choose(current, elements, dir)


def choose(current, elements, dir):
    toward = elements[current]
    if dir == "L":
        return toward[0]
    else:
        return toward[1]


def solve_part1(elements):
    global steps_count
    current = "AAA"
    while current != "ZZZ":
        current = forward(current, elements)
        steps_count += 1

    return steps_count


def find_node_solutions(node):
    global steps_count
    steps_count = 0
    current = node
    solution = None
    paths = {}
    LEN_DIR = len(directions)
    while steps_count == 0 or (steps_count % LEN_DIR != 0) or current != node:
        current = forward(current, elements)
        steps_count += 1
        if current[2] == "Z":
            solution = steps_count
        walk = steps_count % LEN_DIR
        if walk in paths:
            if current in paths[walk]:
                return solution
            else:
                paths[walk].append(current)
        else:
            paths[walk] = [current]
    return solution


def solve_part2(elements):
    global steps_count
    nodes_solutions = [find_node_solutions(node) for node in elements if node[2] == "A"]
    res = 1
    gcd = math.gcd(*nodes_solutions)
    for sol in nodes_solutions:
        res *= (sol / gcd)
    return res * gcd


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    elements = parse_nodes(data)
    print("Part 1: " + str(solve_part1(elements)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")
    elements = parse_nodes(data)
    print("Part 2: " + str(solve_part2(elements)))
    print("Solved in : ", (time.time() - start_time))
