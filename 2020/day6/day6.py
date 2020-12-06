#!/usr/bin/env python3
from collections import Counter


def read_file(file_name):
    inputFile = open(file_name, "r")
    data = inputFile.read().splitlines()
    inputFile.close()
    groups = []
    i = 0
    for line in data:
        if line == "":
            i += 1
        else:
            if len(groups) <= i:
                groups.append([])
            groups[i].append(line)
    return groups


def count_anyone_yes(group_answer):
    return len([ans for ans in Counter("".join(group_answer)).keys()])


def count_everyone_yes(group_answer):
    res = Counter("".join(group_answer))
    return len([ans for ans in res if res[ans] == len(group_answer)])


if __name__ == '__main__':
    # groups = read_file("inputs/part1.example")
    groups = read_file("inputs/part1.input")
    print(sum([count_everyone_yes(ans) for ans in groups]))
