#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [int(i) for i in input_file.read().splitlines()[0].split(" ")]


def rock_blinkink(rock):
    if rock == 0:
        return [1]
    elif len(str(rock)) % 2 == 0:
        rock_str = str(rock)
        middle = len(rock_str) // 2
        return [int(rock_str[:middle]), int(rock_str[middle:])]
    else:
        return [rock * 2024]


def solve_part1(rocks):
    k = 0
    while k < 25:
        new_rock = []
        for i in range(len(rocks)):
            new_rock += rock_blinkink(rocks[i])
        rocks = new_rock
        k += 1
    return len(rocks)


def get_state(rocks):
    current_state = {}
    for rock in rocks:
        if rock in current_state:
            current_state[rock] += 1
        else:
            current_state[rock] = 1
    return current_state


def solve_part2(rocks):
    k = 0
    current_state = get_state(rocks)
    while k < 75:
        next_state = {}
        for rock, count in current_state.items():
            rock_simu = rock_blinkink(rock)
            for res_rock in rock_simu:
                if res_rock in next_state:
                    next_state[res_rock] += count
                else:
                    next_state[res_rock] = count
        current_state = next_state
        k += 1
    return sum(current_state.values())


if __name__ == '__main__':
    # Parse input file
    # data = read_file("inputs/example1.txt")
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
