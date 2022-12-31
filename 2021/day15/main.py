#!/usr/bin/env python3
import math
import bisect
import time
import numpy as np
from collections import Counter

infos = {}


def read_file(file_name):
    with open(file_name) as input_file:
        return [
            [int(i) for i in line]
            for line in input_file.read().splitlines()]


def visit(vortex, map, info, paths):
    i, j = vortex
    for k in [-1, 1]:
        update_distance((i + k, j), vortex, map, info, paths)
        update_distance((i, j + k), vortex, map, info, paths)
    current = info[vortex]
    info[vortex] = (current[0], current[1], current[2], True)


def solve(map, info):
    # Start at top left
    info[(0, 0)] = (0, get_distance(0, 0, map, 0), None, False)

    # While the end is not reached (distance = inf)
    paths = []
    for i in info.keys():
        paths.append((info[i][1], i))

    while info[(len(map) - 1, len(map[0]) - 1)][0] == math.inf:
        closer_vortex = paths[0]
        paths = paths[1:]
        visit(closer_vortex[1], map, info, paths)


def get_closer(info, distances):
    min_dist2 = math.inf
    closer_vortex = None
    for vortex in info.keys():
        info_vortex = info[vortex]
        if info_vortex[1] < min_dist2 and not info_vortex[3]:
            min_dist2 = info_vortex[1]
            closer_vortex = vortex
    return closer_vortex


def get_distance(i, j, map, distance_start):
    return int(math.sqrt(math.pow(len(map) - i, 2) + math.pow(len(map) - j, 2))) + map[i][j] + distance_start
    # return i * i + j * j + map[i][j] + distance_start


def update_distance(child_vortex, parent_vortex, map, info, paths):
    distance_start = info[parent_vortex][0]
    if info[parent_vortex][2] == child_vortex:
        return
    i, j = child_vortex
    if is_in_range(i, j, map):
        info_child = info[child_vortex]
        child_current_distance = info_child[0]
        if child_current_distance > distance_start + map[i][j]:
            try:
                paths.remove((child_current_distance, (i, j)))
            except ValueError:
                pass  # do nothing!

            bisect.insort(paths, (get_distance(i, j, map, distance_start), (i, j)))
            info[child_vortex] = (
                distance_start + map[i][j],
                get_distance(i, j, map, distance_start),
                parent_vortex,
                info_child[3])


def is_in_range(i, j, map):
    return 0 <= i < len(map) and 0 <= j < len(map[0])


def extend_map(map, extension=5):
    extended_map = [[0 for i in range(len(map) * extension)]
                    for j in range(len(map[0]) * extension)]
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
            infos[(i, j)] = (math.inf, math.inf, None, False)
    return infos


def print_path(infos, map):
    i_vortex = infos[(len(map) - 1, len(map[0]) - 1)]
    vortex = i_vortex[2]
    paths = []
    while vortex is not None:
        paths.append([vortex, i_vortex[0]])
        vortex = infos[vortex][2]
        if vortex:
            i_vortex = infos[vortex]
    paths.reverse()
    print(paths)


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
    map = extend_map(map, 5)
    infos = init_infos(map)

    print("Cavern size:,", len(map), len(map[0]), len(map) * len(map[0]))

    solve(map, infos)
    print(infos[(len(map) - 1, len(map[0]) - 1)])
    print("--- %s seconds ---" % (time.time() - start_time))
    print_path(infos, map)
