#!/usr/bin/env python3
import time
import re


def read_file(file_name):
    with open(file_name) as input_file:
        lines = [line for line in input_file.read().splitlines()]
        connections = {}
        for line in lines:
            key = line.split(":")[0]
            values = [elt for elt in line.split(":")[1].split(" ") if elt]
            connections[key] = values
        return connections


def parse_line(line):
    return re.compile(r'\d+').findall(line)


def solve_part1(connections):
    return len(extend_path(["you"], connections))


def extend_path(previous_path, connections):
    last_elt = previous_path[-1]
    all_paths = []
    for co in connections[last_elt]:
        if co == "out":
            all_paths.append(previous_path + ["out"])
        elif co not in previous_path:
            for discovered_path in extend_path(previous_path + [co], connections):
                if discovered_path:
                    all_paths.append(discovered_path)
    return all_paths


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
