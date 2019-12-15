#!/usr/bin/env python3


def read_file(fileName):
    inputFile = open(fileName, "r")
    data = inputFile.read()
    inputFile.close()
    return data.split(",")


# Set alarm (from day2)
def restore_alarm(numbers, noun, verb):
    numbers[1] = noun
    numbers[2] = verb


def get_value(numbers, cursor):
    return int(numbers[cursor])


def set_value(numbers, address, value):
    numbers[address] = str(value)


# Return the opcode and the instruction parameter(opcode, [params])
def parse_parameter_instruction(numbers, cursor):
    # Parse instruction: digits-opcode
    instruction = numbers[cursor]
    opcode = int(instruction[len(instruction) - 1])
    digits = instruction[0:len(instruction) - 2]
    # Digits processed right -> left
    digits = list(digits[::-1])

    required_param = get_required_parameters(opcode)
    # Complete digits with default value (0)
    for k in range(len(digits), required_param):
        digits.append('0')

    # TODO: remove me
    # if (instruction != '99'):
    #     digits[len(digits) - 1] = '1'

    params = []
    for k in range(required_param - 1):
        # Position mode
        if digits[k] == '0':
            address = get_value(numbers, cursor + k + 1)
            params.append(get_value(numbers, address))
        # Immediate mode
        else:
            params.append(get_value(numbers, cursor + k + 1))
    return (opcode, params)


def parse_position_mode(cursor, numbers):
    opcode = int(numbers[cursor])
    if opcode == 99 or opcode == 4:
        return (opcode, 0)
    param1 = int(numbers[int(numbers[cursor + 1])])
    param2 = int(numbers[int(numbers[cursor + 2])])
    return (opcode, [param1, param2])


def process_instruction(cursor, numbers, param=0):
    inputs = parse_parameter_instruction(numbers, cursor)
    opcode = inputs[0]
    params = inputs[1]
    if opcode == 1:
        value = instruction1(numbers, cursor, params)
    elif opcode == 2:
        value = instruction2(numbers, cursor, params)
    elif opcode == 3:
        value = instruction3(numbers, get_value(numbers, cursor + 1), param)
    elif opcode == 4:
        value = instruction4(numbers, cursor)
    elif opcode == 9 or opcode == 99:
        value = intruction99(numbers, inputs)
    else:
        print("Error while parsing cursor at: " + str(cursor) + ", value = " + str(numbers[cursor]))
    return (opcode, value)


def instruction1(numbers, cursor, params):
    address = get_value(numbers, cursor + 3)
    value = params[0] + params[1]
    set_value(numbers, address, value)
    return value


def instruction2(numbers, cursor, params):
    address = get_value(numbers, cursor + 3)
    value = params[0] * params[1]
    set_value(numbers, address, value)
    return value


# Set param value at address
def instruction3(numbers, address, param):
    set_value(numbers, address, param)
    return param


# Output next value
def instruction4(numbers, cursor):
    address = get_value(numbers, cursor + 1)
    value = get_value(numbers, address)
    print(value)
    return None


def intruction99(cursor, numbers):
    # print("processing opcode 99 (from cursor " + str(cursor) + ")")
    return None


def get_required_parameters(opcode):
    if opcode == 1 or opcode == 2:
        return 3
    elif opcode == 4 or opcode == 3:
        return 1
    else:
        return 0


def update_cursor(cursor, currentInstruction):
    if currentInstruction == 99:
        return cursor
    else:
        return cursor + 1 + get_required_parameters(int(currentInstruction))


def run_simulation(data, input=0):
    # print("Running simulation for verb=" + str(verb) + " ,noun=" + str(noun))
    numbers = data.copy()
    cursor = 0
    opcode = numbers[0]
    param = input
    while opcode != "99" and cursor < len(numbers):
        res = process_instruction(cursor, numbers, param)
        opcode = res[0]
        param = res[1]
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
            if result == "19690720":
                solution = noun * 100 + verb
                print("****** Found matching: verb=" + str(noun) + " ,noun=" + str(verb) + "-> " + str(solution))
                return solution


if __name__ == '__main__':
    data = read_file("inputs/day5.input")
    run_simulation(data, 1)
    print(data[0])
