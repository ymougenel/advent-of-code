#!/usr/bin/env python3
import time
import re
import math


def read_file(file_name):
    with open(file_name) as input_file:
        return [parse_line(line) for line in input_file.read().splitlines()]


def parse_line(line):
    return [int(elt) for elt in re.compile(r'\d+').findall(line)]


def solve_part1(boxes):
    remaining_boxes = boxes.copy()

    circuits =
    return data


def find_shortest_boxes(boxes_list):
    min_dist = math.inf
    min_boxes = (None, None)
    for i in range(len(boxes_list)):
        for j in range(i + 1, len(boxes_list)):
            dist = get_distance(boxes_list[i], boxes_list[j])
            if dist < min_dist:
                min_dist = dist
                min_boxes = (boxes_list[i], boxes_list[j])
    return min_boxes


def get_distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]))


def solve_part2(data):
    return data


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    # data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
