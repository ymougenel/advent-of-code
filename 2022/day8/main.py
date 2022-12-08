#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        return [
            [int(tree) for tree in line]
            for line in input_file.read().splitlines()
        ]


def count_visible_trees(trees):
    visible_trees = []
    SIZE = len(trees)
    i = 0
    while i < SIZE:
        j = 0
        maxi = [0, 0, 0, 0]
        while j < SIZE:
            check_tree_visibility(trees, visible_trees, (i, j), maxi, 0)
            check_tree_visibility(trees, visible_trees, (j, i), maxi, 1)
            check_tree_visibility(trees, visible_trees, (i, SIZE - 1 - j), maxi, 2)
            check_tree_visibility(trees, visible_trees, (SIZE - 1 - j, i), maxi, 3)
            j += 1
        i += 1

    return len(visible_trees)


def check_tree_visibility(trees, visible_trees, my_tree, maxi, rank):
    if is_in_border(my_tree[0], my_tree[1], len(trees)) or trees[my_tree[0]][my_tree[1]] > maxi[rank]:
        maxi[rank] = trees[my_tree[0]][my_tree[1]]
        if my_tree not in visible_trees:
            visible_trees.append(my_tree)


def is_in_border(i, j, SIZE):
    return i == 0 or i == SIZE - 1 or j == 0 or j == SIZE - 1


def solve_part1(data):
    return count_visible_trees(data)


def solve_part2(data):
    return data


if __name__ == '__main__':
    # Part 1
    trees = read_file("inputs/part1.example")
    trees = read_file("inputs/part1.input")

    print("Part 1: " + str(solve_part1(trees)))

    # Part 2
    data = read_file("inputs/part2.example")
    # data = read_file("inputs/part2.input")
    print("Part 2: " + str(solve_part2(data)))
