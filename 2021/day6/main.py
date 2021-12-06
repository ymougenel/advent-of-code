

def read_file(file_name):
    with open(file_name) as input_file:
      return [line for line in input_file.read().splitlines()]
import math


def next_day(lanternfish):
    news = [0] * 9
    for i in range(9):
        if i>0:
            news[i-1] += lanternfish[i]
        else:
            news[6] += lanternfish[0]
            news[8] += lanternfish[0]

    return news


if __name__ == '__main__':
    # Part 1
    content = ["3,4,3,1,2"]
    content = ["3,3,5,1,1,3,4,2,3,4,3,1,1,3,3,1,5,4,4,1,4,1,1,1,3,3,2,3,3,4,2,5,1,4,1,2,2,4,2,5,1,2,2,1,1,1,1,4,5,4,3,1,4,4,4,5,1,1,4,3,4,2,1,1,1,1,5,2,1,4,2,4,2,5,5,5,3,3,5,4,5,1,1,5,5,5,2,1,3,1,1,2,2,2,2,1,1,2,1,5,1,2,1,2,5,5,2,1,1,4,2,1,4,2,1,1,1,4,2,5,1,5,1,1,3,1,4,3,1,3,2,1,3,1,4,1,2,1,5,1,2,1,4,4,1,3,1,1,1,1,1,5,2,1,5,5,5,3,3,1,2,4,3,2,2,2,2,2,4,3,4,4,4,1,2,2,3,1,1,4,1,1,1,2,1,4,2,1,2,1,1,2,1,5,1,1,3,1,4,3,2,1,1,1,5,4,1,2,5,2,2,1,1,1,1,2,3,3,2,5,1,2,1,2,3,4,3,2,1,1,2,4,3,3,1,1,2,5,1,3,3,4,2,3,1,2,1,4,3,2,2,1,1,2,1,4,2,4,1,4,1,4,4,1,4,4,5,4,1,1,1,3,1,1,1,4,3,5,1,1,1,3,4,1,1,4,3,1,4,1,1,5,1,2,2,5,5,2,1,5"]
    lanternfish = []
    vals = [int(val) for val in content[0].split(",")]

    for i in range(9):
        lanternfish.append(vals.count(i))
    print(lanternfish)

    for i in range(256):
        lanternfish = next_day(lanternfish)

    print(sum(lanternfish))
