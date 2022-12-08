#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]

def count_visible_trees(trees):
    total = 0
    for i in range(len(trees)):
        j = 0
        hidden = False
        while j < len(trees[0]) and not hidden:
            if j == 0 or trees[i][j] > trees[i][j+1]:
                total += 1
            j += 1
    return total

def solve_part1(data):
    return data

def solve_part2(data):
    return data

if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    trees = []
    for line in data:
        row = []
        for car in line:
            row.append(int(car))
        trees.append(row)

    #data = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(trees)))

    # Part 2
    data = read_file("inputs/part2.example")
    #data = read_file("inputs/part2.input")
    print("Part 2: " + str(solve_part2(data)))
