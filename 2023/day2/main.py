#!/usr/bin/env python3
import time

def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def parse_games(lines):
    games = {}
    for line in lines:
        content = line.split(':')
        id = int(content[0].split(" ")[1])
        sets = content[1].split(";")
        for set in sets:
            cubes = set.split(",")
            red = 0
            green = 0
            blue = 0
            for cube in cubes:
                value = int(cube.strip().split(" ")[0])
                color = cube.strip().split(" ")[1]
                if color == "green":
                    green += value
                elif color == "red":
                    red += value
                elif color == "blue":
                    blue += value
                else:
                    print("Color undefined: " + str(cube))
                    return -1
            if id in games:
                games[id].append((red, green, blue))
            else:
                games[id] = [(red, green, blue)]
    return games

def solve_part1(games):
    max = (12, 13, 14)
    res = 0
    for key, val in games.items():
        possible = True
        for set in val:
            possible = possible and set[0] <= max[0] and set[1] <= max[1] and set[2] <= max[2]
        if possible:
            res += key
    return res

def solve_part2(games):
    res = 0
    for key, val in games.items():
        max_red = 0
        max_green = 0
        max_blue = 0
        for set in val:
            max_red = max(max_red, set[0])
            max_green = max(max_green, set[1])
            max_blue = max(max_blue, set[2])
        res += max_red * max_green * max_blue
    return res


if __name__ == '__main__':
    start_time = time.time()

    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    games = parse_games(data)

    print("Part 1: " + str(solve_part1(games)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    # data = read_file("inputs/input.txt")
    print("Part 2: " + str(solve_part2(games)))
