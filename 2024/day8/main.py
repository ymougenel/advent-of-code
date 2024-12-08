#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [[letter for letter in line] for line in input_file.read().splitlines()]


def solve_part(puzzle, repeat):
    antenna = {}
    n = len(puzzle)
    # Find all antenna position (map: type as keys and positions as values)
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] != ".":
                element = puzzle[i][j]
                if element in antenna:
                    antenna[element].append((i, j))
                else:
                    antenna[element] = [(i, j)]

    # Goes throw the antenna
    for key, values in antenna.items():
        for i in range(len(values)):
            for j in range(len(values)):
                # If part 2, place antinodes on all antenna
                if repeat:
                    puzzle[values[i][0]][values[i][1]] = "#"
                if i != j:
                    # Get vector created from 2 antenna, and mark antinodes
                    vector = (values[i][0] - values[j][0], values[i][1] - values[j][1])
                    mark_antinodes_vector(values[i][0], values[i][1], puzzle, n, vector, repeat)

    return sum([line.count('#') for line in puzzle])


def mark_antinodes_vector(i, j, puzzle, n, vector, repeat=False):
    new_i, new_j = (i + vector[0], j + vector[1])
    if 0 <= new_i < n and 0 <= new_j < n:
        puzzle[new_i][new_j] = "#"
        mark_antinodes_vector(new_i, new_j, puzzle, n, vector, repeat)


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part(data, False)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    data = read_file("inputs/input.txt")
    start_time = time.time()
    print("Part 2: " + str(solve_part(data, True)))
    print("-> Part2 solved in: ", (time.time() - start_time))
