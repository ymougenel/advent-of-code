#!/usr/bin/env python3


def read_file(file_name):
    with open(file_name) as input_file:
        return [int(line) for line in input_file.read().splitlines()]


def generate_additions(data):
    return [[i + data[j] for i in data[j + 1:]] for j in range(len(data))]

# Find first digit (after preamble) that is not the sum of two of the previous elements
def find_weakness(data, addidions, preamble_size):
    for i in range(preamble_size, len(data)):
        found = False
        for j in range(i - preamble_size, i):
            if data[i] in addidions[j]:
                found = True
        if not found:
            return data[i]


def find_weakness_combinasion(data, weakness):
    combinaison = []
    for i in data:
        combinaison.append(i)
        combinaison.reverse()
        comb_sum = sum(combinaison)
        while comb_sum > weakness:
            combinaison.pop()
            comb_sum = sum(combinaison)
        combinaison.reverse()
        if comb_sum == weakness:
            return min(combinaison) + max(combinaison)


if __name__ == '__main__':
    data = read_file("inputs/part1.input")
    # data = read_file("inputs/part1.example")
    additions = generate_additions(data)
    weakness = find_weakness(data, additions, 25)
    print("Part1: " + str(weakness))
    print("Part2: " + str(find_weakness_combinasion(data, weakness)))
