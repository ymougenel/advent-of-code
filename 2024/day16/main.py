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


def update_exporation(i, j, value, path_len):
    global explored
    if (i, j) in explored:
        if value < explored[(i, j)][0]:
            explored[(i, j)] = (value, path_len)
    else:
        explored[(i, j)] = (value, path_len)


to_explore = []


def explore(puzzle, i, j, prev_m, prev_n, points, path_len):
    global to_explore
    # Check if end is reached
    if puzzle[i][j] == "E":
        update_exporation(i, j, points, path_len)
    else:
        # If already went there with shortest path
        if (i, j) in explored and explored[(i, j)][0] < points:
            return
        else:
            update_exporation(i, j, points, path_len)
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if abs(m) + abs(n) == 1 and is_in_range(puzzle, i + m, j + n) and puzzle[i + m][j + n] != "#":
                        if (prev_m, prev_n) == (m, n):
                            to_explore.append((i + m, j + n, m, n, points + 1, path_len + 1))
                        else:
                            to_explore.append((i + m, j + n, m, n, points + 1000 + 1, path_len + 1))


def is_in_range(puzzle, i, j):
    return 0 <= i < len(puzzle) and 0 <= j < len(puzzle[0])


def display(puzzle):
    new_puz = copy.deepcopy(puzzle)
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if (i, j) in explored:
                new_puz[i][j] = explored[(i, j)]
                p1 = str(new_puz[i][j][0])
                p2 = str(new_puz[i][j][1])
                new_puz[i][j] = p1 + " " * (7 - len(p1)) + p2 + " " * (3 - len(p2))
            else:
                new_puz[i][j] = new_puz[i][j] + " " * 9
    for i in range(len(puzzle)):
        print(new_puz[i])


def solve_part1(puzzle):
    i, j = find_element(puzzle, "S")
    to_explore.append((i, j, 0, 1, 0,0))
    while to_explore:
        elt = to_explore.pop()
        explore(puzzle, *elt)
    print(explored[find_element(puzzle, "E")])
    display(puzzle)
    return explored[find_element(puzzle, "E")]


def solve_part2(data):
    return data


def count_best_seats(puzzle):
    i, j = find_element(puzzle, 'E')

    to_be_counted = [(i, j, explored[(i, j)])]
    count = []
    while to_be_counted:
        elt = to_be_counted.pop()
        to_be_counted += get_counting_neighbour(puzzle, *elt)
        count.append(elt)
    return len(set(count))


def get_counting_neighbour(puzzle, i, j, current_points):
    possibilities = []
    for m in range(-1, 2):
        for n in range(-1, 2):
            if (abs(m) + abs(n) == 1 and is_in_range(puzzle, i + m, j + n) and puzzle[i + m][j + n] != "#"
                    and explored[(i + m, j + n)][1] == current_points[1] -1 ):
                possibilities.append((i + m, j + n, explored[(i + m, j + n)]))
                # possibilities = sorted(possibilities, key=lambda x: x[2])
                # possibilities = [elt for elt in possibilities if elt[2] == possibilities[0][2]]
    return possibilities


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/example2.txt")
    # data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    sol = solve_part1(data)
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    sol = solve_part2(data)
    print(count_best_seats(data))
    print("-> Part2 solved in: ", (time.time() - start_time))
