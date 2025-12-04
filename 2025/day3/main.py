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

def solve_part2(batteries):
    res = 0
    for bat_line in batteries:
        s = get_friction_largest_joltage(bat_line)
        res += s
    return res

def get_friction_largest_joltage(bat_line):
    res = ""
    count_remaining_digit = 12
    block = bat_line
    while count_remaining_digit >0:
        max_block = block[:len(block) - count_remaining_digit+1 ]
        remaining_block = block[-(count_remaining_digit-1):]
        maxi = max(max_block)
        res += str(maxi)
        index_maxi = max_block.index(maxi)
        block = max_block[index_maxi+1:] + remaining_block
        count_remaining_digit -= 1

    return int(res)

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

