#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        lines =  [line.split(" ") for line in input_file.read().splitlines()]
    return [ (line[0], int(line[1])) for line in lines]

def solve_part1(data):
    return len(execute_movements(data))

def solve_part2(data):
    return data

def execute_movements(movements):
    head = [4,0]
    tail = [4,0]
    visited = [[4,0]]

    for move in movements:
        if move[0] == "R":
            dir = (0, 1)
        elif move [0] == "L":
            dir = (0, -1)
        elif move[0] == "U":
            dir = (-1, 0)
        elif move[0] == "D":
            dir = (1, 0)
        else:
            print("Error direction")
        for i in range(move[1]):
            head = [head[0] + dir[0], head[1] + dir[1]]
            follow_tail(head, tail, move)
            if tail not in visited:
                visited.append(tail.copy())
            #print("Head", head)
            #print("Tail", tail)
            #print(visited)
    return visited
def follow_tail(head,tail, move):
    if abs(head[0] - tail[0]) + abs(head[1] - tail[1]) == 1:
        pass
    else:
        # Same row
        if head[0] == tail[0]:
            if head[1] > tail[1]:
                tail[1] += 1
            elif head[1] < tail[1]:
                tail[1] -= 1
        # Same col
        elif head[1] == tail[1]:
            if head[0] > tail[0]:
                tail[0] += 1
            elif head[0] < tail[0]:
                tail[0] -= 1
        # Diagonal
        else:
            if abs(head[0] - tail[0]) + abs(head[1] - tail[1]) == 2:
                pass
            else:
                if abs(head[0] - tail[0]) == 1:
                    tail[0] = head[0]
                if abs(head[1] - tail[1]) == 1:
                    tail[1] = head[1]
                if abs(head[0] - tail[0]) == 2:
                    if head[0] > tail[0]:
                        tail[0] += 1
                    else:
                        tail[0] -= 1
                if abs(head[1] - tail[1]) == 2:
                    if head[1] > tail[1]:
                        tail[1] += 1
                    else:
                        tail[1] -= 1

if __name__ == '__main__':
    # Part 1
    movements = read_file("inputs/part1.example")
    movements = read_file("inputs/part1.input")
    print("Part 1: " + str(solve_part1(movements)))

    # Part 2
    #print("Part 2: " + str(solve_part2(movements)))
