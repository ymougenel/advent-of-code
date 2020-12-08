#!/usr/bin/env python3
from STATUS import STATUS
from COMMAND import COMMAND


class GameConsole:

    def __init__(self):
        self.cursor = 0
        self.acc = 0
        self.processed = []
        self.instructions = []
        self.state = STATUS.IDLE

    # Read file_name as input, and return the program inside
    # Ex: Input File
    #       nop +0
    #       acc +1
    #     Output program
    #       [ (NOP, 0), (ACC, 1) ]
    def read_file(self, file_name):
        with open(file_name) as input_file:
            return [self.parse_instruction(line) for line in input_file.read().splitlines()]
    # Load program, reset atributes & run it
    def init_and_run(self, program):
        self.cursor = 0
        self.acc = 0
        self.instructions = program
        self.processed = [0] * len(self.instructions)
        self.state = STATUS.READY

        return self.run_program()

    # Parse en instruction -> cmd, value
    #  ex: (acc, +5)
    def parse_instruction(self, line):
        return COMMAND(line.split(" ")[0]), int(line.split(" ")[1])

    def __process_program__(self):
        if self.cursor >= len(self.instructions):
            self.state = STATUS.TERMINATED_OK
            return True
        if self.processed[self.cursor] == 1:
            self.state = STATUS.INFINITE_LOOP
            return False

        self.processed[self.cursor] = 1
        command = self.instructions[self.cursor][0]
        value = self.instructions[self.cursor][1]
        if command == COMMAND.NOP:
            self.cursor += 1
        elif command == COMMAND.ACC:
            self.acc += value
            self.cursor += 1
        elif command == COMMAND.JMP:
            self.cursor += value
        return True

    def run_program(self):
        self.state = STATUS.RUNNING
        while self.state == STATUS.RUNNING:
            self.__process_program__()
        return self.acc


def generateAlternatives(alternative_programs, command, value, current_switch):
    alternative_command = ""
    if command == COMMAND.NOP:
        alternative_command = COMMAND.JMP
    elif command == COMMAND.JMP:
        alternative_command = COMMAND.NOP

    for i in range(0, len(alternative_programs)):
        if i != current_switch or not alternative_command:
            alternative_programs[i].append((command, value))
        else:
            alternative_programs[i].append((alternative_command, value))

    return current_switch + 1 if alternative_command else current_switch

# Part1:2058
# Part2:1000
if __name__ == '__main__':
    day8 = GameConsole()
    # program = day8.read_file("inputs/part2.example")
    program = day8.read_file("inputs/part1.input")
    day8.init_and_run(program)
    acc = day8.run_program()
    print("Part1:" + str(acc))

    # Find corrupted instruction (nop -> jmp or jmp -> nop)
    alternative_count = len(list(filter(lambda inst: inst[0] == COMMAND.NOP or inst[0] == COMMAND.JMP, program)))
    alternative_programs = [[] for k in range(alternative_count)]
    current_switch = 0
    for command, value in program:
        current_switch = generateAlternatives(alternative_programs, command, value, current_switch)

    for alt_prog in alternative_programs:
        day8.init_and_run(alt_prog)
        if day8.state == STATUS.TERMINATED_OK:
            print("Part2:" + str(day8.acc))
            break
