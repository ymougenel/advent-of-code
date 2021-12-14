#!/usr/bin/env python3
import math
import time
import numpy as np
from collections import Counter

ORD_A = 65


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def get_transformation_matrix(rules, length=26):
    transformation_matrix = np.zeros([length, length], int)
    for rule in rules:
        part_1 = rule.rsplit(" -> ")[0]
        part_2 = rule.rsplit(" -> ")[1]
        index_first_letter = ord(part_1[0]) - ORD_A
        index_second_letter = ord(part_1[1]) - ORD_A
        index_third_letter = ord(part_2) - ORD_A + 1
        transformation_matrix[index_first_letter][index_second_letter] = index_third_letter
    return transformation_matrix


def map_letter_to_vector(letter, length=26):
    index = ord(letter) - ORD_A
    vec = np.zeros(length, int)
    vec[index] = 1
    return vec


if __name__ == '__main__':
    start_time = time.time()

    # Part 1
    data = read_file("inputs/part1.example")


def transform(v1, v2, transfo_matrix, length=26):
    res = np.matmul(transfo_matrix, v2)
    res = np.matmul(v1, res.transpose())

    vec = np.zeros(length, int)
    if res != 0:
        vec[res - 1] = 1
    return vec


def execute_transformation(polymer_matrix, transformation_matrix):
    insertions = []
    SIZE = polymer_matrix.shape[0]
    for i in range(0, SIZE - 1):
        insertions.append([i, transform(polymer_matrix[i], polymer_matrix[i + 1], transformation_matrix)])

    new_polymer = np.zeros([len(insertions) + SIZE, 26], int)
    done = 0
    for i in range(new_polymer.shape[0]):
        found = False
        for insert in insertions:
            if insert[0] + done < i:
                new_polymer[i] = insert[1]
                insert[0] = math.inf
                done += 1
                found = True
        if not found:
            new_polymer[i] = polymer_matrix[i - done]
            # TODO: break
    return new_polymer


def matrix_to_polymer(matrix):
    res = ""
    for i in range(0, len(matrix)):
        letter_index = 0
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 1:
                letter_index = j
                res += chr(letter_index + 65)
    return res


if __name__ == '__main__':
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    tranfo_m = get_transformation_matrix(data[2:])

    polymer_str = data[0]
    polymer_matrix = np.zeros([len(polymer_str), 26], int)
    for i in range(0, len(polymer_matrix)):
        polymer_matrix[i][ord(polymer_str[i]) - ORD_A] = 1
    for i in range(40):
        # print(matrix_to_polymer(polymer_matrix))
        polymer_matrix = execute_transformation(polymer_matrix, tranfo_m)
    occurences = Counter(matrix_to_polymer(polymer_matrix))
    print(max(occurences.values()) - min(occurences.values()))

# print(matrix_to_polymer(polymer_matrix))
