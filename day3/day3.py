#!/usr/bin/env python3
import numpy as np


def read_wires(input_file):
    inputFile = open(input_file, "r")
    # inputFile = open("inputs/example3.txt", "r")
    data = inputFile.read().splitlines()
    inputFile.close()
    wires = list(map(lambda s: s.split(','), data))
    return wires


# Grid distance: https://en.wikipedia.org/wiki/Taxicab_geometry
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Return vector (row, col) base from letter
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


# Print the wire path on the board
def displayPath(wire, origin, size_row, size_col):
    board = np.zeros((size_row, size_col), dtype=int)
    position = origin
    steps = 0
    for segment in wire:
        direction = get_direction_vector(segment[0])
        distance = int(segment[1:])
        for i in range(distance):
            steps += 1
            position = (position[0] + direction[0], position[1] + direction[1])
            if board[position[0]][position[1]] == 0:
                board[position[0]][position[1]] = steps

    return board


# Find the closest intersection
def find_closest_intersection_distance(origin, panel):
    min_distance = len(panel) ** 2
    for i in range(len(panel)):
        for j in range(len(panel[0])):
            if panel[i][j].real > 1 and panel[i][j].imag > 1j:
                distance = manhattan_distance(origin, (i, j))
                if distance <= min_distance:
                    min_distance = distance
    return min_distance


def fewest_combined_steps(panel):
    combined_steps = len(panel) ** 4
    for i in range(len(panel)):
        for j in range(len(panel[0])):
            if panel[i][j].real > 1 and panel[i][j].imag > 1j:
                steps = panel[i][j].real + panel[i][j].imag
                combined_steps = min(combined_steps, steps)
    return combined_steps


def displayPaths(panel, origin, wires, size_row, size_col):
    panel += displayPath(wires[0], origin, size_row, size_col)  # First draw when real number
    panel += (displayPath(wires[1], origin, size_row, size_col) * 1j)  # Second draw with imaginary

# Sicne we are dealing with huge matrix, calculate the minimum size required
def get_required_size(wires):
    u = d = l = r = 0
    for wire in wires:
        x = y = 0
        for segment in wire:
            direction = get_direction_vector(segment[0])
            distance = int(segment[1:])
            x = x + distance * direction[0]
            y = y + distance * direction[1]
            u = min(x, u)
            d = max(x, d)
            l = min(y, l)
            r = max(y, r)
    return (abs(u), abs(d), abs(l), abs(r))


if __name__ == '__main__':
    wires = read_wires("wires_example3.txt")
    # wires = read_wires("wires.txt")

    size = get_required_size(wires)  # Max: Up, down, left, right
    SIZE_ROW = size[0] + size[1] + 1
    SIZE_COL = size[2] + size[3] + 1
    panel = np.zeros((SIZE_ROW, SIZE_COL), dtype=complex)
    central_port = (size[0], size[2])

    displayPaths(panel, central_port, wires, SIZE_ROW, SIZE_COL)
    print(find_closest_intersection_distance(central_port, panel))
    print(fewest_combined_steps(panel))
