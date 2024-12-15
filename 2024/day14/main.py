#!/usr/bin/env python3
import time
import re

HEIGHT = None
WIDTH = None


def read_file(file_name):
    inputs = []
    with open(file_name) as input_file:
        lines = [line for line in input_file]
        for line in lines:
            digits = re.findall(r'(-?\d+)', line)
            digits = [int(i) for i in digits]
            inputs.append(digits)
    return inputs


def solve_robot(robot, iteration):
    position = robot[0], robot[1]
    velocity = robot[2], robot[3]
    k = 0
    while k < iteration:
        x = (position[0] + velocity[0]) % WIDTH
        y = (position[1] + velocity[1]) % HEIGHT
        position = (x, y)
        k += 1
    return position


def display(positions):
    map = [[0] * WIDTH for k in range(HEIGHT)]
    for x, y in positions:
        map[y][x] += 1

    for i in range(HEIGHT):
        print(map[i])


def solve_part1(robots):
    final_positions = []
    for robot in robots:
        final_positions.append(solve_robot(robot, 100))
    print(final_positions)
    display(final_positions)
    return count_quadrants(final_positions)


def count_quadrants(positions):
    top_left = len([pos for pos in positions if pos[0] < WIDTH // 2 and pos[1] < HEIGHT // 2])
    bottom_left = len([pos for pos in positions if pos[0] < WIDTH // 2 and pos[1] > HEIGHT / 2])
    top_right = len([pos for pos in positions if pos[0] > WIDTH / 2 and pos[1] < HEIGHT // 2])
    bottom_right = len([pos for pos in positions if pos[0] > WIDTH / 2 and pos[1] > HEIGHT / 2])
    return top_left * bottom_left * top_right * bottom_right


def solve_part2(data):
    return data


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    WIDTH, HEIGHT = 11, 7
    data = read_file("inputs/input.txt")
    WIDTH, HEIGHT = 101, 103

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
