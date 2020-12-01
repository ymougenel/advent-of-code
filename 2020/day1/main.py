#!/usr/bin/env python3


def read_file(fileName):
    inputFile = open(fileName, "r")
    data = inputFile.read().splitlines()
    inputFile.close()
    return list(map(int, data))


def find_entries_making_sum(entries, sum):
    for i in range(0, len(entries)):
        for j in range(i + 1, len(entries)):
            if (entries[i] + entries[j] == sum):
                return (entries[i], entries[j])


if __name__ == '__main__':
    # data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    (nb1, nb2) = find_entries_making_sum(data, 2020)
    print(nb1 * nb2)
