#!/usr/bin/env python3
import time

directions = ""
steps_count = 0


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines() if line != ""]


def parse_nodes(data):
    global directions
    directions = data[0]
    elements = {}
    for i in range(1, len(data)):
        line = data[i]
        elements[line[0:3]] = (line[7:10], line[12:15])
    return elements


def forward(current, elements):
    dir = directions[steps_count % len(directions)]
    return choose(current, elements, dir)


def choose(current, elements, dir):
    toward = elements[current]
    if dir == "L":
        return toward[0]
    else:
        return toward[1]


def solve_part1(elements):
    global steps_count
    current = "AAA"
    while current != "ZZZ":
        current = forward(current, elements)
        steps_count += 1

    return steps_count


def solve_part2(elements):
    global steps_count
    current_nodes = [node for node in elements.keys() if node[2] == "A"]
    DIRECTIONS_LEN = len(directions)
    NODES_LEN = len(current_nodes)
    while True:
        first = current_nodes[0]
        chosen_direction = []
        # Run the first element until his end
        while chosen_direction == [] or first[2] != "Z":
            dest = directions[steps_count % DIRECTIONS_LEN]
            chosen_direction.append(dest)
            first = choose(first, elements, dest)
            steps_count += 1
        current_nodes[0] = first

        # Rerun other nodes
        for i in range(1, NODES_LEN):
            elt = current_nodes[i]
            for j in range(len(chosen_direction)):
                elt = choose(elt, elements, chosen_direction[j])
            current_nodes[i] = elt
        # print(steps_count)
        # CHeck if all done
        IS_SOLUTION = True
        i = 1
        while i < NODES_LEN and IS_SOLUTION:
            IS_SOLUTION = current_nodes[i][2] == "Z"
            i += 1
        if IS_SOLUTION:
            return steps_count


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/example1.txt")

    # data = read_file("inputs/input.txt")
    elements = parse_nodes(data)
    print("Part 1: " + str(solve_part1(elements)))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    steps_count = 0
    data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")
    elements = parse_nodes(data)
    print("Part 2: " + str(solve_part2(elements)))
    print("Solved in : ", (time.time() - start_time))

