#!/usr/bin/env python3
import time
import bisect


def read_file(file_name):
    with open(file_name) as input_file:
        return [(int(e2), int(e1)) for e1, e2 in [line.split(",") for line in input_file.read().splitlines()]]


def solve_part1(bytes, limit, maxi, maxj):
    grid = [["."] * (maxj + 1) for i in range(maxi + 1)]
    # Place corrupted bytes on grid
    for i, j in bytes[0:limit]:
        grid[i][j] = '#'

    solve_maze(grid, maxi, maxj)
    return distance_explored[(maxi, maxj)]


distance_explored = {}

# Method to quickly update python dictionary
def set_or_update_distance_exploration(i, j, points):
    if (i, j) not in distance_explored or distance_explored[(i, j)] > points:
        distance_explored[(i, j)] = points

# Try to solve the input grid, return True if end reached, False otherwise
def solve_maze(grid, maxi, maxj):
    i, j = (0, 0)
    to_explore = [(i, j, 0)]
    while to_explore and (i, j) != (maxi, maxj):
        i, j, points = to_explore.pop()
        # if current path is the shortest
        if (i, j) not in distance_explored or points < distance_explored[(i, j)]:
            set_or_update_distance_exploration(i, j, points)
            for m in range(-1, 2):
                for n in range(-1, 2):
                    # For all vertical/horizontal neighbours that are not corrupted (#)
                    if abs(m) + abs(n) == 1 and is_in_range(i + m, j + n, maxi, maxj) and grid[i + m][j + n] != "#":
                        # Insert new neighbour for exploration (bisect for ordering based on the points)
                        bisect.insort(to_explore, (i + m, j + n, points + 1), key=lambda x: -1 * x[2])

    # A path as been found (the end is reached)
    if (i, j) == (maxi, maxj):
        set_or_update_distance_exploration(i, j, points)
        return True
    # Return False if no path available
    return False


def is_in_range(i, j, maxi, maxj):
    return 0 <= i <= maxi and 0 <= j <= maxj


def solve_part2(bytes, limit, maxi, maxj):
    global distance_explored
    grid = [["."] * (maxj + 1) for i in range(maxi + 1)]
    for i, j in bytes[0:limit]:
        grid[i][j] = '#'
    k = limit
    # Try bytes while a path is found
    while k < len(bytes):
        distance_explored = {}
        path_exist = solve_maze(grid, maxi, maxj)
        # If no path available (ie: all roads are blocked) -> Return last bytes
        if not path_exist:
            return bytes[k - 1]
        path = compute_path(maxi, maxj)
        i, j = bytes[k]
        skipped = False
        # Quick process for all bytes not on the shortest road (no solving required)
        while (i, j) not in path:
            skipped = True
            i, j = bytes[k]
            grid[i][j] = "#"
            k += 1
        if not skipped:
            k += 1
    return None


# Compute the full path based on the computed exploration
def compute_path(maxi, maxj):
    i, j = maxi, maxj

    path = []
    # Stop when grip start is reached
    while (i, j) != (0, 0):
        path.append((i, j))
        points = distance_explored[(i, j)]

        for m in range(-1, 2):
            for n in range(-1, 2):
                # Find in vertical/horizontal neighbour which square belongs to the shortest path
                if abs(m) + abs(n) == 1 and is_in_range(i + m, j + n, maxi, maxj) and (
                i + m, j + n) in distance_explored and \
                        distance_explored[(i + m, j + n)] == points - 1:
                    next_i = i + m
                    next_j = j + n
        i, j = next_i, next_j
    return path


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
    # print("Part 2: " + str(solve_part2(data, 12, 6, 6)))
    print("Part 2: " + str(solve_part2(data, 1024, 70, 70)))
    print("-> Part2 solved in: ", (time.time() - start_time))
