#!/usr/bin/env python3
import numpy as np
from Robot import Robot
from Direction import Direction
from intCode import *


def init_matrix(row, col):
    return np.zeros((row, col), dtype=int)


def run_simulation(numbers, panel, robot):
    cursor = 0
    opcode = numbers[0]
    param = panel[robot.x][robot.y]
    relative_base = 0
    outputs = []
    painted_areas = 0
    while opcode != 99 and cursor < len(numbers):
        # if len(outputs) == 1:
        #     param = 0
        if len(outputs) == 2:
            paint_user = paintAndMove(robot, panel, outputs)
            if paint_user:
                painted_areas += 1
            print("(" + str(outputs[0]) + ", " + str(outputs[1])+ ")")            # param = panel[robot.x][robot.y]
            param = panel[robot.x][robot.y]
            outputs = []

        res = process_instruction(cursor, numbers, outputs, param, relative_base)
        opcode = res[0]
        relative_base = res[2]
        # If jump encountered
        if cursor != res[1]:
            cursor = res[1]
        # Else: cursor += parameters used
        else:
            cursor = update_cursor(cursor, opcode)
    return painted_areas


def paintAndMove(robot, panel, inputs):
    paint_used = panel[robot.x][robot.y] == 0 and inputs[0] == 1

    robot.paint(panel, inputs[0])
    robot.move(Direction(inputs[1]))
    return paint_used


def count_color(panel):
    count = 0
    for i in range(len(panel)):
        for j in range(len(panel[0])):
            if panel[i][j] == 1:
                count += 1
    return count


if __name__ == '__main__':
    data = read_file("inputs/day11.input")
    SIZE = 20000
    panel = init_matrix(SIZE, SIZE)
    robot = Robot(SIZE // 2, SIZE // 2)
    print(run_simulation(data, panel, robot))
