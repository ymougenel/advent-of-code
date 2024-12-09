#!/usr/bin/env python3
import time
import copy

def read_file(file_name):
    with open(file_name) as input_file:
        return [[int(i) for i in line] for line in input_file][0]


def get_blocks(disk):
    blocks = []
    index = 0
    file_block = True
    for i in range(len(disk)):
        if file_block:
            symbol = index
            index += 1
        else:
            symbol = "."
        file_block = not file_block
        blocks.append([symbol, disk[i]])
    return blocks


def re_partition_part1(blocks):
    space_left = True
    space_index = 1
    while space_left:
        id_rightmost, count_rightmost = blocks.pop()
        if id_rightmost == ".":
            pass
        else:
            while space_index < len(blocks) and count_rightmost != 0:
                current_space = blocks[space_index][1]
                if current_space > 0:
                    if count_rightmost >= current_space:
                        count_rightmost -= current_space
                        blocks[space_index] = [id_rightmost, current_space]
                    else:
                        new_space = [".", current_space - count_rightmost]
                        blocks[space_index] = [id_rightmost, count_rightmost]
                        count_rightmost = 0
                        blocks = blocks[:space_index + 1] + [new_space] + blocks[space_index + 1:]
                        space_index -= 1
                space_index += 2
            if space_index > len(blocks):
                space_left = False
                blocks.append([id_rightmost, count_rightmost])
    return blocks


def solve_part1(disk):
    blocks = get_blocks(disk)
    blocks = re_partition_part1(blocks)
    # display(blocks)
    return get_checksum(blocks)


def get_checksum(blocks):
    i = 0
    cur_sum = 0
    for id, nb in blocks:
        for j in range(nb):
            if id != ".":
                cur_sum += id * i
            i += 1
    return cur_sum


def display(blocks):
    flatblock = ""
    for id, count in blocks:
        flatblock += str(id) * count
    print(flatblock)


def re_partition_part2(blocks):
    block_index = len(blocks) - 1
    while 0 < block_index:
        if blocks[block_index][0] == ".":
            block_index -=1
        else:
            space_index = 1
            placed = False
            while not placed and space_index< block_index:
                if blocks[space_index][0] != ".":
                    space_index += 1
                else:
                    space_left = blocks[space_index][1]
                    id_bloc, count_bloc = blocks[block_index]
                    if count_bloc == space_left:
                            placed = True
                            blocks[space_index] = blocks[block_index]
                            blocks[block_index] = [".", count_bloc]
                            space_index += 2
                    elif count_bloc < space_left:
                        placed = True
                        blocks[space_index] = [id_bloc, count_bloc]
                        blocks[block_index] = [".", count_bloc]
                        blocks = blocks[:space_index + 1] + [[".", space_left - count_bloc]] + blocks[space_index + 1:]
                    space_index += 1

            block_index -= 1
    return blocks


def solve_part2(disk):
    blocks = get_blocks(disk)
    blocks = re_partition_part2(blocks)
    return get_checksum(blocks)


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
