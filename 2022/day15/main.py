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
        distance = manhattan_distance(si, sj, bi, bj)
        max_i = max(max_i, si, bi)
        max_j = max(max_j, sj + distance)
        min_i = min(min_i, si, bi)
        min_j = min(min_j, sj - distance)
    min_i = abs(min_i)
    min_j = abs(min_j)

    values = []
    for sj, si, bj, bi in data:
        values.append((si + min_i, sj + min_j, bi + min_i, bj + min_j))

    i_row = 10 + min_i
    i_row = 2000000 + min_i
    row = ['.'] * (max_j + min_j + 1)

    for si, sj, bi, bj in values:
        rayon = manhattan_distance(si, sj, bi, bj)
        if si - rayon <= i_row <= si + rayon:
            start = max(0, sj - rayon + (abs(si - i_row)))
            end = min(len(row), sj + rayon - (abs(si - i_row)) + 1)
            for k in range(start, end):
                row[k] = "#"
    for si, sj, bi, bj in values:
        if si == i_row:
            row[sj] = "S"
        if bi == i_row:
            row[bj] = "B"
    return len([elt for elt in row if elt == "#"])


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
    print("Part 1: " + str(solve_part1(data)))
    data = read_file("inputs/part1.input")

    # Part 2
    data = read_file("inputs/part2.example")
    # data = read_file("inputs/part2.input")
    print("Part 2: " + str(solve_part2(data)))
