#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]

def find_marker(data, LENGTH):
    count = 0
    for i in range(len(data)):
        if data[i] in data[i+1:i+LENGTH]:
            count = 0
        else:
            count += 1
        if count == LENGTH:
            return i+1
    return 0

def solve_part1(data):
    return find_marker(data, 4)

def solve_part2(data):
    return find_marker(data, 14)

if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")[0]
    data = read_file("inputs/part1.input")[0]
    #data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    #data = "nppdvjthqldpwncqszvftbrmjlhg"
    #data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

    print("Part 1: " + str(solve_part1(data)))

    # Part 2
    print("Part 2: " + str(solve_part2(data)))
