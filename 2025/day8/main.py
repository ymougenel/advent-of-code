#!/usr/bin/env python3
import time
import re
import math


def read_file(file_name):
    with open(file_name) as input_file:
        return [parse_line(line) for line in input_file.read().splitlines()]


def parse_line(line):
    return [int(elt) for elt in re.compile(r'\d+').findall(line)]


def solve_part1(boxes, limit):
    all_distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            all_distances.append((boxes[i], boxes[j], get_distance(boxes[i], boxes[j])))
    all_distances = sorted(all_distances, key=lambda elt: elt[2])

    all_circuits = []
    all_processed = []
    connection_made = 0
    while all_distances and connection_made < limit:

        box1, box2, dist = all_distances.pop(0)

        box1_in_circuit = box1 in all_processed
        box2_in_circuit = box2 in all_processed

        if not box1_in_circuit or not box2_in_circuit:

            # If Box1 already in circuit
            if box1_in_circuit:
                box1_circuits = [circuit for circuit in all_circuits if box1 in circuit]
                if len(box1_circuits) > 1:
                    print("Error size")
                box1_circuits[0].append(box2)
                all_processed.append(box2)
                connection_made += 1

            # If Box1 already in circuit
            elif box2_in_circuit:
                box2_circuits = [circuit for circuit in all_circuits if box2 in circuit]
                if len(box2_circuits) > 1:
                    print("Error size")
                box2_circuits[0].append(box1)
                all_processed.append(box1)
                connection_made += 1

            # Otherwise create circuit from box1 and box2
            else:
                all_circuits.append([box1, box2])
                all_processed.append(box1)
                all_processed.append(box2)
                connection_made += 1
        else:
            box1_circuit = [circuit for circuit in all_circuits if box1 in circuit][0]
            box2_circuit = [circuit for circuit in all_circuits if box2 in circuit][0]
            if box1_circuit != box2_circuit:
                all_circuits.remove(box2_circuit)
                box1_circuit += box2_circuit
            connection_made += 1

    all_circuits = sorted(all_circuits, key=lambda elt:len(elt), reverse=True)
    print([len(c) for c in all_circuits])
    return len(all_circuits[0]) * len(all_circuits[1]) * len(all_circuits[2])


def find_shortest_remaining_boxes(remaining_boxes, all_boxes):
    min_dist = math.inf
    min_boxes = (None, None)
    for remaining_boxe in remaining_boxes:
        for boxe in all_boxes:
            dist = get_distance(remaining_boxe, boxe)
            if 0 < dist < min_dist:
                min_dist = dist
                min_boxes = (remaining_boxe, boxe)
    return min_boxes


def get_distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]))

def solve_part2(boxes):
    all_distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            all_distances.append((boxes[i], boxes[j], get_distance(boxes[i], boxes[j])))
    all_distances = sorted(all_distances, key=lambda elt: elt[2])

    all_circuits = []
    all_processed = []
    connection_made = 0
    while len(all_circuits) != 1 or len(all_circuits[0]) != len(boxes):

        box1, box2, dist = all_distances.pop(0)

        box1_in_circuit = box1 in all_processed
        box2_in_circuit = box2 in all_processed

        if not box1_in_circuit or not box2_in_circuit:

            # If Box1 already in circuit
            if box1_in_circuit:
                box1_circuits = [circuit for circuit in all_circuits if box1 in circuit]
                if len(box1_circuits) > 1:
                    print("Error size")
                box1_circuits[0].append(box2)
                all_processed.append(box2)
                connection_made += 1

            # If Box1 already in circuit
            elif box2_in_circuit:
                box2_circuits = [circuit for circuit in all_circuits if box2 in circuit]
                if len(box2_circuits) > 1:
                    print("Error size")
                box2_circuits[0].append(box1)
                all_processed.append(box1)
                connection_made += 1

            # Otherwise create circuit from box1 and box2
            else:
                all_circuits.append([box1, box2])
                all_processed.append(box1)
                all_processed.append(box2)
                connection_made += 1
        else:
            box1_circuit = [circuit for circuit in all_circuits if box1 in circuit][0]
            box2_circuit = [circuit for circuit in all_circuits if box2 in circuit][0]
            if box1_circuit != box2_circuit:
                all_circuits.remove(box2_circuit)
                box1_circuit += box2_circuit
            connection_made += 1
    print("Done" + str(box1)+ str(box2))
    all_circuits = sorted(all_circuits, key=lambda elt:len(elt), reverse=True)
    print([len(c) for c in all_circuits])
    return box1[0] * box2[0]


if __name__ == '__main__':
    # Parse input file
    data = read_file("inputs/example1.txt")
    limit = 10
    data = read_file("inputs/input.txt")
    limit = 1000

    # Part 1
    start_time = time.time()
    print("Part 1: " + str(solve_part1(data, limit)))
    print("-> Part1 solved in: ", (time.time() - start_time))

    # Part 2
    start_time = time.time()
    print("Part 2: " + str(solve_part2(data)))
    print("-> Part2 solved in: ", (time.time() - start_time))
