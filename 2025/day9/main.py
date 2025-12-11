#!/usr/bin/env python3
import time
import re


def read_file(file_name):
    with open(file_name) as input_file:
        return [parse_line(line) for line in input_file.read().splitlines()]


def parse_line(line):
    return [int(elt) for elt in re.compile(r'\d+').findall(line)]


def solve_part1(tiles_pos):
    max_area = 0
    for i in range(len(tiles_pos)):
        for j in range(i + 1, len(tiles_pos)):
            area = abs(tiles_pos[i][0] - tiles_pos[j][0] + 1) * abs(tiles_pos[i][1] - tiles_pos[j][1] + 1)
            max_area = max(max_area, area)
    return max_area


def solve_part2(tiles_pos):
    max_area = 0
    for k1 in range(len(tiles_pos)):
        for k2 in range(k1 + 1, len(tiles_pos)):
            tile1 = tiles_pos[k1]
            tile2 = tiles_pos[k2]
            area = abs(tiles_pos[k1][0] - tiles_pos[k2][0] + 1) * abs(tiles_pos[k1][1] - tiles_pos[k2][1] + 1)
            if area >= max_area:
                if [tile1[0], tile2[1]] in tiles_pos or [tile2[0], tile1[1]] in tiles_pos:
                    max_area = area
                    print(tiles_pos[k1], tiles_pos[k2], area)

    return max_area


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
