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
    if cursor >= len(numbers):
        extend_memory(numbers, cursor)
    return numbers[cursor]


def set_value(numbers, address, value):
    if address >= len(numbers):
        extend_memory(numbers, address)
    numbers[address] = value


# If address outside current memory, extend with zeros(from rule day9)
def extend_memory(numbers, final_size):
    zeros = [0] * (1 + final_size - len(numbers))
    numbers += zeros


# Return the opcode and the instruction parameter(opcode, [params])
def parse_parameter_instruction(numbers, cursor, relative_base=0):
    # Parse instruction: digits-opcode
    instruction = str(numbers[cursor])
    opcode = int(instruction[len(instruction) - 2:])
    digits = str(instruction[0:len(instruction) - 2])
    # Digits processed right -> left
    digits = list(digits[::-1])

    required_param = get_required_parameters(opcode)

    # Complete digits with default value (0)
    for k in range(len(digits), required_param):
        digits.append('0')

    # For those instructions, the last param is the address
    if is_setting_value_instruction(opcode) and digits[-1] == '0':
        digits[-1] = '1'

    params = []
    for k in range(required_param):
        # Position mode
        if digits[k] == '0':
            address = get_value(numbers, cursor + k + 1)
            params.append(get_value(numbers, address))
        # Immediate mode
        elif digits[k] == '1':
            params.append(get_value(numbers, cursor + k + 1))
        # Relative base
        else:
            # For instructions setting values, the last parameter is is address
            if k == required_param - 1 and is_setting_value_instruction(opcode):
                params.append(get_value(numbers, cursor + k + 1) + relative_base)
            else:
                address = get_value(numbers, cursor + k + 1)
                params.append(get_value(numbers, address + relative_base))
    return (opcode, params)


def is_setting_value_instruction(opcode):
    return opcode == 1 or opcode == 2 or opcode == 3 or opcode == 7 or opcode == 8


# Process and execute the current instruction
def process_instruction(cursor, numbers,outputs, param=0, relative_base=0 ):
    inputs = parse_parameter_instruction(numbers, cursor, relative_base)
    opcode = inputs[0]
    params = inputs[1]
    if opcode == 1:
        instruction1(numbers, params)
    elif opcode == 2:
        instruction2(numbers, params)
    elif opcode == 3:
        instruction3(numbers, params, param)
    elif opcode == 4:
        instruction4(params, outputs)
    elif opcode == 5:
        cursor = instruction5(cursor, params)
    elif opcode == 6:
        cursor = instruction6(cursor, params)
    elif opcode == 7:
        instruction7(numbers, params)
    elif opcode == 8:
        instruction8(numbers, params)
    elif opcode == 9:
        relative_base = instruction9(params, relative_base)
    elif opcode == 99:
        intruction99()
    else:
        print("Error while parsing cursor at: " + str(cursor) + ", value = " + str(numbers[cursor]))
        raise NotImplementedError
    return (opcode, cursor, relative_base)


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
def instruction4(params, outputs):
    outputs.append(params[0])


# Jump-if-true
def instruction5(cursor, params):
    if params[0] != 0:
        return params[1]
    else:
        return cursor


def output(element):
    print(element)


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


# Update relative_base
def instruction9(params, relative_base):
    return relative_base + params[0]


# Stop instruction
def intruction99():
    return None


def get_required_parameters(opcode):
    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        return 3
    elif opcode == 5 or opcode == 6:
        return 2
    elif opcode == 3 or opcode == 4 or opcode == 9:
        return 1
    else:
        return 0


def update_cursor(cursor, currentInstruction):
    if currentInstruction == 99:
        return cursor
    else:
        return cursor + 1 + get_required_parameters(int(currentInstruction))


if __name__ == '__main__':
    # data = read_file("inputs/day5.input")
    # data = read_file("inputs/day9_quine.input")
    data = read_file("inputs/day11.input")