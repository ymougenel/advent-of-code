#!/usr/bin/env python3

# inputFile = open("day2test.input", "r")
inputFile = open("day2.input", "r")
data = inputFile.read()
inputFile.close()


def restoreAlarm(numbers, noun, verb):
    numbers[1] = noun
    numbers[2] = verb


def processInstruction(cursor, numbers):
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


def updateCursor(cursor, currentInstruction):
    return cursor + 4


def runSimulation(data, noun, verb):
    # print("Running simulation for verb=" + str(verb) + " ,noun=" + str(noun))
    numbers = list(map(int, data.split(',')))
    cursor = 0
    opcode = numbers[0]
    restoreAlarm(numbers, noun, verb)
    while (opcode != 99 and cursor < len(numbers)):
        processInstruction(cursor, numbers)
        opcode = numbers[cursor]
        cursor = updateCursor(cursor, opcode)

    return numbers[0]

for noun in range(len(data)):
    for verb in range(len(data)):
        try:
            result = runSimulation(data, noun, verb)
        except IndexError:
            pass
        if result == 19690720:
            solution=noun*100 + verb
            print("****** Found matching: verb=" + str(noun) + " ,noun=" + str(verb) + "-> " + str(solution))
