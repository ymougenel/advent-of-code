#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        return [
            [int(tree) for tree in line]
            for line in input_file.read().splitlines()
        ]


def find_visible_trees(trees):
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

    return visible_trees


def check_tree_visibility(trees, visible_trees, my_tree, maxi, rank):
    if is_in_border(my_tree[0], my_tree[1], len(trees)) or trees[my_tree[0]][my_tree[1]] > maxi[rank]:
        maxi[rank] = trees[my_tree[0]][my_tree[1]]
        if my_tree not in visible_trees:
            visible_trees.append(my_tree)


def is_in_border(i, j, SIZE):
    return i == 0 or i == SIZE - 1 or j == 0 or j == SIZE - 1


def solve_part1(data):
    return len(find_visible_trees(data))


# TODO: clean function (code redundancy)
def find_view(trees, tree_pos):
    current_height = trees[tree_pos[0]][tree_pos[1]]
    views = [0, 0, 0, 0]
    SIZE = len(trees)
    ########
    i = tree_pos[0] - 1
    j = tree_pos[1]
    hidden = False
    while i >= 0 and not hidden:
        if trees[i][j] >= current_height:
            views[0] += 1
            hidden = True
        else:
            views[0] += 1
        i -= 1
    ########
    i = tree_pos[0] + 1
    j = tree_pos[1]
    hidden = False
    while i < SIZE and not hidden:
        if trees[i][j] >= current_height:
            views[1] += 1
            hidden = True
        else:
            views[1] += 1
        i += 1

    ########
    i = tree_pos[0]
    j = tree_pos[1] + 1
    hidden = False
    while j < SIZE and not hidden:
        if trees[i][j] >= current_height:
            views[2] += 1
            hidden = True
        else:
            views[2] += 1
        j += 1

    ########
    i = tree_pos[0]
    j = tree_pos[1] - 1
    hidden = False
    while j >= 0 and not hidden:
        if trees[i][j] >= current_height:
            views[3] += 1
            hidden = True
        else:
            views[3] += 1
        j -= 1
    return views


def solve_part2(data):
    visibles_trees = find_visible_trees(data)
    maxi = [0]
    for tree in visibles_trees:
        if not is_in_border(tree[0], tree[1], len(data)):
            views = find_view(data, tree)
            if multiply(views) >= multiply(maxi):
                maxi = views
    return multiply(maxi)


def multiply(list):
    total = 1
    for elt in list:
        total *= elt
    return total


if __name__ == '__main__':
    # Part 1
    trees = read_file("inputs/part1.example")
    trees = read_file("inputs/part1.input")

    print("Part 1: " + str(solve_part1(trees)))

    # Part 2
    print("Part 2: " + str(solve_part2(trees)))
