#!/usr/bin/env python3
import time
import copy


def read_file(file_name):
    with open(file_name) as input_file:
        lines = [line for line in input_file.read().splitlines()]
    puzzle = []
    directions = []
    is_puzzle = True
    for line in lines:
        if len(line) == 0:
            is_puzzle = False
        elif is_puzzle:
            puzzle.append(line)
        else:
            directions += list(line)

    return [list(elt) for elt in puzzle], directions


def find_initial_position(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "@":
                return i, j


def can_move(position, dir, puzzle):
    i, j = position
    new_i, new_j = i + dir[0], j + dir[1]
    if puzzle[i][j] == "#" or puzzle[new_i][new_j] == "#":
        return False
    if puzzle[i][j] == ".":
        return True
    elif puzzle[i][j] in ["[", "]"] and dir[0] != 0:
        if puzzle[i][j] == "[":
            other_j = j + 1
        else:
            other_j = j - 1
        if puzzle[new_i][j] == "." and puzzle[new_i][other_j] == ".":
            return True
        else:
            return can_move((new_i, new_j), dir, puzzle) and can_move((new_i, other_j), dir, puzzle)
    elif puzzle[new_i][new_j] == ".":
        return True
    else:
        return can_move((new_i, new_j), dir, puzzle)


def move(position, dir, puzzle, new_puzzle, processed = []):
    i, j = position

    processed.append((i,j))
    current_elt = puzzle[i][j]
    # Detect end of movement
    if current_elt == ".":
        new_puzzle[i][j] = puzzle[i - dir[0]][j - dir[1]]
        return new_puzzle

    # Special process for extended boxes
    if current_elt in ["[", "]"] and dir[0] != 0:
        if current_elt == "[":
            other_j = j + 1
        else:
            other_j = j - 1
        if (i, other_j) not in processed:
            new_puzzle[i][other_j] = "."
        move((i + dir[0], other_j + dir[1]), dir, puzzle, new_puzzle, processed)

    # Copy previous value and move next object
    new_puzzle[i][j] = puzzle[i - dir[0]][j - dir[1]]
    move((i + dir[0], j + dir[1]), dir, puzzle, new_puzzle, processed)

    # Special case for current position
    if current_elt == "@":
        new_puzzle[i][j] = "."
    return new_puzzle


def map_str_to_dir(str_dir):
    if str_dir == ">":
        return 0, 1
    elif str_dir == "<":
        return 0, -1
    elif str_dir == "^":
        return -1, 0
    elif str_dir == "v":
        return 1, 0
    else:
        return None


def run_simulation(puzzle, directions):
    n = len(puzzle)
    position = find_initial_position(puzzle)
    k = 0
    for str_dir in directions:
        dir = map_str_to_dir(str_dir)
        new_puzzle = copy.deepcopy(puzzle)
        if can_move(position, dir, puzzle):
            zoom_display(puzzle, position)
            puzzle = move(position, dir, puzzle, new_puzzle, [])
            position = position[0] + dir[0], position[1] + dir[1]
        # display(puzzle)
        print(str_dir)
        zoom_display(puzzle,position)
        k += 1
        print("Processed %d%", k * 100 / len(directions))
    return puzzle


def solve_part1(data):
    puzzle, directions = data
    puzzle = copy.deepcopy(puzzle)
    puzzle = run_simulation(puzzle, directions)
    return calculate_gps_coordinates(puzzle)


def calculate_gps_coordinates(puzzle):
    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] in ["O", "["]:
                total += 100 * i + j
    return total

def zoom_display(puzzle,position):
    i,j = position
    window = 5
    for m in range(max(0,i-window), min(i+window, len(puzzle))):
        tmp = ""
        for n in range(max(0,j-window), min(j+window, len(puzzle[0]))):
            tmp+=puzzle[m][n]
        print(tmp)
    print("\n")
def display(puzzle):
    for line in puzzle:
        print(line)

    print("---")


def extend_puzzle(initial_puzzle):
    extended_puzzle = []
    for line in initial_puzzle:
        extended_row = []
        for elt in line:
            if elt == "#":
                extended_row += ["#", "#"]
            elif elt == "@":
                extended_row += ["@", "."]
            elif elt == "O":
                extended_row += ["[", "]"]
            elif elt == ".":
                extended_row += [".", "."]
            else:
                print("Character unknown")
        extended_puzzle.append(extended_row)
    return extended_puzzle


def solve_part2(data):
    puzzle, directions = data
    save_puzzle = copy.deepcopy(puzzle)
    puzzle = run_simulation(puzzle, directions)
    display(puzzle)
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if save_puzzle[i][j] == "#" and puzzle[i][j] != "#":
                print("Error encountered at %d;%d",i,j)
            if puzzle[i][j] == "#" and save_puzzle[i][j] != "#":
                print("Error encountered at %d;%d",i,j)
            if puzzle[i][j] == "[" and puzzle[i][j+1] != "]":
                print("Missing part at %d;%d",i,j)
    return calculate_gps_coordinates(puzzle)


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/example2.txt")
    # data = read_file("inputs/example3.txt")
    data = read_file("inputs/input.txt")
    # <^>v>>>^^
    # data = read_file("inputs/example.txt")

    # Part 1
    start_time = time.time()
    # print("Part 1: " + str(solve_part1(data)))
    # print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    extended_puzzle = extend_puzzle(data[0])
    save_puzzle = copy.deepcopy(extended_puzzle)
    print("Part 2: " + str(solve_part2((extended_puzzle, data[1]))))
    print("-> Part2 solved in: ", (time.time() - start_time))
