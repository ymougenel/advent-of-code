#!/usr/bin/env python3
import math
import time
import re


def read_file(file_name):
    res = [[], [], []]
    with open(file_name) as input_file:
        content = [line for line in input_file.read().splitlines()]
        for line in content:
            index = -1
            digits = re.findall(r'(\d+)', line)

            if line.startswith("Button A"):
                index = 0
            elif line.startswith("Button B"):
                index = 1
            elif line.startswith("Prize:"):
                index = 2

            if index >= 0:
                res[index].append((int(digits[0]), int(digits[1])))
    return (res[0], res[1], res[2])


def find_combinaisons(a, b, p):
    max_k1 = min(p[0] // a[0] + 1, p[1] // a[1] + 1)
    max_k2 = min(p[0] // b[0] + 1, p[1] // b[1] + 1)
    combinaisons = []
    for k1 in range(0, max_k1 + 1):
        k2 = 0
        total1 = 0
        total2 = 0
        while k2 < max_k2 + 1 and total1 <= p[0] and total2 <= p[1]:
            total1 = a[0] * k1 + b[0] * k2
            total2 = a[1] * k1 + b[1] * k2
            if total1 == p[0] and total2 == p[1]:
                combinaisons.append((k1, k2))
            k2 += 1
    return combinaisons


def find_combinaisons_2(x, y, p):
    max_k1 = p // x
    max_k2 = p // y
    combinaisons = []
    for k1 in range(0, max_k1 + 1):
        k2 = 0
        total = 0
        while k2 < max_k2 + 1 and total < p:
            total = x * k1 + y * k2
            if total == p:
                combinaisons.append((k1, k2))
            k2 += 1
    return combinaisons


def find_best_cost(combinaisons, a_prize, b_prize):
    best = None
    for combinaison in combinaisons:
        a_count, b_count = combinaison
        cost = a_count * a_prize + b_count * b_prize
        if not best or cost < best:
            best = cost
    return best


def solve_part1(data):
    total_cost = 0
    for i in range(len(data[2])):
        a = data[0][i]
        b = data[1][i]
        p = data[2][i]
        combinaisons = find_combinaisons(a, b, p)
        cost = find_best_cost(combinaisons, 3, 1)
        if cost:
            total_cost += cost
        else:
            print("Error cost for: %d,%d,%d", a, b, p)

    return total_cost


def solve_part2(data):
    total_cost = 0
    for i in range(len(data[2])):
        a = data[0][i]
        b = data[1][i]
        p = data[2][i]
        PART2_GAP = 1000000000000
        p = (p[0] + PART2_GAP, p[1] + PART2_GAP)
        lcm0 = math.lcm(a[0], b[0])
        lcm1 = math.lcm(a[1], b[1])
        res0 = p[0] % lcm0
        res1 = p[1] % lcm1
        if res0 > res1:
            combinaisons = find_combinaisons_2(a[0], b[0], res0)
            k = p[0] // lcm0
            combinaisons = [(k1, k2) for (k1, k2) in combinaisons if a[1] * (k1 + k) + b[1] * (k2 + k) == p[1]]
        else:
            combinaisons = find_combinaisons_2(a[1], b[1], res1)
            k = p[1] // lcm1
            combinaisons = [(k1, k2) for (k1, k2) in combinaisons if a[0] * (k1 + k) + b[0] * (k2 + k) == p[0]]

        if combinaisons:
            print(combinaisons)
            cost = find_best_cost(combinaisons, 3, 1)
            total_cost += cost
        # else:
        #     print("Error cost for: %d,%d,%d", a, b, p)
        print("Processed: %d", i * 100 / len(data[0]))
    return total_cost


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    # data = read_file("inputs/input.txt")

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
