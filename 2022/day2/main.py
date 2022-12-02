#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        return [line.split(" ") for line in input_file.read().splitlines()]

def get_round_score(him, you):
    points = 0
    if you == "X": # ROCK
        points += 1
        if him == "A": # ROCK -> equality
            points += 3
        elif him == "C": # Scissors -> Win
            points += 6
    elif you == "Y": # PAPER
        points += 2
        if him == "A": # ROCK -> WIN
            points += 6
        elif him == "B": # Paper -> Equality
            points += 3
    elif you == "Z": # SCISSORS
        points += 3
        if him == "B": # PAPER -> WIN
            points += 6
        elif him == "C": # Scissors -> Equality
            points += 3
    return points

def get_round_score2(him, you):
    points = 0
    if you == "X": # Loose
        points += 0
        if him == "A": # ROCK -> SCISSORS
            points += 3
        elif him == "B": # PAPER -> ROCK
            points += 1
        elif him == "C": # SCISSORS -> PAPER
            points += 2
    elif you == "Y": # Equality
        points += 3
        if him == "A": # ROCK -> ROCK
            points += 1
        elif him == "B": # PAPER -> PAPER
            points += 2
        elif him == "C": # SCISSORS -> SCISSORS
            points += 3
    elif you == "Z": # Win
        points += 6
        if him == "A": # ROCK -> PAPER
            points += 2
        elif him == "B": # PAPER -> SCISSORS
            points += 3
        elif him == "C": # Scissors -> ROCK
            points += 1
    return points
if __name__ == '__main__':
    # Part 1
    #data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    points = 0
    for round in data:
        points += get_round_score(round[0],round[1])
    print(points)

    # Part 2
    #data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    points = 0
    for round in data:
        points += get_round_score2(round[0],round[1])
    print(points)
