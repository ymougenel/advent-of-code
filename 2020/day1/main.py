#!/usr/bin/env python3


def read_file(fileName):
    inputFile = open(fileName, "r")
    data = inputFile.read().splitlines()
    inputFile.close()
    return list(map(int, data))


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
