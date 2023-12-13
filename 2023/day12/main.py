#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


# def is_possibility(springs, counts):
#     blocks = 0
#     for elt in springs:
#         if elt == "#":
#             blocks += 1
#         elif elt == ".":
#             if blocks != 0:
#                 if len(counts) == 0 or blocks != counts[0]:
#                     return False
#                 else:
#                     blocks = 0
#                     counts = counts[1:]
#         else:
#             print("Error, found unwanted symbol")
#             return -1
#     return (len(counts) == 0 and blocks == 0) or (len(counts) == 1 and blocks == counts[0])


# def find_possibilities(springs):
#     possibilities = [""]
#     for i in range(len(springs)):
#         tmp_poss = []
#         for poss in possibilities:
#             if springs[i] == "?":
#                 tmp_poss.append(poss + "#")
#                 tmp_poss.append(poss + ".")
#             else:
#                 tmp_poss.append(poss + springs[i])
#         possibilities = tmp_poss
#     return possibilities


def parse_springs(line):
    springs = line.split(" ")[0]
    counts = list(map(int, line.split(" ")[1].split(",")))
    return springs, counts


def solve_part(data):
    total = 0
    i = 0
    for spring, counts in data:
        possibilities = parse_opti_springs(spring, counts, sum(counts), spring.count("#"))
        i += 1
        print(i)
        total += len(possibilities)
    return total

# '.#.###.#.######'
def parse_opti_springs(line, counts, total_required, already_placed, parsed="", block_count=0, i=0):
    if i >= len(line):
        if (block_count == 0 and len(counts) == 0) or (len(counts) == 1 and block_count == counts[0]):
            return [parsed]
        else:
            return []
    if line[i] == "#":
        sub_sols = parse_opti_springs(line, counts, total_required, already_placed, parsed + "#", block_count + 1,
                                      i + 1)
        return sub_sols
    elif line[i] == ".":
        if block_count == 0:
            sub_sols = parse_opti_springs(line, counts, total_required, already_placed, parsed + ".", block_count,
                                          i + 1)
            return sub_sols
        else:
            if len(counts) == 0 or block_count != counts[0]:
                return []
            else:
                sub_sols = parse_opti_springs(line, counts[1:], total_required, already_placed, parsed + ".", 0, i + 1)
                return sub_sols
    else:
        sub_sols1 = parse_opti_springs(line[:i] + "." + line[i + 1:], counts, total_required, already_placed, parsed,
                                       block_count, i)
        sub_sols2 = []
        if already_placed <= total_required:
            sub_sols2 = parse_opti_springs(line[:i] + "#" + line[i + 1:], counts, total_required, already_placed + 1,
                                           parsed, block_count, i)
        return sub_sols1 + sub_sols2


def unfold(data, time=5):
    new_data = []
    for line, counts in data:
        new_line = ""
        for i in range(time):
            new_line += line + "?"
        new_data.append((new_line[:-1], counts * time))
    return new_data


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    data = [parse_springs(line) for line in data]

    print("Part 1: " + str(solve_part(data)))
    print("Part1 Solved in : ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    data = unfold(data)
    print("Part 2: " + str(solve_part(data)))
    print("Part 2 Solved in : ", (time.time() - start_time))
