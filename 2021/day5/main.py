#!/usr/bin/env python3


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]

"""
    Parse wind segments 
     ex: 0,9 -> 5,9 becomes ( (0,9), (5,9) )
    
    input: file content
    output list of segments
"""
def parse_content(data):
    segments = []
    for line in data:
        starting_pos = line.split("->")[0].split(",")
        ending_pos = line.split("->")[1].split(",")
        segments.append(((int(starting_pos[0]), int(starting_pos[1])), (int(ending_pos[0]), int(ending_pos[1]))))
    return segments


def put_winds_on_map(map, segments):
    for seg in segments:
        start = seg[0]
        end = seg[1]
        # Only consider vertical/horizontal lines
        if start[0] == end[0] or start[1] == end[1]:
            for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                for j in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                    map[i][j] += 1
        # Diagonal
        else:
            min_i = min(start[1], end[1])
            max_i = max(start[1], end[1])
            min_j = min(start[0], end[0])
            max_j = max(start[0], end[0])

            for i in range(max_i - min_i + 1):
                if (min_i == start[1] and min_j == start[0]) or (max_i == start[1] and max_j == start[0]):
                    map[min_i + i][min_j + i] += 1
                else:
                    map[min_i + i][max_j - i] += 1


def count_overlap(map):
    count = 0
    for line in map:
        for val in line:
            if val >= 2:
                count += 1
    return count


if __name__ == '__main__':
    # Part 1
    SIZE = 1000
    # data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")

    segments = parse_content(data)
    print(segments)

    map = [[0] * SIZE for i in range(SIZE)]
    put_winds_on_map(map, segments)
    print(count_overlap(map))
