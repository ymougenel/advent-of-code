#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        lines = [line for line in input_file.read().splitlines()]
    puzzle = []
    directions = []
    is_puzzle = True
    for line in lines:
        if len(line) == 0:
            is_puzzle = False
        elif is_puzzle:
            puzzle.append(line)
        else:
            directions += list(line)

    return [list(elt) for elt in puzzle], directions


def find_initial_position(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == "@":
                return i, j


def can_move(position, dir, puzzle):
    new_i, new_j = position[0] + dir[0], position[1] + dir[1]
    if puzzle[new_i][new_j] == ".":
        return True
    elif puzzle[new_i][new_j] == "#":
        return False
    else:
        return can_move((new_i, new_j), dir, puzzle)


def move(position, dir, puzzle, before):
    i, j = position
    current_elt = puzzle[i][j]
    puzzle[i][j] = before
    if current_elt != ".":
        move((position[0] + dir[0], position[1] + dir[1]), dir, puzzle, current_elt)


def map_str_to_dir(str_dir):
    if str_dir == ">":
        return 0, 1
    elif str_dir == "<":
        return 0, -1
    elif str_dir == "^":
        return -1, 0
    elif str_dir == "v":
        return 1, 0
    else:
        return None


def solve_part1(data):
    puzzle, directions = data
    n = len(puzzle)
    position = find_initial_position(puzzle)
    for str_dir in directions:
        dir = map_str_to_dir(str_dir)
        if can_move(position, dir, puzzle):
            puzzle[position[0]][position[1]] = '.'
            position = position[0] + dir[0], position[1] + dir[1]
            move(position, dir, puzzle, '@')
        # display(puzzle)
    return calculate_gps_coordinates(puzzle)


def calculate_gps_coordinates(puzzle):
    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == "O":
                total += 100 * i + j
    return total


def display(puzzle):
    for line in puzzle:
        print(line)

    print("---")


def solve_part2(data):
    return data


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    # start_time = time.time()
    # print("Part 2: " + str(solve_part2(data)))
    # print("-> Part2 solved in: ", (time.time() - start_time))
