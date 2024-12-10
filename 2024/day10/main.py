#!/usr/bin/env python3
import time
import copy

def read_file(file_name):
    with open(file_name) as input_file:
        return [[int(i) for i in line] for line in input_file.read().splitlines()]


def explore_value(map, i, j, value, path, solutions):
    size = len(map)
    for m in range(-1, 2):
        for n in range(-1, 2):
            if abs(m) + abs(n) == 1 and 0 <= i + m < size and 0 <= j + n < size and map[i + m][j + n] == value:
                if value == 9:
                    solutions.append(path + [(i+m,j+n)])
                else:
                    explore_value(map, i + m, j + n, value + 1, copy.copy(path)+[(i+m,j+n)], solutions)


def solve_part1(map):
    starting_positions = []
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 0:
                starting_positions.append((i, j))
    final_solutions = []
    for start_pos in starting_positions:
        explore_value(map, start_pos[0], start_pos[1], 1, [start_pos],final_solutions)
    return get_score(final_solutions)

def get_score(solutions_path):
    counts = {}
    short_path = []
    for path in solutions_path:
        if (path[0], path[-1]) not in short_path:
            short_path.append((path[0], path[-1]))
    for path in short_path:
        starter = path[0]
        if starter in counts:
            counts[starter] += 1
        else:
            counts[starter] = 1
    return sum(counts.values())
def solve_part2(data):
    return len(data)


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example2.txt")
    data = read_file("inputs/example5.txt")
    # data = read_file("inputs/example4.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
