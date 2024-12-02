#!/usr/bin/env python3
import time
def read_file(file_name):
    with open(file_name) as input_file:
        line = [[l for l in line.split("   ")] for line in input_file]
        return [int(e[0]) for e in line], [int(e[1]) for e in line]

def solve_part1(l1, l2):
    return sum([abs(l1[i] - l2[i]) for i in range(len(l1))])

def solve_part2(l1, l2):
    return sum([elt* l2.count(elt) for elt in l1])

if __name__ == '__main__':
    # Parse input file
    # l1, l2 = read_file("inputs/example1.txt")
    l1, l2  = read_file("inputs/input.txt")
    l1.sort()
    l2.sort()

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(l1, l2)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(l1, l2)))
    print("-> Part2 solved in: ", (time.time() - start_time))
