#!/usr/bin/env python3

class IntCode:

    def __init__(self, input=0, relative_base=0):
        self.cursor = 0
        self.opcode = 0
        self.relative_base = relative_base
        self.input = input
        self.outputs = []

    def init_numbers_from_file(self, file_path: str):
        inputFile = open(file_path, "r")
        data = inputFile.read()
        inputFile.close()
        self.numbers = list(map(int, data.split(',')))

    def init_numbers_from_data(self, data: list):
        self.numbers = data

    # Set alarm (from day2)
    def restore_alarm(self, noun, verb):
        self.numbers[1] = noun
        self.numbers[2] = verb

    def __get_value(self, address):
        if address >= len(self.numbers):
            self.__extend_memory(address)
        return self.numbers[address]

    def __set_value(self, address, value):
        if address >= len(self.numbers):
            self.__extend_memory(address)
        self.numbers[address] = value

    # If address outside current memory, extend with zeros(from rule day9)
    def __extend_memory(self, final_size):
        zeros = [0] * (1 + final_size - len(self.numbers))
        self.numbers += zeros

    # Return the opcode and the instruction parameter(opcode, [params])
    def __parse_parameter_instruction(self):
        # Parse instruction: digits-opcode
        instruction = str(self.numbers[self.cursor])
        self.opcode = int(instruction[len(instruction) - 2:])
        digits = str(instruction[0:len(instruction) - 2])
        # Digits processed right -> left
        digits = list(digits[::-1])

        required_param = self.__get_required_parameters()

        # Complete digits with default value (0)
        for k in range(len(digits), required_param):
            digits.append('0')

        # For those instructions, the last param is the address
        if self.__is_setting_value_instruction() and digits[-1] == '0':
            digits[-1] = '1'

        params = []
        for k in range(required_param):
            # Position mode
            if digits[k] == '0':
                address = self.__get_value(self.cursor + k + 1)
                params.append(self.__get_value(address))
            # Immediate mode
            elif digits[k] == '1':
                params.append(self.__get_value(self.cursor + k + 1))
            # Relative base
            else:
                # For instructions setting values, the last parameter is is address
                if k == required_param - 1 and self.__is_setting_value_instruction():
                    params.append(self.__get_value(self.cursor + k + 1) + self.relative_base)
                else:
                    address = self.__get_value(self.cursor + k + 1)
                    params.append(self.__get_value(address + self.relative_base))
        return params

    def __is_setting_value_instruction(self):
        return self.opcode == 1 or self.opcode == 2 or self.opcode == 3 or self.opcode == 5 or self.opcode == 6 or self.opcode == 7 or self.opcode == 8

    # Process and execute the current instruction
    def process_instruction(self):
        params = self.__parse_parameter_instruction()
        if self.opcode == 1:
            self.__instruction1(params)
        elif self.opcode == 2:
            self.__instruction2(params)
        elif self.opcode == 3:
            self.__instruction3(params)
        elif self.opcode == 4:
            self.__instruction4(params)
        elif self.opcode == 5:
            self.__instruction5(params)
        elif self.opcode == 6:
            self.__instruction6(params)
        elif self.opcode == 7:
            self.__instruction7(params)
        elif self.opcode == 8:
            self.__instruction8(params)
        elif self.opcode == 9:
            self.__instruction9(params)
        elif self.opcode == 99:
            self.__intruction99()
        else:
            print("Error while parsing self.cursor at: " + str(self.cursor) + ", value = " + str(
                self.numbers[self.cursor]))
            raise NotImplementedError
        return self.opcode

    # Addition
    def __instruction1(self, params):
        value = params[0] + params[1]
        self.__set_value(params[2], value)

    # Multiplication
    def __instruction2(self, params):
        value = params[0] * params[1]
        self.__set_value(params[2], value)

    # Set param value at address
    def __instruction3(self, params):
        self.__set_value(params[0], self.input)

    # Output next value
    def __instruction4(self, params):
        self.outputs.append(params[0])

    # Jump-if-true
    def __instruction5(self, params):
        if params[0] != 0:
            self.cursor = params[1]

    # Jump-if-false
    def __instruction6(self, params):
        if params[0] == 0:
            self.cursor = params[1]

    # Less than
    def __instruction7(self, params):
        if params[0] < params[1]:
            value = 1
        else:
            value = 0
        self.__set_value(params[2], value)

    # Equals
    def __instruction8(self, params):
        if params[0] == params[1]:
            value = 1
        else:
            value = 0
        self.__set_value(params[2], value)

    # Update relative_base
    def __instruction9(self, params):
        self.relative_base = self.relative_base + params[0]

    # Stop instruction
    def __intruction99(self):
        pass

    def __get_required_parameters(self):
        if self.opcode == 1 or self.opcode == 2 or self.opcode == 7 or self.opcode == 8:
            return 3
        elif self.opcode == 5 or self.opcode == 6:
            return 2
        elif self.opcode == 3 or self.opcode == 4 or self.opcode == 9:
            return 1
        else:
            return 0

    def update_cursor(self):
        if self.opcode != 99:
            self.cursor = self.cursor + 1 + self.__get_required_parameters()

    def __run_instrution_and_update(self):
        current_cursor = self.cursor
        self.process_instruction()
        # If no jump encountered: self.cursor += parameters used
        if self.cursor == current_cursor:
            self.update_cursor()

    def run_simulation(self, input=0):
        while self.opcode != 99 and self.cursor < len(self.numbers):
            self.__run_instrution_and_update()
        return self.outputs

    def next_output(self):
        old_outputs_length = len(self.outputs)
        # Run instructions until output
        while self.opcode != 99 and old_outputs_length == self.outputs:
            self.__run_instrution_and_update()
        # Return last generated output
        return self.outputs[-1]

    # Found input alarm that produces an specific result (day2)
    def found_matching_noun_verb(self):
        initial_data = self.numbers.copy()
        for noun in range(len(initial_data)):
            for verb in range(len(initial_data)):
                try:
                    self.numbers = initial_data.copy()
                    self.cursor = 0
                    self.restore_alarm(noun, verb)
                    self.run_simulation()
                except IndexError:
                    pass
                if self.numbers[0] == 19690720:
                    solution = noun * 100 + verb
                    print("****** Found matching: verb=" + str(noun) + " ,noun=" + str(verb) + "-> " + str(solution))
                    return solution


if __name__ == '__main__':
    intcode = IntCode()
    intcode.init_numbers_from_file("inputs/day5_example2.input")
    intcode.input = 8
    intcode.run_simulation()
    print(intcode.outputs)
