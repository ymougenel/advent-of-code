#!/usr/bin/env python3
import time

def read_file(file_name):
    res=[]
    with open(file_name) as input_file:
        c= [line for line in input_file.read().splitlines()]
    for a in c:
        res.append([int(b) for b in a])
    return res

def solve_part1(batteries):
    return sum([get_largest_joltage(bat_line) for bat_line in batteries])

def get_largest_joltage(bat_line):
    maxi = max(bat_line[:-1]) # Avoid last element for incoming concatenation
    index_maxi = bat_line.index(maxi)
    second_largest = max(bat_line[index_maxi+1:])
    return 10*maxi + second_largest

def solve_part2(data):
    return data

if __name__ == '__main__':

    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))

