#!/usr/bin/env python3
from pile import *


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def get_empty_line_position(data):
    """
    Spot the empty line delimiter
    :param data: The file content
    :return: the index delimiter between stacks and instructions
    """
    i = 0
    while data[i] != "":
        i += 1
    return i


def parse_pile(content):
    """
    Creates piles based from the input content
    :param content: The raw lines
    :return: The matching piles
    """
    size = int(content[-1][-1])  # Last line indicates the column digits
    piles = []
    for i in range(size):
        piles.append(Pile())
    for i in range(0, len(content) - 1):
        j = 0
        while j * 4 + 1 < len(content[i]):
            if content[i][j * 4 + 1] != " ":
                piles[j].stack(content[i][j * 4 + 1])
            j += 1
    for pile in piles:
        pile.reverse()
    return piles


def run_instructions(instructions, piles, is_9000=True):
    """
    process all the instructions
    :param instructions: the raw input instructions
    :param piles: the piles
    :param is_9000: Either the code runs on version 9000 (part 1), or 9001 (part 2)
    """
    for instruction in instructions:
        content = instruction.split(" ")
        count = int(content[1])
        from_pile = int(content[3]) - 1
        to_pile = int(content[5]) - 1
        if is_9000:
            run_instruction_9000(piles, from_pile, to_pile, count)
        else:
            run_instruction_9001(piles, from_pile, to_pile, count)


def run_instruction_9000(piles, from_pile, to_pile, count):
    for i in range(count):
        elt = piles[from_pile].destack()
        piles[to_pile].stack(elt)


def run_instruction_9001(piles, from_pile, to_pile, count):
    tmp = Pile()
    for i in range(count):
        elt = piles[from_pile].destack()
        tmp.stack(elt)
    # reverse the taken pile
    while not tmp.is_empty():
        elt = tmp.destack()
        piles[to_pile].stack(elt)


def solve_part1(piles):
    res = ""
    for p in piles:
        elt = p.destack()
        res += elt
        p.stack(elt)
    return res


def solve_part2(data):
    return solve_part1(data) # Same as part 1


if __name__ == '__main__':
    # Part 1
    # data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    limit = get_empty_line_position(data)
    piles = parse_pile(data[0:limit])
    run_instructions(data[limit + 1:], piles)

    print("Part 1: " + str(solve_part1(piles)))

    # Part 2
    # data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")

    limit = get_empty_line_position(data)
    piles = parse_pile(data[0:limit])
    run_instructions(data[limit + 1:], piles, False)
    print("Part 2: " + str(solve_part1(piles)))
