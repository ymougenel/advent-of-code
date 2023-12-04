#!/usr/bin/env python3
import time

paths = {}


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                return (i, j)


def solve_maze(starting_pos, maze):
    global paths
    i_start, j_start = starting_pos
    i, j = i_start, j_start
    paths[(i, j)] = (None, 0)
    nexts = []
    while maze[i][j] != "E":
        tmp = find_nexts(maze, i, j)
        nexts += tmp
        nexts = sorted(nexts, key=lambda x: ord(maze[x[0]][x[1]]),
                       reverse=True)
        if not nexts:
            return None, None

        i, j = nexts.pop(0)

    return (i, j)


def solve_part1(maze):
    starting_pos = find_start(maze)
    exit = solve_maze(starting_pos, maze)

    return len(find_path(exit[0], exit[1], starting_pos))


def find_path(i, j, starting_pos):
    solution = []
    while (i, j) != starting_pos:
        solution.append((i, j))
        i, j = paths[(i, j)][0]
    solution.reverse()
    return solution


def find_nexts(maze, cur_i, cur_j):
    global paths
    nextt = []
    cur_case = maze[cur_i][cur_j]
    cur_distance = paths[(cur_i, cur_j)][1]
    for i in range(cur_i - 1, cur_i + 2):
        for j in range(cur_j - 1, cur_j + 2):
            if abs(i - cur_i) + abs(j - cur_j) == 1 \
                    and is_in_range(maze, i, j) \
                    and is_superior(cur_case, maze[i][j]):
                if (i, j) not in paths:
                    paths[(i, j)] = ((cur_i, cur_j), cur_distance + 1)
                    nextt.append((i, j))
                elif paths[(i, j)][1] > cur_distance + 1:
                    paths[(i, j)] = ((cur_i, cur_j), cur_distance + 1)
                    nextt.append((i, j))
    return nextt


def is_in_range(maze, i, j):
    return 0 <= i < len(maze) and 0 <= j < len(maze[0])


def is_superior(from_case, to_case):
    if from_case == "S":
        from_case = "a"
    if to_case == "E":
        to_case = "z"

    return ord(to_case) <= ord(from_case) + 1


def solve_part2(maze):
    steps = None
    visited = {}
    global paths
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "a":
                paths = {}
                exit = solve_maze((i, j), maze)
                if exit != (None, None):
                    tmp_steps = len(find_path(exit[0], exit[1], (i, j)))
                    if steps is None or tmp_steps < steps:
                        steps = tmp_steps
    return steps


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/part2.example")
    data = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(data)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    print("Part 2: " + str(solve_part2(data)))
