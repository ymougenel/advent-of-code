#!/usr/bin/env python3


def read_file(file_name):
    with open(file_name) as input_file:
        return [int(line) for line in input_file.read().splitlines()]


def get_chain_jolt_diff(chargers):
    chargers = sorted(chargers)
    diff_1 = 1 if chargers[0] == 1 else 0
    diff_3 = 1 if chargers[0] == 3 else 0
    for i in range(1, len(chargers)):
        if chargers[i] - chargers[i - 1] == 1:
            diff_1 += 1
        elif chargers[i] - chargers[i - 1] == 3:
            diff_3 += 1
    return diff_1 * (diff_3 +1)


if __name__ == '__main__':
    chargers = read_file("inputs/part1.input")
    # chargers = read_file("inputs/part1.example2")

    jolt_diff = get_chain_jolt_diff(chargers)
    print("Part1: " + str(jolt_diff))

    # print("Part2: " + str(find_weakness_combinasion(data, weakness)))
