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
    visited.append(vortex)


def solve(map, info):
    visited = []
    info[(0, 0)] = (0, None)
    while info[(len(map)-1, len(map[0])-1)][0] == math.inf and len(visited) < len(map) * len(map[0]):
        closer_vortex = get_closer(info, visited)
        visit(closer_vortex, map, info, visited)


def get_closer(info, visited):
    min_dist = math.inf
    closer_vortex = None
    for vortex in info.keys():
        if info[vortex][0] < min_dist and vortex not in visited:
            min_dist = info[vortex][0]
            closer_vortex = vortex
    return closer_vortex


def update_distance(child_vortex, parent_vortex, distance_start, map, info):
    i, j = child_vortex
    if is_in_range(i, j, map):
        child_current_distance = info[child_vortex][0]
        if child_current_distance > distance_start + map[i][j]:
            info[child_vortex] = (distance_start + map[i][j], parent_vortex)


def is_in_range(i, j, map):
    return 0 <= i < len(map) and 0 <= j < len(map[0])


if __name__ == '__main__':
    start_time = time.time()

    # Part 1
    map = read_file("inputs/part1.example")
    map = read_file("inputs/my_example")
    # print(map)
    for i in range(len(map)):
        for j in range(len(map[0])):
            infos[(i, j)] = (math.inf, None)

    solve(map, infos)
    print(infos[(len(map) - 1, len(map[0]) - 1)])
