#!/usr/bin/env python3
import time
import copy

def read_file(file_name):
    with open(file_name) as input_file:
        return [[elt for elt in line] for line in input_file.read().splitlines()]


def find_element(puzzle, elt):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == elt:
                return i, j


explored = {}


def update_exporation(i, j, value):
    global explored
    if (i, j) in explored:
        if value < explored[(i, j)]:
            explored[(i, j)] = value
    else:
        explored[(i, j)] = value


to_explore = []


def explore(puzzle, i, j, prev_m, prev_n, points, path=[]):
    global to_explore
    # Check if end is reached
    if puzzle[i][j] == "E":
        update_exporation(i, j, points)
    else:
        # If already went there with shortest path
        if (i, j) in explored and explored[(i, j)] < points:
            return None
        else:
            update_exporation(i, j, points)
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if abs(m) + abs(n) == 1 and is_in_range(puzzle, i + m, j + n) and puzzle[i + m][j + n] != "#":
                        if (prev_m, prev_n) == (m, n):
                            to_explore.append((i + m, j + n, m, n, points + 1, count +1))
                        else:
                            to_explore.append((i + m, j + n, m, n, points + 1000 + 1, count + 1))


def is_in_range(puzzle, i, j):
    return 0 <= i < len(puzzle) and 0 <= j < len(puzzle[0])

def display(puzzle):
    new_puz = copy.deepcopy(puzzle)
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if (i,j) in explored:
                new_puz[i][j] = explored[(i,j)]
    for i in range(len(puzzle)):
        print(new_puz[i])


def solve_part1(puzzle):
    i, j = find_element(puzzle, "S")
    to_explore.append((i, j, 0, 1, 0))
    while to_explore:
        elt = to_explore.pop()
        explore(puzzle, *elt)
    print(explored[find_element(puzzle, "E")])
    # display(puzzle)
    return explored[find_element(puzzle, "E")]


def solve_part2(data):
    return data


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
