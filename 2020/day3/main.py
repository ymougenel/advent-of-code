#!/usr/bin/env python3

def get_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


# Display forest
def display(forest):
    for line in forest:
        print(line)


# Count trees encountered during the journey
def count_trees(forest, i, j, vi, vj, total_count=0):
    # Increments position with direction
    i += vi
    j = (j + vj) % len(forest[0])

    if (i >= len(forest)):
        return total_count

    if forest[i][j] == "#":
        total_count += 1

    return count_trees(forest, i, j, vi, vj, total_count)


if __name__ == '__main__':
    # forest = get_file("inputs/part1.example")
    forest = get_file("inputs/part1.input")
    # display(forest)

    slope1 = count_trees(forest, 0, 0, 1, 1, 0)
    slope2 = count_trees(forest, 0, 0, 1, 3, 0)
    slope3 = count_trees(forest, 0, 0, 1, 5, 0)
    slope4 = count_trees(forest, 0, 0, 1, 7, 0)
    slope5 = count_trees(forest, 0, 0, 2, 1, 0)

    print(slope1 * slope2 * slope3 * slope4 * slope5)
