#!/usr/bin/env python3
cave = []
ground = 0
for i in range(300):
    line = []
    for j in range(640):
        line.append(".")
    cave.append(line)


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
    cave[i][j] = "+"
    landed = cave[i + 1][j] == "#"
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
    global ground
    draw_rocks(data)
    k = 0
    while sand_fall(ground):
        display()
        k += 1
    return k


def solve_part2(data):
    return data


def parse(data):
    global ground
    res = []
    for elts in data:
        tmp1 = []
        for elt in elts:
            tmp2 = elt.split(",")
            if int(tmp2[1]) > ground:
                ground = int(tmp2[1])
            tmp1.append((int(tmp2[0]), int(tmp2[1])))
        res.append(tmp1)
    return res


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    data = parse(data)
    print("Part 1: " + str(solve_part1(data)))

    # Part 2
    data = read_file("inputs/part2.example")
    # data = read_file("inputs/part2.input")
    # print("Part 2: " + str(solve_part2(data)))
