#!/usr/bin/env python3
import math
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def data_to_map(data):
    map = []
    for line in data:
        row = []
        for char in line:
            if char == ".":
                row.append((False, False, False, False))
            elif char == "|":
                row.append((False, True, False, True))
            elif char == "-":
                row.append((True, False, True, False))
            elif char == "L":
                row.append((True, True, False, False))
            elif char == "J":
                row.append((False, True, True, False))
            elif char == "7":
                row.append((False, False, True, True))
            elif char == "F":
                row.append((True, False, False, True))
            elif char == "S":
                row.append((True, True, True, True))
        map.append(row)
    return map


def dijktra(map, starting_pos):
    remaining = [starting_pos]
    distances = {}
    distances[starting_pos] = 0

    while remaining:
        shortest_sol, shortest_dist = find_shortest(remaining, distances)
        remaining.remove(shortest_sol)
        valid_neighbours = find_neigbouh(map, shortest_sol)
        # update distances
        for neighbour in valid_neighbours:
            if neighbour in distances:
                if distances[neighbour] > shortest_dist + 1:
                    distances[neighbour] = shortest_dist + 1
            else:
                distances[neighbour] = shortest_dist + 1
                remaining.append(neighbour)
    return distances


def solve_part1(distances):
    longest_dist = 0
    for val in distances.values():
        if val >= longest_dist:
            longest_dist = val

    return longest_dist


def find_neigbouh(map, shortest_sol):
    solutions = []
    directions = "LRUD"
    for dir in directions:
        res = can_go(map, shortest_sol, dir)
        if res: solutions.append(res)
    return solutions


def can_go(map, current, direction):
    i, j = current
    k = vi = vj = 0
    if direction == "L":
        k = 2
        vi, vj = (0, -1)
    elif direction == "R":
        k = 0
        vi, vj = (0, 1)
    elif direction == "U":
        k = 1
        vi, vj = (-1, 0)
    elif direction == "D":
        k = 3
        vi, vj = (1, 0)
    else:
        print("Direction not found")

    if 0 <= i + vi < len(data) and 0 <= j + vj < len(data[0]) and map[i][j][k] and map[i + vi][j + vj][(k + 2) % 4]:
        return i + vi, j + vj
    else:
        return None


def find_shortest(remaining, distances):
    shortest_sol = None
    shortest_dist = math.inf
    for node in remaining:
        dist = distances[node]
        if dist < shortest_dist:
            shortest_sol = node
            shortest_dist = dist
    return shortest_sol, shortest_dist


def solve_part2(map, distances):
    valid_inside = []
    raw_count = {}
    col_count = {}

    for i, j in distances.keys():
        if i in raw_count:
            raw_count[i].append(j)
        else:
            raw_count[i] = [j]

        if j in col_count:
            col_count[j].append(i)
        else:
            col_count[j] = [i]

    for i in range(len(data)):
        for j in range(len(data[0])):
            valid = map[i][j] == (False, False, False, False)

    return len(valid_inside)


def count_colision_walls(position, directions, distances, map):
    count = 0
    return count


def find_starting_pos(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "S":
                return i, j


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example4.txt")
    data = read_file("inputs/input.txt")
    map = data_to_map(data)
    starting_pos = find_starting_pos(data)

    # Part 1
    start_time = time.time()
    distances = dijktra(map, starting_pos)
    print("Part 1: " + str(solve_part1(distances)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    # data = read_file("inputs/example2.txt")
    print("Part 2: " + str(solve_part2(data, distances)))
    print("-> Part2 solved in: ", (time.time() - start_time))
