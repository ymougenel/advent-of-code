#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        return [line.split(",") for line in input_file.read().splitlines()]


def solve_part1(data):
    count = 0
    for (left, right) in data:
        if (left[0] >= right[0] and left[1] <= right[1]) or (left[0] <= right[0] and left[1] >= right[1]):
            count += 1
    return count


def solve_part2(data):
    count = 0
    for (left, right) in data:
        if not (left[0] < right[0] and left[1] < right[0]) and not (left[0] > right[1] and left[1] > right[1]):
            count += 1
    return count


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    res = []
    for left, right in data:
        part1 = int(left.split("-")[0])
        part2 = int(left.split("-")[1])
        part3 = int(right.split("-")[0])
        part4 = int(right.split("-")[1])
        res.append([(part1, part2), (part3, part4)])
    print("Part 1: " + str(solve_part1(res)))

    # Part 2
    data = read_file("inputs/part2.example")
    # data = read_file("inputs/part2.input")
    print("Part 2: " + str(solve_part2(res)))
