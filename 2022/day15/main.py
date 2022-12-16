#!/usr/bin/env python3
import re
import numpy as np


def read_file(file_name):
    p = re.compile(r'-?\d+\.?\d*')  # Any positive/negative digit
    with open(file_name) as input_file:
        return [tuple(map(int, p.findall(line))) for line in input_file.read().splitlines()]


def display(map):
    for i in range(len(map)):
        print(map[i])


def place_sensors(data):
    max_i = 0
    max_j = 0
    min_i = 0
    min_j = 0
    for sj, si, bj, bi in data:
        max_i = max(max_i, si, bi)
        max_j = max(max_j, sj, bj)
        min_i = min(min_i, si, bi)
        min_j = min(min_j, sj, bj)
    min_i = abs(min_i)
    min_j = abs(min_j)


    values = []
    for sj, si, bj, bi in data:
        values.append((si + min_i, sj + min_j, bi + min_i, bj + min_j))

    i_row = 10 + min_i
    i_row = 2000000 + min_i
    row = ['.'] * (max_j + min_j + 1)
    for si, sj, bi, bj in values:
        for j in range(len(row)):
            if manhattan_distance(i_row, j, si, sj) <= manhattan_distance(si, sj, bi, bj):
                row[j] = "#"
    for si, sj, bi, bj in values:
        if si == i_row:
            row[sj] = "S"
        if bi == i_row:
            row[bj] = "B"
    return len([elt for elt in row if elt == "#"])

    """
    map = np.full((max_i + min_i + 1, max_j + min_j + 1), '.')
    map = [['.' for x in range(max_j + min_j + 1)] for y in range(max_i + min_i + 1)]
    for si, sj, bi, bj in values:
        map[si][sj] = "S"
        map[bi][bj] = "B"
        distance = manhattan_distance(si, sj, bi, bj)
        for i in range(-distance, distance + 1):
            for j in range(-distance + i, distance + 1 - i):
                place_empty(i, j, si, sj, map, distance)
        # print(si, sj, bi, bj)
        # display(map)
        # print()
    display(map)
    # return len([i for i in range(len(map[0])) if map[2000000 + min_i][i] == "#"])
    return len([i for i in range(len(map[0])) if map[10 + min_i][i] == "#"])"""



def place_empty(i, j, si, sj, map, distance):
    if is_in_range(si + i, sj + j, len(map), len(map[0])) \
            and manhattan_distance(si, sj, i + si, j + sj) <= distance \
            and map[si + i][sj + j] == ".":
        map[si + i][sj + j] = "#"


def manhattan_distance(i, j, k, l):
    return abs(i - k) + abs(j - l)


def is_in_range(i, j, height, width):
    return 0 <= i < height and 0 <= j < width


def solve_part1(data):
    return place_sensors(data)


def solve_part2(data):
    return data


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(data)))

    # Part 2
    data = read_file("inputs/part2.example")
    # data = read_file("inputs/part2.input")
    print("Part 2: " + str(solve_part2(data)))
