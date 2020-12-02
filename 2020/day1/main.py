#!/usr/bin/env python3


def read_file(file_name):
    with open(file_name) as input_file:
        return [int(line) for line in input_file.read().splitlines()]


def find_entries_making_sum(entries, sum):
    for i in range(0, len(entries)):
        for j in range(i + 1, len(entries)):
            for k in range(j+1, len(entries)):
                if (entries[i] + entries[j] + entries[k] == sum):
                    return (entries[i], entries[j], entries[k])


if __name__ == '__main__':
    # data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    (nb1, nb2, nb3) = find_entries_making_sum(data, 2020)
    print(nb1 * nb2 * nb3)
