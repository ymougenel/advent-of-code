#!/usr/bin/env python3


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def prepare_paper(dots):
    range_x = max([el[0] for el in dots])
    range_y = max([el[1] for el in dots])
    paper = [["." for j in range(range_x + 1)] for i in range(range_y + 1)]
    for dot in dots:
        paper[dot[1]][dot[0]] = "#"
    return paper


def draw(paper):
    for line in paper:
        l = ""
        for c in line:
            l += c
        print(l)


def fold_paper(paper, folding):
    if folding[0] == "y":
        y = folding[1]
        for i in range(1, len(paper) - y):
            for j in range(0, len(paper[0])):
                if paper[y + i][j] == "#":
                    paper[y - i][j] = "#"
        return paper[0:y]
    if folding[0] == "x":
        x = folding[1]
        for j in range(1, len(paper[0]) - x):
            for i in range(0, len(paper)):
                if paper[i][j + x] == "#":
                    paper[i][x - j] = "#"
        return [line[0:x] for line in paper]


def count_dots(paper):
    count = 0
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            if paper[i][j] == "#":
                count += 1
    print(count)


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/part1.example")
    data = read_file("inputs/part1.input")
    dots = []
    foldings = []
    part = 1
    for line in data:
        if line == "":
            part = 2
        elif part == 1:
            x = int(line.split(',')[0])
            y = int(line.split(',')[1])
            dots.append([x, y])
        else:
            segment = line.split('=')[0][-1]
            value = int(line.split('=')[1])
            foldings.append([segment, value])
    print(dots)
    print(foldings)
    paper = prepare_paper(dots)

    for fold in foldings:
        paper = fold_paper(paper, fold)
    draw(paper)
    print(count_dots(paper))
