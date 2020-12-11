#!/usr/bin/env python3
import copy


def read_file(file_name):
    with open(file_name) as input_file:
        return [list(line) for line in input_file.read().splitlines()]


def display_room(room, height):
    for i in range(height):
        print(room[i])


def place_participants(room, height, width):
    r = copy.deepcopy(room)
    for i in range(height):
        for j in range(width):
            if __empty_and_no_taken_direction__(room, i, j):
                r[i][j] = "#"
            if __taken_and_5_directions__(room, i, j):
                r[i][j] = "L"
    return r


def __taken_and_4_adjacents(room, i, j):
    taken = [__seat_taken__(room, i - 1, j - 1),
             __seat_taken__(room, i - 1, j),
             __seat_taken__(room, i - 1, j + 1),
             __seat_taken__(room, i, j - 1),
             __seat_taken__(room, i, j + 1),
             __seat_taken__(room, i + 1, j - 1),
             __seat_taken__(room, i + 1, j),
             __seat_taken__(room, i + 1, j + 1)
             ]

    return room[i][j] == "#" and taken.count(True) >= 4


def __first_seat_in_direction__(room, i, j, vi, vj):
    if not __check_position__(room, i + vi, j + vj):
        return "L"
    elif room[i + vi][j + vj] != ".":
        return room[i + vi][j + vj]
    else:
        return __first_seat_in_direction__(room, i + vi, j + vj, vi, vj)


# Check the first seats (taken of free) in all 8 directions
def __get_first_seats_in_all_directions(room, i, j):
    return [__first_seat_in_direction__(room, i, j, - 1, - 1),
            __first_seat_in_direction__(room, i, j, -1, 0),
            __first_seat_in_direction__(room, i, j, -1, 1),
            __first_seat_in_direction__(room, i, j, 0, - 1),
            __first_seat_in_direction__(room, i, j, 0, 1),
            __first_seat_in_direction__(room, i, j, 1, - 1),
            __first_seat_in_direction__(room, i, j, 1, 0),
            __first_seat_in_direction__(room, i, j, 1, 1)
            ]

# Check that the seat is empty and can see no taken seats in all directions
def __empty_and_no_taken_direction__(room, i, j):
    if room[i][j] != "L":
        return False

    return __get_first_seats_in_all_directions(room, i, j).count("#") == 0


# Check that the seat is empty and can see less than 5 seats
def __taken_and_5_directions__(room, i, j):
    if room[i][j] != "#":
        return False
    return __get_first_seats_in_all_directions(room, i, j).count("#") >= 5


def __empty_and_no_direct_adjacent__(room, i, j):
    return room[i][j] == "L" \
           and not __seat_taken__(room, i - 1, j - 1) \
           and not __seat_taken__(room, i - 1, j) \
           and not __seat_taken__(room, i - 1, j + 1) \
           and not __seat_taken__(room, i, j - 1) \
           and not __seat_taken__(room, i, j + 1) \
           and not __seat_taken__(room, i + 1, j - 1) \
           and not __seat_taken__(room, i + 1, j) \
           and not __seat_taken__(room, i + 1, j + 1)


def __check_position__(room, i, j):
    return 0 <= i < len(room) and 0 <= j < len(room[0])


def __seat_available__(room, i, j):
    return __check_position__(room, i, j) and room[i][j] == "L"


def __seat_taken__(room, i, j):
    return __check_position__(room, i, j) and room[i][j] == "#"


def __count_seats_taken__(room):
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

    seats_taken = __count_seats_taken__(new_room)
    print("Part2: " + str(seats_taken))
