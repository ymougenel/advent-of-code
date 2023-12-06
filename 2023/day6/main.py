#!/usr/bin/env python3
import time
import math


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def parse_races(data):
    times = list(map(int, data[0].split(":")[1].split()))
    distances = list(map(int, data[1].split(":")[1].split()))
    return [(times[i], distances[i]) for i in range(len(times))]


def solve_race(time, distance_record):
    option_count = 0
    for press_count in range(1, time):
        distance = (time - press_count) * press_count
        if distance > distance_record:
            option_count += 1
    return option_count


def solve_part1(races):
    return math.prod([solve_race(t, d) for t, d in races])


def solve_part2(races):
    time = ""
    distance = ""
    for t, d in races:
        time += str(t)
        distance += str(d)

    return solve_race(int(time), int(distance))


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    races = parse_races(data)
    print("Part 1: " + str(solve_part1(races)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    print("Part 2: " + str(solve_part2(races)))
