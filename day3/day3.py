#!/usr/bin/env python3
import numpy as np

def read_wires(input_file):
    inputFile = open(input_file, "r")
    # inputFile = open("inputs/example3.txt", "r")
    data = inputFile.read().splitlines()
    inputFile.close()
    wires = list(map(lambda s: s.split(','), data))
    return wires


# Init matrix
def init_matrix(row, col, value=-1):
    M = []
    for i in range(row):
        M.append([value] * col)
    return M


# Print matrix
def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()


# Grid distance: https://en.wikipedia.org/wiki/Taxicab_geometry
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_direction_vector(dir_letter):
    if dir_letter == "U":
        return (-1, 0)
    elif dir_letter == "D":
        return (1, 0)
    elif dir_letter == "L":
        return (0, -1)
    elif dir_letter == "R":
        return (0, 1)
    else:
        print("Unknown direction input: " + dir_letter)
        raise ValueError


def displayPath(wire, origin, size):
    board =  np.zeros((size, size), dtype=complex)
    position = origin
    for segment in wire:
        direction = get_direction_vector(segment[0])
        distance = int(segment[1:])
        for i in range(distance):
            position = (position[0] + direction[0], position[1] + direction[1])
            board[position[0]][position[1]] = 1

    return board

def find_closest_intersection_distance(origin, panel):
    min_distance = len(panel) ** 2
    closest_intersection = ()
    for i in range(len(panel)):
        for j in range(len(panel[0])):
            if panel[i][j] > 1:
                distance = manhattan_distance(origin, (i, j))
                if distance <= min_distance:
                    min_distance = distance
                    closest_intersection = (i, j)
    return min_distance


def displayPaths(panel, origin, wires, size):
    for wire in wires:
        panel += displayPath(wire, origin, size)




if __name__ == '__main__':
    wires = read_wires("wires_example1.txt")
    # wires = read_wires("wires.txt")
    # TODO: Calculate required size for wires
    SIZE = 190
    panel = np.zeros((SIZE, SIZE), dtype=complex)
    central_port = (SIZE // 2, SIZE // 2)
    displayPaths(panel, central_port, wires, SIZE)

    print(find_closest_intersection_distance(central_port, panel))

