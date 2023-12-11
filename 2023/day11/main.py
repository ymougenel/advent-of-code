#!/usr/bin/env python3
import time

empty_rows = []
empty_cols = []
stars = []


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def solve_part(expansion):
    distance = 0
    for i in range(len(stars)):
        for j in range(i + 1, len(stars)):
            distance = calculate_distance(stars[i], stars[j], expansion)
    return distance


def detect_empy_rows(map):
    global empty_rows
    empty_rows = []
    for i in range(len(map)):
        valid = True
        j = 0
        while valid and j < len(map[0]):
            valid = map[i][j] == "."
            j += 1
        if valid:
            empty_rows.append(i)


def detect_empy_cols(map):
    global empty_cols
    empty_cols = []
    for j in range(len(map[0])):
        valid = True
        i = 0
        while valid and i < len(map):
            valid = map[i][j] == "."
            i += 1
        if valid:
            empty_cols.append(j)


def detect_stars(map):
    global stars
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "#":
                stars.append((i, j))


def calculate_distance(star1, star2, expansion):
    i_min = min(star1[0], star2[0])
    i_max = max(star1[0], star2[0])
    j_min = min(star1[1], star2[1])
    j_max = max(star1[1], star2[1])
    distance = 0
    for i in range(i_min, i_max):
        if i in empty_rows:
            distance += expansion
        else:
            distance += 1
    for j in range(j_min, j_max):
        if j in empty_cols:
            distance += expansion
        else:
            distance += 1
    return distance


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    map = read_file("inputs/example1.txt")
    map = read_file("inputs/input.txt")
    detect_empy_rows(map)
    detect_empy_cols(map)
    detect_stars(map)
    print("Part 1: " + str(solve_part(2)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    print("Part 2: " + str(solve_part(1000000)))
