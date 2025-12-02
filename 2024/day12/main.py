#!/usr/bin/env python3
import copy
import time

from nltk.sem.chat80 import borders


def read_file(file_name):
    with open(file_name) as input_file:
        return [[elt for elt in line] for line in input_file.read().splitlines()]


def discover(puzzle, i, j, current_elt, borders):
    area = 0
    if puzzle[i][j].islower() or puzzle[i][j] == ".":
        return 0, 0
    puzzle[i][j] = current_elt.lower()

    if match_element(puzzle, i, j, current_elt) and puzzle[i][j] != ".":
        area += 1
        for m in range(-1, 2):
            for n in range(-1, 2):
                if abs(m) + abs(n) == 1 and match_element(puzzle, i + m, j + n, current_elt):
                    res = discover(puzzle, i + m, j + n, current_elt, borders)
                    area += res[0]
                elif abs(m) + abs(n) == 1:
                    borders.append(((i, j, match_dir(m, n))))
    return area, borders


def match_dir(m, n):
    if m == 0 and n > 0:  # Right Border
        return "R"
    elif m == 0 and n < 0:  # Left Border
        return "L"
    elif m > 0 and n == 0:  # Bottom border
        return "B"
    elif m < 0 and n == 0:  # Top Border
        return "T"
    else:
        return "U"


def is_in_range(puzzle, i, j):
    return 0 <= i < len(puzzle) and 0 <= j < len(puzzle)


def match_element(puzzle, i, j, search_elt):
    return is_in_range(puzzle, i, j) and puzzle[i][j].upper() == search_elt


def solve_part1(puzzle):
    area_perimeters = []
    n = len(puzzle)
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] != "." and puzzle[i][j].isupper():
                new_area, borders = discover(puzzle, i, j, puzzle[i][j], [])
                if new_area != 0:
                    area_perimeters.append((puzzle[i][j], new_area, len(borders)))
    print(area_perimeters)
    return compute_price(area_perimeters)


def compute_price(area_perimeters):
    return sum([elt[1] * elt[2] for elt in area_perimeters])


def solve_part2(puzzle):
    area_perimeters = []
    n = len(puzzle)
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] != "." and puzzle[i][j].isupper():
                new_area, borders = discover(puzzle, i, j, puzzle[i][j], [])
                if new_area != 0:
                    area_perimeters.append((puzzle[i][j], new_area, borders))
    return compute_price_part_2(area_perimeters)


def compute_price_part_2(area_perimeters):
    total = 0
    for elt, area, borders in area_perimeters:
        count_perimeters = 0
        for i, j, b in borders:
            if b in ["L", "R"] and (i + 1, j, b) not in borders:
                count_perimeters += 1
            if b in ["B", "T"] and (i, j + 1, b) not in borders:
                count_perimeters += 1
        total += count_perimeters * area
    return total


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/example.txt")
    # data = read_file("inputs/example2.txt")
    # data = read_file("inputs/input.txt")
    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(copy.deepcopy(data))))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
