#!/usr/bin/env python3
import time
import copy


def read_file(file_name):
    with open(file_name) as input_file:
        return [[letter for letter in line] for line in input_file.read().splitlines()]


def detect_starter(puzzle):
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
    return starting_position, direction


def run_simulation(puzzle, starting_position, starting_direction):
    direction = starting_direction
    out = False
    n= len(puzzle)
    # Init puzzle (replace '.' by empty arrays for path tracking
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] != "#":
                puzzle[i][j] = []
    i, j = starting_position
    while not out:
        next_i = i + direction[0]
        next_j = j + direction[1]

        # Detect the out of the puzzle
        if not (0 <= next_i < n) or not (0 <= next_j < n):
            puzzle[i][j].append(direction)
            out = True
        # Next step is a wall -> Turn right
        elif puzzle[next_i][next_j] == "#":
            direction = turn(direction)
        else:
            # Detect forever loop (path used with same direction)
            if direction in puzzle[i][j] :
                return False
            # Move forward
            puzzle[i][j].append(direction)
            i, j = next_i, next_j
    return True

def get_path(puzzle):
    path = []
    n = len(puzzle)
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] not in [".", "#", []]:
                path.append((i, j))
    return path

def solve_part1(puzzle):
    starting_pos, starting_dir = detect_starter(puzzle)
    run_simulation(puzzle, starting_pos, starting_dir)
    return len(get_path(puzzle))


def display(puzzle):
    for line in puzzle:
        tmp = ""
        for elt in line:
            if elt == "#":
                tmp += elt
            elif elt == []:
                tmp += "."
            else:
                tmp += "X"
        print(tmp)
    print()


def turn(direction):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    index = directions.index(direction)
    return directions[(index + 1) % len(directions)]


def solve_part2(puzzle):
    starting_pos, starting_dir = detect_starter(puzzle)
    solved_puzzled = copy.deepcopy(puzzle)
    run_simulation(solved_puzzled, starting_pos, starting_dir)
    path = get_path(solved_puzzled)
    count = 0
    for i, j in path:
        obstruction_puzzle = copy.deepcopy(puzzle)
        obstruction_puzzle[i][j] = "#"
        if (i,j) != starting_pos and not run_simulation(obstruction_puzzle, starting_pos, starting_dir):
            count += 1
    return count


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(copy.deepcopy(data))))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))