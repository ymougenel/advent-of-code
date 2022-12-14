#!/usr/bin/env python3
cave = []
MAX_I = 400
MAX_J = 700
lowest_block = 0
for i in range(MAX_I):
    line = []
    for j in range(MAX_J):
        line.append(".")
    cave.append(line)
cave[0][500] = "+"


def read_file(file_name):
    with open(file_name) as input_file:
        return [line.split(" -> ") for line in input_file.read().splitlines()]


def draw_rocks(data):
    for blocks in data:
        previous = blocks[0]
        for k in range(1, len(blocks)):
            current = blocks[k]
            for i in range(min(previous[0], current[0]), max(previous[0], current[0]) + 1):
                for j in range(min(previous[1], current[1]), max(previous[1], current[1]) + 1):
                    cave[j][i] = "#"
            previous = current


def display():
    for i in range(20):
        print(cave[i][494:505])


def sand_fall(max):
    i = 0
    j = 500
    landed = False
    while not landed and i <= max:
        if cave[i + 1][j] == ".":
            i += 1
        elif cave[i + 1][j - 1] == ".":
            i += 1
            j -= 1
        elif cave[i + 1][j + 1] == ".":
            i += 1
            j += 1
        else:
            landed = True
            cave[i][j] = "o"
    return i <= max


def solve_part1(data):
    global lowest_block
    draw_rocks(data)
    k = 0
    while sand_fall(lowest_block):
        display()
        k += 1
    return k


def solve_part2(data):
    draw_rocks(data)
    for j in range(MAX_J):
        cave[lowest_block + 2][j] = "#"

    k = 0
    while cave[0][500] == "+":
        sand_fall(lowest_block + 2)
        # display()
        k += 1
    return k


def parse(data):
    global lowest_block
    res = []
    for elts in data:
        tmp1 = []
        for elt in elts:
            tmp2 = elt.split(",")
            if int(tmp2[1]) > lowest_block:
                lowest_block = int(tmp2[1])
            tmp1.append((int(tmp2[0]), int(tmp2[1])))
        res.append(tmp1)
    return res


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    data = parse(data)
    # print("Part 1: " + str(solve_part1(data)))

    # Part 2

    print("Part 2: " + str(solve_part2(data)))
