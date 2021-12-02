position_x = 0
position_z = 0
aim = 0
def read_file(file_name):
    with open(file_name) as input_file:
      return [line for line in input_file.read().splitlines()]

def update_position(line):
    global position_x, position_z
    command = line.split(" ")[0]
    value = int(line.split(" ")[1])
    if command == "forward":
        position_x += value
    elif command == "down":
        position_z += value
    elif command == "up":
        position_z -= value

def update_position2(line):
    global position_x, position_z, aim
    command = line.split(" ")[0]
    value = int(line.split(" ")[1])
    if command == "forward":
        position_x += value
        position_z += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value
def read_instructions(instructions):
    for line in instructions:
        update_position2(line)
if __name__ == '__main__':
    # Part 1
    #data = read_file("inputs/part1.example.txt")
    #data = read_file("inputs/input1.txt")
    #read_instructions(data)
    #print(position_x * position_z)

    # Part 2
    #data = read_file("inputs/part1.example.txt")
    data = read_file("inputs/input1.txt")
    read_instructions(data)
    print(position_x * position_z)
