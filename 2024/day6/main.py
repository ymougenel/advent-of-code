#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [[letter for letter in line] for line in input_file.read().splitlines()]

def run_simulation(puzzle):
    n = len(puzzle)
    starting_position = None
    direction = None
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] not in [".", "#"]:
                starting_position = (i, j)
                if puzzle[i][j] == "^":
                    direction = (-1, 0)
                elif puzzle[i][j] == ">":
                    direction = (0, 1)
                elif puzzle[i][j] == "<":
                    direction = (0, -1)
                else:
                    direction = (1, 0)
                puzzle[i][j] = direction

    i, j = starting_position
    out = False
    while not out:
        next_i = i + direction[0]
        next_j = j + direction[1]

        if not (0 <= next_i < n) or not (0 <= next_j < n):
            puzzle[i][j] = direction
            out = True
        elif puzzle[next_i][next_j] == "#":
            direction = turn(direction)
        else:
            puzzle[i][j] = "X"
            # display(puzzle)
            i, j = next_i, next_j
    # return True

def get_path(puzzle):
    path = []
    n = len(puzzle)
    count = 0
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] not in [".", "#"]:
                path.append((i,j))
    return path

def solve_part1(puzzle):
    run_simulation(puzzle)
    return len(get_path(puzzle))


def display(puzzle):
    for line in puzzle:
        print(line)
    print()


def turn(direction):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    index = directions.index(direction)
    return directions[(index + 1) % len(directions)]


def solve_part2(puzzle):
    return puzzle


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
