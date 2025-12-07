#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [list(line) for line in input_file.read().splitlines()]


def solve_part1(maze):
    total_count = 0
    for i in range(1, len(maze)):
        total_count += run_line(maze, i)
        # print_maze(maze)
    return total_count


def run_line(maze, i):
    count = 0
    for j in range(len(maze[0])):
        if maze[i - 1][j] in ['S', '|']:
            if maze[i][j] == "^":
                count += 1
                if j > 0 and maze[i][j - 1] != "^":
                    maze[i][j - 1] = "|"
                if j < len(maze[0]) - 1 and maze[i][j + 1] != "^":
                    maze[i][j + 1] = "|"
            else:
                maze[i][j] = "|"
    return count

def print_maze(maze):
    for line in maze:
        print(line)
    print("\n")

def solve_part2(data):
    return None


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
