#!/usr/bin/env python3

# inputFile = open("day2test.input", "r")
inputFile = open("day2.input", "r")
data = inputFile.read()
inputFile.close()

numbers = list(map(int, data.split(',')))

def restoreAlarm(numbers):
    numbers[1] = 12
    numbers[2] = 2

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
    print("processing opcode 99 (from cursor " + str(cursor) + ")")

def updateCursor(cursor, currentInstruction):
    return cursor + 4

cursor = 0
opcode = numbers[0]
restoreAlarm(numbers)
while (opcode != 99 and cursor < len(numbers)):
    processInstruction(cursor, numbers)
    opcode = numbers[cursor]
    cursor = updateCursor(cursor, opcode)

print(numbers)