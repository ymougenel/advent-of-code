#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        return [(line[:len(line)//2], line[len(line)//2:]) for line in input_file.read().splitlines()]

def get_letter_points(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26

def solve_part1(data):
    points = 0
    for compartments in data:
        for letter in compartments[0]:
            if letter in compartments[1]:
                points += get_letter_points(letter)
                break
    return points

def solve_part2(data):
    points = 0
    compartments = data
    for i in range(0,len(data),3):
        for letter in compartments[i][0]+compartments[i][1]:
            if letter in compartments[i+1][0]+compartments[i+1][1] and letter in compartments[i+2][0]+compartments[i+2][1]:
                points += get_letter_points(letter)
                break
    return points

if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(data)))

    # Part 2
    print("Part 2: " + str(solve_part2(data)))
