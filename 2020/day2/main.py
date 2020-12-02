#!/usr/bin/env python3

def count_valid_pass(file_name):
    with open(file_name) as input_file:
        return len([line for line in input_file.read().splitlines() if validate_position(line)])


# Validate Password occurrence policy
def validate_occurences(line):
    parts = line.split(" ")
    min = parts[0].split("-")[0]
    max = parts[0].split("-")[1]
    letter = parts[1][0]
    occurrences = parts[2].count(letter)
    return int(min) <= occurrences and occurrences <= int(max)


# Validate Password position policy
def validate_position(line):
    parts = line.split(" ")
    first_index = int(parts[0].split("-")[0]) - 1
    last_index = int(parts[0].split("-")[1]) - 1
    letter = parts[1][0]
    password = parts[2][0:]

    first_match = bool(password[first_index] == letter)
    last_match = bool(last_index >= len(password) or password[last_index] == letter)
    return first_match != last_match


if __name__ == '__main__':
    # file = "inputs/part1.example"
    file = "inputs/part1.input"
    print(count_valid_pass(file))
