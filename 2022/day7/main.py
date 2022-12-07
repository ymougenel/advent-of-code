#!/usr/bin/env python3
import sys

path = []
files = {}

files_size = {}


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def parse_commands(lines):
    global path
    for line in lines:
        content = line.split(" ")
        # Command
        if content[0] == "$":
            if content[1] == "cd":
                if content[2] == "..":
                    path.pop(-1)
                else:
                    path.append(content[2])
        # Output
        else:
            current_dir = "/".join(path)
            if current_dir in files:
                files[current_dir].append((content[1], content[0]))
            else:
                files[current_dir] = [(content[1], content[0])]

# def get_directory_size(dir):
#     children = files[dir]
#     size = 0
#     for child in children:
#         if child[1] != "dir":
#             size += int(child[1])
#         else:
#             if child[0] in files_size:
#                 size += files_size[child[0]]
#             else:
#                 size += get_directory_size(child[0])
#     files_size[dir] = size
#     return size


depths = {}


def depth(dir, current):
    global depths
    depths[dir] = current
    for child in files[dir]:
        if child[1] == "dir":
            depth(child[0], current + 1)


def getFolderChildren(dir):
    res = []
    for content in files[dir]:
        if content[1] == "dir":
            res.append(content[0])
    return res


def process_size():
    global depths
    i = 0
    depths[i] = "/"
    children = getFolderChildren("/")
    while children:
        i += 1
        new_children = []
        depths[i] = []
        for child in children:
            depths[i].append(child)
            new_children += getFolderChildren(child)
        children = new_children.copy()

    tree = list(depths.items())
    tree.reverse()
    for level in tree:
        for dir in level[1]:
            get_directory_size(dir)


def solve_part1():
    total_size = 0
    process_size()
    for dir, size in files_size.items():
        if size <= 100000:
            print(dir, size)
            total_size += size
    return total_size


def solve_part2(data):
    return data


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")

    parse_commands(data)
    print("Part 1: " + str(solve_part1()))

    # Part 2
    data = read_file("inputs/part2.example")
    # data = read_file("inputs/part2.input")
    print("Part 2: " + str(solve_part2(data)))
