#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def solve_part1(grid):
    accessed_paper = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@" and find_adjacent_rolls(grid, i, j) < 4:
                accessed_paper.append((i, j))
    return len(accessed_paper)


def solve_part2(data):
    return data


def find_adjacent_rolls(grid, i, j):
    count_rolls = 0
    for m in range(-1, 2):
        for n in range(-1, 2):
            if (m, n) != (0, 0):
                if is_in_range(grid, i + m, j + n) and grid[i + m][j + n] == '@':
                    count_rolls += 1
    return count_rolls


def is_in_range(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
