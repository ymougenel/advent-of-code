#!/usr/bin/env python3


def read_file(file_name):
    with open(file_name) as input_file:
        return [int(line) for line in input_file.read().splitlines()]

def read_file_sliding_window(file_name):
    with open(file_name) as input_file:
        return [int(line.split(" ")[0]) for line in input_file.read().splitlines()]

def find_depth_increases(sonar_data):
    current = sonar_data[0]
    increase_count = 0
    for i in range(1, len(sonar_data)):
        if sonar_data[i] > current:
            increase_count += 1
        current = sonar_data[i]
    return increase_count

def regroup_values(sonar_data):
    sumed_values = [0]*len(sonar_data)
    for i in range(len(sonar_data)):
        sumed_values[i] += sonar_data[i]
        if i - 1 >= 0:
            sumed_values[i-1] += sonar_data[i]
        if i - 2 >= 0:
            sumed_values[i-2] += sonar_data[i]
    return sumed_values

if __name__ == '__main__':
    # data = read_file("inputs/part1.example")
    # data = read_file("inputs/part1.input")
    # print(find_depth_increases(data))

    # data = read_file_sliding_window("inputs/part2.example")
    data = read_file_sliding_window("inputs/part2.input")
    print(find_depth_increases(regroup_values(data)))
