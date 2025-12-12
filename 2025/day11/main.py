#!/usr/bin/env python3
import time
import re


def read_file(file_name):
    with open(file_name) as input_file:
        lines = [line for line in input_file.read().splitlines()]
        connections = {}
        for line in lines:
            key = line.split(":")[0]
            values = [elt for elt in line.split(":")[1].split(" ") if elt]
            connections[key] = values
        connections["out"] = []
        return connections


def parse_line(line):
    return re.compile(r'\d+').findall(line)


def solve_part1(connections):
    return len(extend_path(["you"], connections, stop="out"))


def extend_path(previous_path, connections, stop):
    last_elt = previous_path[-1]
    all_paths = []
    for co in connections[last_elt]:
        if co == stop:
            all_paths.append(previous_path + [co])
        elif co not in previous_path:
            for discovered_path in extend_path(previous_path + [co], connections, stop):
                if discovered_path:
                    all_paths.append(discovered_path)
    return all_paths


def solve_part2(connections):
    # TODO: path you -> fft , then path fft -> dac, then path dac-> end
    svr_fft = extend_path(["out", "dac", "svr"], connections, "fft")
    print("tic")
    fft_dac = extend_path(["end","you","fft"], connections, "dac")
    print("tac")
    dac_out = extend_path(["you","fft","dac"], connections, "out")
    return len(svr_fft) * len(fft_dac) * len(dac_out)
    # return len([elt for elt in extend_path(["svr"], connections, "out") if
    #             "fft" in elt and "dac" in elt])


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
