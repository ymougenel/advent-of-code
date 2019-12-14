#!/usr/bin/env python3


def read_file(fileName):
    inputFile = open(fileName, "r")
    data = inputFile.read()
    inputFile.close()
    return list(map(int, data.split(',')))


def restore_alarm(numbers, noun, verb):
    numbers[1] = noun
    numbers[2] = verb


def process_instruction(cursor, numbers):
    if numbers[cursor] == 1:
        instruction1(cursor, numbers)
    elif numbers[cursor] == 2:
        instruction2(cursor, numbers)
    elif numbers[cursor] == 99:
        intruction99(cursor, numbers)
    else:
        print("Error while parsing cursor at: " + str(cursor) + ", value = " + str(numbers[cursor]))


def instruction1(cursor, numbers):
    # print("processing opcode 1 (from cursor " + str(cursor) + ")")
    position1 = numbers[cursor + 1]
    position2 = numbers[cursor + 2]
    destination = numbers[cursor + 3]
    numbers[destination] = numbers[position1] + numbers[position2]


def instruction2(cursor, numbers):
    # print("processing opcode 2 (from cursor " + str(cursor) + ")")
    position1 = numbers[cursor + 1]
    position2 = numbers[cursor + 2]
    destination = numbers[cursor + 3]
    numbers[destination] = numbers[position1] * numbers[position2]


def intruction99(cursor, numbers):
    # print("processing opcode 99 (from cursor " + str(cursor) + ")")
    pass


def update_cursor(cursor, currentInstruction):
    return cursor + 4


def run_simulation(data):
    # print("Running simulation for verb=" + str(verb) + " ,noun=" + str(noun))
    numbers = data.copy()
    cursor = 0
    opcode = numbers[0]
    while opcode != 99 and cursor < len(numbers):
        process_instruction(cursor, numbers)
        opcode = numbers[cursor]
        cursor = update_cursor(cursor, opcode)
    return numbers



def found_matching_noun_verb(data):
    for noun in range(len(data)):
        for verb in range(len(data)):
            try:
                restore_alarm(data, noun, verb)
                res = run_simulation(data)
                result = res[0]
            except IndexError:
                pass
            if result == 19690720:
                solution = noun * 100 + verb
                # print("****** Found matching: verb=" + str(noun) + " ,noun=" + str(verb) + "-> " + str(solution))
                return solution


if __name__ == '__main__':
    data = read_file("inputs/day2_example.input")
    run_simulation(data)
    print(data[0])
    # print(found_matching_noun_verb(data))
