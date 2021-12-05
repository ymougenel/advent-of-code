#!/usr/bin/env python3
boards = []
number_picked = []
SIZE = 5
def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def parse_bingo(data):
    global number_picked,boards
    number_picked =  [int(val) for val in data[0].split(",")]

    boards = []
    board = []
    for i in range(2, len(data)):
        if len(board) == 5:
            boards.append(board)
            board = []
        else:
            board.append([(int(val),False) for val in data[i].split(" ") if val != ""])
    boards.append(board)
def is_winning_board(board):
    global SIZE
    for i in range(SIZE):
        count_line = 0
        count_col = 0
        for j in range(SIZE):
            if board[i][j][1]:
                count_line += 1
            if board[j][i][1]:
                count_col += 1
        if max(count_col,count_line) == SIZE:
            return True
    return False

def pick_number(board, number):
    global SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j][0] == number:
                board[i][j] = (board[i][j][0], True)

def get_winners():
    global number_picked, boards
    i = 0
    while(i < len(number_picked)):
        number = number_picked[i]
        for board in boards:
            pick_number(board, number)
        winning = [val for val in boards if is_winning_board(val)]
        if len(winning) > 0:
            return (winning[0],number)
        i += 1

def get_loser():
    global number_picked, boards
    i = 0
    while(i < len(number_picked)):
        number = number_picked[i]
        for board in boards:
            pick_number(board, number)
        if len(boards) != 1:
            boards = [val for val in boards if not is_winning_board(val)]
        else:
            if is_winning_board(boards[0]):
                return (boards[0], number)
        i += 1


def get_score(winning_board, number):
    score = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if not winning_board[i][j][1]:
                score += winning_board[i][j][0]
    return number * score
if __name__ == '__main__':
    # Part 1
#     data = read_file("inputs/part1.example")
#     data = read_file("inputs/part1.input")
#     parse_bingo(data)
#     print(number_picked)
#     print(boards)
#     print("-----")
#     winners = get_winners()
#     print(get_score(*winners))

    # Part 2
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    parse_bingo(data)
    loser = get_loser()
    print(loser)
    print(get_score(*loser))
    #data = read_file("inputs/part1.input")
    #print(data)
