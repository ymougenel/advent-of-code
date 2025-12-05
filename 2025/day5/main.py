#!/usr/bin/env python3
import time


def read_file(file_name):
    ranges = []
    ingredients = []
    with open(file_name) as input_file:
        lines = [line for line in input_file.read().splitlines()]
        for line in lines:
            if "-" in line:
                r = line.split("-")
                ranges.append((int(r[0]), int(r[1])))
            elif line:
                ingredients.append(int(line))
    return ranges, ingredients


def solve_part1(ranges, ingredients):
    return len([ingredient for ingredient in ingredients if is_fresh(ingredient,ranges)])


def is_fresh(ingredient, ranges):
    for r in ranges:
        if r[0] <= ingredient <= r[1]:
            return True
    return False


def solve_part2(ranges, ingredients):
    return ranges


if __name__ == '__main__':
    # Parse input file
    ranges, ingredients = read_file("inputs/example1.txt")
    ranges, ingredients = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(ranges, ingredients)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    # print("Part 2: " + str(solve_part2(ranges, ingredients)))
    print("-> Part2 solved in: ", (time.time() - start_time))
