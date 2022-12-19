#!/usr/bin/env python3
import time

chamber = [["."] * 7 for k in range(3)]
highest_rock = -1
block_height = 0
block_width = [0, 0]


def read_file(file_name):
    with open(file_name) as input_file:
        return input_file.read().splitlines()[0]


def add_rock(id):
    global chamber, block_height, block_width
    if id % 5 == 0:
        block_height = 1
    elif id % 5 == 1:
        block_height = 3
    elif id % 5 == 2:
        roomblock_height_required = 3
    elif id % 5 == 3:
        block_height = 4
    else:
        block_height = 2

    required_space = highest_rock + block_height + 4 - len(chamber)
    if required_space > 0:
        for k in range(required_space):
            chamber.append(["."] * 7)
    if id % 5 == 0:  # Horizontal Rock
        block_width = [2, 5]
        chamber[highest_rock + 4] = ["."] * 2 + [str(id)] * 4 + ["."]
        return highest_rock + 4
    elif id % 5 == 1:  # Cross Rock
        block_width = [2, 4]
        chamber[highest_rock + 6][3] = str(id)
        chamber[highest_rock + 5] = ["."] * 2 + [str(id)] * 3 + ["."] * 2
        chamber[highest_rock + 4][3] = str(id)
        return highest_rock + 6
    elif id % 5 == 2:  # L Inverse Rock
        block_width = [2, 4]
        chamber[highest_rock + 6][4] = str(id)
        chamber[highest_rock + 5][4] = str(id)
        chamber[highest_rock + 4] = ["."] * 2 + [str(id)] * 3 + ["."] * 2
        return highest_rock + 6
    elif id % 5 == 3:  # Vertical Rock
        block_width = [2, 2]
        for k in range(4):
            chamber[highest_rock + 4 + k][2] = str(id)
        return highest_rock + 7
    elif id % 5 == 4:  # Square Rock
        block_width = [2, 3]
        chamber[highest_rock + 4] = ["."] * 2 + [str(id)] * 2 + ["."] * 3
        chamber[highest_rock + 5] = ["."] * 2 + [str(id)] * 2 + ["."] * 3
        return highest_rock + 5


def move_rock(id, position, dist):
    global block_width
    # Check rock can move (no items below)
    for i in range(block_height):
        for k in range(block_width[0], block_width[1] + 1):
            if position - i >= 0 and chamber[position - i][k] == id:  # Rock detected
                if not 0 <= k + dist < 7:  # Border
                    return False
                next = chamber[position - i][k + dist]
                if next != "." and next != id:  # Piece next
                    return False

    # Move rock
    for i in range(block_height):
        for k in range(block_width[0], block_width[1] + 1):
            if dist >= 1:
                current = block_width[1] + block_width[0] - k
            else:
                current = k
            if position - i >= 0 and 0 <= current + dist < 7 and chamber[position - i][current] == id:
                chamber[position - i][current] = "."
                chamber[position - i][current + dist] = id
    block_width[0] += dist
    block_width[1] += dist

    return True


def can_rock_fall(id, position):
    # Check rock can fall (no items below)
    for i in range(block_height):
        # for k in range(block_width[0], block_width[1] + 1):
        for k in range(block_width[0], block_width[1] + 1):
            if position - i >= 0 and chamber[position - i][k] == id:
                if position - i == 0:  # Bottom reached
                    return False
                below = chamber[position - 1 - i][k]
                if below != "." and below != id:  # Piece down
                    return False
    return True


def rock_fall(id, position):
    # Move piece down
    for i in range(4):
        for k in range(block_width[0], block_width[1] + 1):
            if position - 3 + i >= 0 and chamber[position - 3 + i][k] == id:
                chamber[position - 3 + i][k] = "."
                chamber[position - 4 + i][k] = id

    return True


def run(data, turns):
    global highest_rock
    gas_index = 0
    for i in range(2022):
        position = add_rock(i)
        # display()
        if data[gas_index % len(data)] == ">":
            move_rock(str(i), position, 1)
        else:
            move_rock(str(i), position, -1)
        gas_index += 1
        while can_rock_fall(str(i), position):
            # display()
            rock_fall(str(i), position)
            position -= 1
            # display()
            if data[gas_index % len(data)] == ">":
                move_rock(str(i), position, 1)
            else:
                move_rock(str(i), position, -1)
            gas_index += 1
            # display()
        highest_rock = max(highest_rock, position)
        # display()


def solve_part1(data, turns=2022):
    run(data, turns)

    return highest_rock + 1


def display():
    print()
    for i in range(len(chamber)):
        print("".join(chamber[len(chamber) - 1 - i]))


def solve_part2(data):
    return data


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(data)))
    print("Solved in : ", (time.time() - start_time))
    # Part 2
    data = read_file("inputs/part2.example")
    # data = read_file("inputs/part2.input")
    print("Part 2: " + str(solve_part2(data)))
