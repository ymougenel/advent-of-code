#!/usr/bin/env python3
import time

from nltk.sem.chat80 import borders


def read_file(file_name):
    with open(file_name) as input_file:
        return [[elt for elt in line] for line in input_file.read().splitlines()]


discovered = []


def discover(puzzle, i, j, current_elt):
    area, perimeter = 0, 0
    if match_element(puzzle, i, j, current_elt) and (i, j) not in discovered:
        discovered.append((i, j))
        area += 1
        borders = 4
        # sides = 4
        for m in range(-1, 2):
            for n in range(-1, 2):
                if abs(m) + abs(n) == 1 and match_element(puzzle, i + m, j + n, current_elt):
                    borders -= 1
                    res = discover(puzzle, i + m, j + n, current_elt)
                    area += res[0]
                    perimeter += res[1]
        perimeter += borders
    return area, perimeter


def match_element(puzzle, i, j, search_elt):
    return 0 <= i < len(puzzle) and 0 <= j < len(puzzle) and puzzle[i][j] == search_elt


def solve_part1(puzzle):
    global discovered
    discovered = []
    area_perimeters = []
    n = len(puzzle)
    for i in range(n):
        for j in range(n):
            new_area, new_perimeter = discover(puzzle, i, j, puzzle[i][j])
            if new_area != 0:
                area_perimeters.append((puzzle[i][j], new_area, new_perimeter))
    print(area_perimeters)
    return compute_price(area_perimeters)


def compute_price(area_perimeters):
    return sum([elt[1] * elt[2] for elt in area_perimeters])


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
