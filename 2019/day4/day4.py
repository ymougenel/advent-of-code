#!/usr/bin/env python3

from collections import Counter

def check_two_adjacent_digits(number):
    digits = convertToArray(number)
    current = None
    for digit in digits:
        if current == digit:
            return True
        current = digit
    return False


def check_adjacents_not_part_larger_group(number):
    digits = convertToArray(number)
    dict = Counter(digits).most_common()
    for el in dict:
        if el[1] == 2:
            return True
    return False


def check_never_decrease(number):
    digits = convertToArray(number)
    current = digits[0]
    for digit in digits:
        if current > digit:
            return False
        current = digit
    return True


def convertToArray(number):
    return list(map(lambda x: int(x), str(number)))


if __name__ == '__main__':
    begin = 197487
    end = 673251

    count = 0
    for k in range(begin, end):
        if check_never_decrease(k) and check_two_adjacent_digits(k) and check_adjacents_not_part_larger_group(k):
            count += 1
    print(count)
