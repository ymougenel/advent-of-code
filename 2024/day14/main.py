#!/usr/bin/env python3
import time
import re
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np
import glob
import contextlib
from PIL import Image

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
    return count_quadrants(final_positions)


def count_quadrants(positions):
    top_left = len([pos for pos in positions if pos[0] < WIDTH // 2 and pos[1] < HEIGHT // 2])
    bottom_left = len([pos for pos in positions if pos[0] < WIDTH // 2 and pos[1] > HEIGHT / 2])
    top_right = len([pos for pos in positions if pos[0] > WIDTH / 2 and pos[1] < HEIGHT // 2])
    bottom_right = len([pos for pos in positions if pos[0] > WIDTH / 2 and pos[1] > HEIGHT / 2])
    return top_left * bottom_left * top_right * bottom_right


def solve_part2(robots):
    k = 0
    while k < 10000:
        for robot in robots:
            next_positions = solve_robot(robot, 1)
            robot[0], robot[1] = next_positions
        print(k)
        display_xmas([[r[0], r[1]] for r in robots], k)
        k += 1
    # filepaths
    fp_in = "./outputs/*.png"
    fp_out = "./outputs/computed.gif"

    # Generated GIF
    with contextlib.ExitStack() as stack:

        # lazily load images
        imgs = (stack.enter_context(Image.open(f))
                for f in sorted(glob.glob(fp_in)))

        # extract  first image from iterator
        img = next(imgs)

        img.save(fp=fp_out, format='GIF', append_images=imgs,
                 save_all=True, duration=200, loop=0)


def display_xmas(positions, iteration):
    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    for pos in positions:
        img[pos[1]][pos[0]] = [255, 0, 0]
    plt.imsave('outputs/Xmax_' + str(iteration) + '.png', img)

    # plt.title('Iteration:' + str(iteration), fontweight="bold")
    # plt.pause(0.01)
    # plt.imshow(img)


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
