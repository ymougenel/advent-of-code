#!/usr/bin/env python3
import math
import time
import numpy as np
from collections import Counter

infos = {}


def read_file(file_name):
    with open(file_name) as input_file:
        return [
            [int(i) for i in line]
            for line in input_file.read().splitlines()]


def visit(vortex, map, info, visited=[]):
    distance_start = info[vortex][0]
    i, j = vortex
    for k in [-1, 1]:
        update_distance((i + k, j), vortex, distance_start, map, info)
        update_distance((i, j + k), vortex, distance_start, map, info)
    current = info[vortex]
    info[vortex] = (current[0], current[1], True)


def solve(map, info):
    visited = []
    info[(0, 0)] = (0, None, False)
    while info[(len(map) - 1, len(map[0]) - 1)][0] == math.inf and len(visited) < len(map) * len(map[0]):
        closer_vortex = get_closer(info, visited)
        visit(closer_vortex, map, info, visited)


def get_closer(info, visited):
    min_dist = math.inf
    closer_vortex = None
    for vortex in info.keys():
        if info[vortex][0] < min_dist and not info[vortex][2]:
            min_dist = info[vortex][0]
            closer_vortex = vortex
    return closer_vortex


def update_distance(child_vortex, parent_vortex, distance_start, map, info):
    i, j = child_vortex
    if is_in_range(i, j, map):
        child_current_distance = info[child_vortex][0]
        if child_current_distance > distance_start + map[i][j]:
            info[child_vortex] = (distance_start + map[i][j], parent_vortex, info[child_vortex][2])


def is_in_range(i, j, map):
    return 0 <= i < len(map) and 0 <= j < len(map[0])


def extend_map(map):
    extended_map = [[0 for i in range(len(map) * 5)]
                    for j in range(len(map[0]) * 5)]
    for i in range(len(extended_map)):
        for j in range(len(extended_map[0])):
            reduced_i = i % len(map)
            reduced_j = j % len(map[0])
            i_factor = i // len(map)
            j_factor = j // len(map[0])
            new_value = map[reduced_i][reduced_j] + i_factor + j_factor
            if new_value > 9:
                new_value = new_value % 9
            extended_map[i][j] = new_value

    return extended_map


def init_infos(map):
    infos = {}
    # print(map)
    for i in range(len(map)):
        for j in range(len(map[0])):
            infos[(i, j)] = (math.inf, None, False)
    return infos


if __name__ == '__main__':
    start_time = time.time()

    # Init
    # map = read_file("inputs/part1.example")
    # map = read_file("inputs/my_example")
    map = read_file("inputs/part1.input")

    # Part 1
    # infos = init_infos(map)
    # solve(map, infos)

    # Part 2
    infos = init_infos(map)
    map = extend_map(map)
    infos = init_infos(map)

    print("Cavern size:,", len(map), len(map[0]), len(map) * len(map[0]))

    solve(map, infos)
    print(infos[(len(map) - 1, len(map[0]) - 1)])
    print("--- %s seconds ---" % (time.time() - start_time))
