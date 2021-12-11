def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def is_in_range(i, j, map):
    return i >= 0 and j >= 0 and i < len(map) and j < len(map[0])


def get_mininums(map):
    minimums = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            val = map[i][j]
            minimum = True
            if is_in_range(i - 1, j, map) and map[i - 1][j] <= val:
                minimum = False
            if is_in_range(i + 1, j, map) and map[i + 1][j] <= val:
                minimum = False
            if is_in_range(i, j - 1, map) and map[i][j - 1] <= val:
                minimum = False
            if is_in_range(i, j + 1, map) and map[i][j + 1] <= val:
                minimum = False
            if minimum:
                minimums.append(val)
    return minimums


def count_basin_size(map, i, j):
    if not is_in_range(i, j, map) or map[i][j] == 9:
        return 0
    else:
        map[i][j] = 9
        return 1 + count_basin_size(map, i - 1, j) + count_basin_size(map, i + 1, j) + count_basin_size(map, i,
                                                                                                        j - 1) + count_basin_size(
            map, i, j + 1)


def get_basins_lengths(map):
    lengths = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != 9:
                lengths.append(count_basin_size(map, i, j))
    return lengths


if __name__ == '__main__':
    content = read_file("inputs/part1.example.txt")
    content = read_file("inputs/input1.txt")
    map = []
    for line in content:
        row = []
        for i in line:
            row.append(int(i))
        map.append(row)
    print(sum([i + 1 for i in get_mininums(map)]))

    # Part 2
    lengths = get_basins_lengths(map)
    list.sort(lengths)
    print(lengths[-1] * lengths[-2] * lengths[-3])
