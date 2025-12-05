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
    return len([ingredient for ingredient in ingredients if is_fresh(ingredient, ranges)])


def is_fresh(ingredient, ranges):
    for r in ranges:
        if r[0] <= ingredient <= r[1]:
            return True
    return False


def solve_part2(ranges):
    new_ranges = ranges.copy()
    ranges = sorted(ranges, key=lambda x: x[0])
    optimized = True
    while optimized:
        optimized = False
        for i in range(len(ranges)):
            r1 = ranges[i]
            for j in range(i + 1, len(ranges)):
                r2 = ranges[j]
                opti, nr = find_intersection2(r1[0], r1[1], r2[0], r2[1])
                if opti:
                    if r1 in new_ranges:
                        new_ranges.remove(r1)
                    if r2 in new_ranges:
                        new_ranges.remove(r2)
                    new_ranges.append(nr)
                    optimized = True
        ranges = new_ranges.copy()

    res = 0
    for r in ranges:
        res += r[1] - r[0] + 1
    return res

def find_intersection2(mini1, maxi1, mini2, maxi2):
    if mini2 <= maxi1 <= maxi2:
        return True, (mini1, maxi2)
    else:
        return False, (None, None)


def find_intersection(mini1, maxi1, mini2, maxi2):
    if mini2 <= mini1 < maxi2:
        if maxi1 >= maxi2:
            return True, (mini2, maxi1)
        else:
            return True, (mini2, maxi2)
    elif mini1 <= mini2:
        if maxi1 >= maxi2:
            return True, (mini1, maxi1)
        elif mini2 <= maxi1 <= maxi2:
            return True, (mini1, maxi2)

    return False, (None, None)


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
    print("Part 2: " + str(solve_part2(ranges)))
    print("-> Part2 solved in: ", (time.time() - start_time))
