#!/usr/bin/env python3
import time
import re

from debian.debtags import output


def read_file(file_name):
    procedures = []
    with open(file_name) as input_file:
        for line in input_file.read().splitlines():
            diag = parse_indicator_light_diagram(line)
            schematic = parse_schematics(line)
            joltage = parse_schematics(line, joltage=True)[0]
            procedures.append((diag, schematic, joltage))
    return procedures


def parse_schematics(line, joltage=False):
    schematics_content = line.split(" ")[1:]
    schematics = []
    for s in schematics_content:
        if (not joltage and "(" in s) or (joltage and "{" in s):
            digits = re.compile(r'\d+').findall(s)
            schematics.append([int(digit) for digit in digits])
    return schematics


def parse_indicator_light_diagram(line):
    str_diag = line.split(" ")[0]
    binary_diag = []
    for char in str_diag[1:-1]:  # Compute characters inside brackets
        if char == ".":
            binary_diag.append(0)
        else:
            binary_diag.append(1)
    return binary_diag


def apply_switch(diag, switch, is_part2):
    new_diag = diag.copy()
    for s in switch:
        new_diag[s] = (new_diag[s] + 1)
        if not is_part2:
            new_diag[s] = new_diag[s] % 2

    return new_diag


def run_switches(path, diag, switches, is_part2=False):
    if path:
        start_index = switches.index(path[-1])
    else:
        start_index = 0
    return [(path + [s], apply_switch(diag, s, is_part2)) for s in switches[start_index:]]


def solve_part1(data):
    total = 0
    k = 0

    for expected_diag, switches, joltage in data:
        presses_count = compute_line(expected_diag, switches)
        k += 1
        # print(f'Computed ->', k/len(data)*100)
        total += presses_count
    return total


def compute_line(expected_diag, switches, part2=False):
    # Initial state: path is empty and diag is full of zeros
    to_compute = [([], [0 for i in expected_diag])]
    pattern_encountered = []
    while to_compute:
        first_path, first_diag = to_compute[0]
        to_compute = to_compute[1:]
        res = run_switches(first_path, first_diag, switches, part2)
        find_matching = [r for r in res if r[1] == expected_diag]
        if find_matching:
            return len(find_matching[0][0])
        if part2:
            res = [elt for elt in res if is_valid(elt[1], expected_diag) and elt[1] not in pattern_encountered]
            pattern_encountered += [elt[1] for elt in res]

        to_compute += res


def is_valid(pattern, expected_pattern):
    for i in range(len(pattern)):
        if pattern[i] > expected_pattern[i]:
            return False
    return True


def solve_part2(data):
    total = 0
    k = 0

    for expected_diag, switches, joltage in data:
        presses_count = compute_line(joltage, switches, True)
        k += 1
        print(f'Computed ->', k / len(data) * 100)
        total += presses_count
    return total


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    # start_time = time.time()
    # print("Part 1: " + str(solve_part1(data)))
    # print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
