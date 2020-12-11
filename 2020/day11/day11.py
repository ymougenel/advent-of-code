#!/usr/bin/env python3
import copy


def read_file(file_name):
    with open(file_name) as input_file:
        return [list(line) for line in input_file.read().splitlines()]


def display_room(room, heigh):
    for i in range(heigh):
        print(room[i])


def place_participants(room, height, width):
    r = copy.deepcopy(room)
    for i in range(height):
        for j in range(width):
            if __empty_and_no_adjacent(room, i, j):
                r[i][j] = "#"
            if __taken_and_4_adjacents(room, i, j):
                r[i][j] = "L"

    return r


def __taken_and_4_adjacents(room, i, j):
    taken = [seat_taken(room, i - 1, j - 1),
             seat_taken(room, i - 1, j),
             seat_taken(room, i - 1, j + 1),
             seat_taken(room, i, j - 1),
             seat_taken(room, i, j + 1),
             seat_taken(room, i + 1, j - 1),
             seat_taken(room, i + 1, j),
             seat_taken(room, i + 1, j + 1)
             ]

    return room[i][j] == "#" and taken.count(True) >= 4


def __empty_and_no_adjacent(room, i, j):
    return room[i][j] == "L" \
           and not seat_taken(room, i - 1, j - 1) \
           and not seat_taken(room, i - 1, j) \
           and not seat_taken(room, i - 1, j + 1) \
           and not seat_taken(room, i, j - 1) \
           and not seat_taken(room, i, j + 1) \
           and not seat_taken(room, i + 1, j - 1) \
           and not seat_taken(room, i + 1, j) \
           and not seat_taken(room, i + 1, j + 1)


def __check_position__(room, i, j):
    return 0 <= i < len(room) and 0 <= j < len(room[0])


def seat_available(room, i, j):
    return __check_position__(room, i, j) and room[i][j] == "L"


def seat_taken(room, i, j):
    return __check_position__(room, i, j) and room[i][j] == "#"


def count_seats_taken(room):
    return len([i for i in range(len(room)) for j in range(len(room[0])) if room[i][j] == "#"])


if __name__ == '__main__':
    # room = read_file("inputs/part1.example")
    room = read_file("inputs/part1.input")
    height = len(room)
    width = len(room[0])
    new_room = place_participants(room, height, width)
    while new_room != room:
        room = new_room
        new_room = place_participants(room, height, width)

    # display_room(new_room, height)
    seats_taken = count_seats_taken(new_room)
    print("Part1: " + str(seats_taken))

    # print("Part2: " + str(find_weakness_combinasion(data, weakness)))
