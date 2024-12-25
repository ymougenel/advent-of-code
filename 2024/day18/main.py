#!/usr/bin/env python3
import time
import bisect


def read_file(file_name):
    with open(file_name) as input_file:
        return [(int(e2), int(e1)) for e1, e2 in [line.split(",") for line in input_file.read().splitlines()]]


def solve_part1(bytes, limit, maxi, maxj):
    # maxi = max([elt[0] for elt in bytes])
    # maxj = max([elt[1] for elt in bytes])
    grid = [["."] * (maxj + 1) for i in range(maxi + 1)]
    for i, j in bytes[0:limit]:
        grid[i][j] = '#'
    # for line in grid:
    #     print(line)
    solve_maze(grid, maxi, maxj)
    return explored[(maxi, maxj)]


explored = {}


def explore(i, j, points):
    if (i, j) not in explored or explored[(i, j)] > points:
        explored[(i, j)] = points


def solve_maze(grid, maxi, maxj):
    i, j = (0, 0)
    to_explore = [(i, j, 0)]
    while to_explore and (i, j) != (maxi, maxj):
        i, j, points = to_explore.pop()
        # if current path is the shortest
        if (i,j) not in explored or points < explored[(i, j)]:
            explore(i, j, points)
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if abs(m) + abs(n) == 1 and is_in_range(i + m, j + n, maxi, maxj) and grid[i + m][j + n] != "#":
                        bisect.insort(to_explore, (i + m, j + n, points + 1), key=lambda x: -1 * x[2])
    # print(explored)
    if (i,j) == (maxi, maxj):
        explore(i,j,points)

def is_in_range(i, j, maxi, maxj):
    return 0 <= i <= maxi and 0 <= j <= maxj


def solve_part2(data):
    return data


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    # print("Part 1: " + str(solve_part1(data, 12, 6, 6)))
    print("Part 1: " + str(solve_part1(data, 1024, 70, 70)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
