#!/usr/bin/env python3
from collections import Counter

def read_file(file_name):
    inputFile = open(file_name, "r")
    data = inputFile.read().splitlines()
    inputFile.close()
    passports = []
    i = 0
    for line in data:
        if line == "":
            i += 1
        else:
            if len(passports) > i:
                passports[i] += " " + line
            else:
                passports.append(" " + line)
    return passports


def count_yes(group_answer):
    return len([ans for ans in Counter(group_answer).keys() if ans != " "])


if __name__ == '__main__':
    # groups = read_file("inputs/part1.example")
    groups = read_file("inputs/part1.input")
    print(groups)
    print(sum([count_yes(yes) for yes in groups]))
