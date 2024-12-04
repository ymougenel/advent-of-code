#!/usr/bin/env python3
import time

def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]

def discover(searched_word, data, n, i, j, dir, letter_index):
    return (letter_index == len(searched_word)) or (
            0 <= i < n and 0 <= j < n and data[i][j] == searched_word[letter_index] and discover(searched_word, data, n,
                                                                                                 i + dir[0],
                                                                                                 j + dir[1], dir,
                                                                                                 letter_index + 1))

def solve_part1(data):
    count = 0
    n = len(data)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for i in range(n):
        for j in range(n):
            if data[i][j] == "X":
                for direction in directions:
                    if discover("XMAS", data, n, i + direction[0], j + direction[1], direction, 1):
                        count += 1
    return count

def solve_part2(data):
    n = len(data)
    count = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == "A" and 0<i< n-1 and 0<j<n-1:
                diag1 = data[i-1][j-1]+ data[i+1][j+1]
                diag2 = data[i-1][j+1] + data[i+1][j-1]
                if diag1 in ["MS","SM"] and diag2 in ["MS","SM"]:
                    count += 1
    return count

if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
