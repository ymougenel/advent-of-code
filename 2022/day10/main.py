#!/usr/bin/env python3
from CPU import CPU


def read_file(file_name):
    with open(file_name) as input_file:
        return [line.split(" ") for line in input_file.read().splitlines()]


def solve_part1_2(instructions):
    cpu = CPU()
    for inst in instructions:
        command = inst[0]
        value = None
        if len(inst) > 1:
            value = inst[1]
        while cpu.run(command, value) != 0:
            pass

    for line in cpu.crt:
        print("".join(line))
    return sum(cpu.counts)


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part2.example")
    data = read_file("inputs/part1.input")
    print("Part 1 and 2: " + str(solve_part1_2(data)))
