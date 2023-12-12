#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def is_possibility(springs, counts):
    blocks = 0
    for elt in springs:
        if elt == "#":
            blocks += 1
        elif elt == ".":
            if blocks != 0:
                if len(counts) == 0 or blocks != counts[0]:
                    return False
                else:
                    blocks = 0
                    counts = counts[1:]
        else:
            print("Error, found unwanted symbol")
            return -1
    return (len(counts) == 0 and blocks == 0) or (len(counts) == 1 and blocks == counts[0])


def find_possibilities(springs):
    possibilities = [""]
    for i in range(len(springs)):
        tmp_poss = []
        for poss in possibilities:
            if springs[i] == "?":
                tmp_poss.append(poss + "#")
                tmp_poss.append(poss + ".")
            else:
                tmp_poss.append(poss + springs[i])
        possibilities = tmp_poss
    return possibilities


def parse_springs(line):
    springs = line.split(" ")[0]
    counts = list(map(int, line.split(" ")[1].split(",")))
    return springs, counts


def solve_part1(data):
    total = 0
    for springs, counts in data:
        possibilities = find_possibilities(springs)
        possibles = [poss for poss in possibilities if is_possibility(poss, counts)]
        total += len(possibles)
    return total


def solve_part2(data):
    return data


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    data = [parse_springs(line) for line in data]

    print("Part 1: " + str(solve_part1(data)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    data = read_file("inputs/example2.txt")
    # data = read_file("inputs/input.txt")
    print("Part 2: " + str(solve_part2(data)))
