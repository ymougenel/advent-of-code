#!/usr/bin/env python3


def read_file(fileName):
    inputFile = open(fileName, "r")
    data = inputFile.read()
    inputFile.close()
    return list(map(int, data.split(',')))


# Set alarm (from day2)
def restore_alarm(numbers, noun, verb):
    numbers[1] = noun
    numbers[2] = verb


def get_value(numbers, cursor):
    return numbers[cursor]


def set_value(numbers, address, value):
    numbers[address] = value


# Return the opcode and the instruction parameter(opcode, [params])
def parse_parameter_instruction(numbers, cursor):
    # Parse instruction: digits-opcode
    instruction = str(numbers[cursor])
    opcode = int(instruction[len(instruction) - 1])
    digits = str(instruction[0:len(instruction) - 2])
    # Digits processed right -> left
    digits = list(digits[::-1])

    required_param = get_required_parameters(opcode)

    # Complete digits with default value (0)
    for k in range(len(digits), required_param):
        digits.append('0')

    # For those instructions, the last param is the address
    if opcode == 1 or opcode == 2 or opcode == 3 or opcode == 7 or opcode == 8:
        digits[-1] = 1

    params = []
    for k in range(required_param):
        # Position mode
        if digits[k] == '0':
            address = get_value(numbers, cursor + k + 1)
            params.append(get_value(numbers, address))
        # Immediate mode
        else:
            params.append(get_value(numbers, cursor + k + 1))
    return (opcode, params)


# Process and execute the current instruction
def process_instruction(cursor, numbers, param=0):
    inputs = parse_parameter_instruction(numbers, cursor)
    opcode = inputs[0]
    params = inputs[1]
    if opcode == 1:
        instruction1(numbers, params)
    elif opcode == 2:
        instruction2(numbers, params)
    elif opcode == 3:
        instruction3(numbers, params, param)
    elif opcode == 4:
        instruction4(params)
    elif opcode == 5:
        cursor = instruction5(cursor, params)
    elif opcode == 6:
        cursor = instruction6(cursor, params)
    elif opcode == 7:
        instruction7(numbers, params)
    elif opcode == 8:
        instruction8(numbers, params)
    elif opcode == 9 or opcode == 99:
        intruction99()
    else:
        print("Error while parsing cursor at: " + str(cursor) + ", value = " + str(numbers[cursor]))
        raise NotImplementedError
    return (opcode, cursor)


# Addition
def instruction1(numbers, params):
    value = params[0] + params[1]
    set_value(numbers, params[2], value)


# Multiplication
def instruction2(numbers, params):
    value = params[0] * params[1]
    set_value(numbers, params[2], value)


# Set param value at address
def instruction3(numbers, params, param):
    set_value(numbers, params[0], param)


# Output next value
def instruction4(params):
    print(params[0])


# Jump-if-true
def instruction5(cursor, params):
    if params[0] != 0:
        return params[1]
    else:
        return cursor


# Jump-if-false
def instruction6(cursor, params):
    if params[0] == 0:
        return params[1]
    else:
        return cursor


# Less than
def instruction7(numbers, params):
    if params[0] < params[1]:
        value = 1
    else:
        value = 0
    set_value(numbers, params[2], value)


# Equals
def instruction8(numbers, params):
    if params[0] == params[1]:
        value = 1
    else:
        value = 0
    set_value(numbers, params[2], value)


# Stop instruction
def intruction99():
    return None


def get_required_parameters(opcode):
    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        return 3
    elif opcode == 5 or opcode == 6:
        return 2
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
    numbers = data.copy()
    cursor = 0
    opcode = numbers[0]
    param = input
    while opcode != 99 and opcode != 9 and cursor < len(numbers):
        res = process_instruction(cursor, numbers, param)
        opcode = res[0]
        # If jump encountered
        if cursor != res[1]:
            cursor = res[1]
        # Else: cursor += parameters used
        else:
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
                print("****** Found matching: verb=" + str(noun) + " ,noun=" + str(verb) + "-> " + str(solution))
                return solution


if __name__ == '__main__':
    data = read_file("inputs/day5.input")
    run_simulation(data, 1)
