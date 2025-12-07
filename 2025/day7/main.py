#!/usr/bin/env python3
import time


def read_file(file_name):
    with open(file_name) as input_file:
        return [list(line) for line in input_file.read().splitlines()]


def solve_part1(maze):
    # Process line by line, and for each line counts occurred splitting
    return sum([run_classical_line(maze, i) for i in range(1, len(maze))])


def run_classical_line(maze, i):
    count = 0
    for j in range(len(maze[0])):
        if maze[i - 1][j] in ['S', '|']:
            if maze[i][j] == "^":
                count += 1
                if j > 0 and maze[i][j - 1] != "^":
                    maze[i][j - 1] = "|"
                if j < len(maze[0]) - 1 and maze[i][j + 1] != "^":
                    maze[i][j + 1] = "|"
            else:
                maze[i][j] = "|"
    return count


def print_maze(maze):
    for line in maze:
        print(line)
    print("\n")


def solve_part2(maze):
    computed_path = {}
    for i in range(1, len(maze)):
        run_quantum_line(maze, i, computed_path)


    all_final_paths = [maze[-1][j] for j in range(len(maze[0])) if maze[-1][j] != "."]
    count_timelines = 0
    for final_paths in all_final_paths:
        for path in final_paths:
            count_timelines += computed_path[path]
    return count_timelines


def run_quantum_line(maze, i, computed_path):
    # Process all line elements
    for j in range(len(maze[0])):

        # If below starting point
        if maze[i - 1][j] == "S":
            maze[i][j] = [(i - 1, j)]
            computed_path[(i - 1, j)] = 1

        # Elif below quantum timeline
        elif maze[i - 1][j] not in [".", "^"]:

            # If current element is splitter
            if maze[i][j] == "^":
                # Split the signal, and mark the splitter origin
                mark_splitter_path(i, j, maze[i - 1][j], computed_path)

                # Process left
                if maze[i][j - 1] == ".":
                    maze[i][j - 1] = [(i, j)]
                else:
                    maze[i][j - 1].append((i, j))

                # Process right
                if maze[i][j + 1] == ".":
                    maze[i][j + 1] = [(i, j)]
                else:
                    maze[i][j + 1].append((i, j))

            # Below timeline but not splitter
            else:
                # If "." found -> >The Path is the same as previous
                if maze[i][j] == ".":
                    maze[i][j] = maze[i - 1][j]
                # If post splitter -> The path is the concatenation of left splitter and previous path
                else:
                    maze[i][j] += maze[i - 1][j]


'''
 Process the new splitter timeline_count.
 The split count will be the sum of all the paths from previous splitter
'''
def mark_splitter_path(i, j, previous_path, computed_path):
    if (i, j) not in computed_path:
        computed_path[(i, j)] = 0

    for path in previous_path:
        computed_path[(i, j)] += computed_path[path]


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/example2.txt")
    data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    # print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
