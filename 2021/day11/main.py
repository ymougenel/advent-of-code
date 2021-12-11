#!/usr/bin/env python3

nb_flashes = 0


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()[ for j in range(len(line))]]

    def execute_step(octopus):
        found = False
        global nb_flashes
        for i in range(len(octopus)):
            for j in range(len(octopus[0])):
                if not octopus[i][j][1] and octopus[i][j][0] > 9:
                    nb_flashes += 1
                    found = True
                    flash(i, j, octopus)
        return found

    def next_step(octopus):
        # Increment energy
        for i in range(len(octopus)):
            for j in range(len(octopus[0])):
                octopus[i][j][0] += 1

        # Execute flash chain
        while execute_step(octopus):
            print(i)

        print()
        # Reset flashed octopuses
        for i in range(len(octopus)):
            for j in range(len(octopus[0])):
                if octopus[i][j][1]:
                    octopus[i][j][0] = 0
                octopus[i][j][1] = False

    def flash(i, j, octopus):
        octopus[i][j][1] = True
        for m in range(-1, 2):
            for n in range(-1, 2):
                if is_in_range(i + m, j + n, octopus):
                    octopus[i + m][j + n][0] += 1

    def is_in_range(i, j, tab):
        return 0 <= i < len(tab) and 0 <= j < len(tab[0])

    def all_flashed(octopuses):
        for i in range(len(octopuses)):
            for j in range(len(octopuses[0])):
                if octopuses[i][j][0] != 0:
                    return False
        return True

    if __name__ == '__main__':

        # Part 1
        data = read_file("inputs/part1.example")
        data = read_file("inputs/part1.input")

        octopuses = []
        for line in data:
            row = []
            for i in line:
                if i != "\n":
                    row.append([int(i), False])
            octopuses.append(row)
        # for i in range(100):
        #     next_step(octopuses)
        # print(nb_flashes)

        # Part 2
        simultaneously = False
        i = 0
        while not all_flashed(octopuses):
            next_step(octopuses)
            i += 1
        print(i)
