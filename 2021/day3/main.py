
def read_file(file_name):
    with open(file_name) as input_file:
      return [line for line in input_file.read().splitlines()]
import math

def get_most_least_commun_bits(table, position):
    count_0 = 0
    count_1 = 0
    for n in table:
        if n[position] == "1":
            count_1 += 1
        if n[position] == "0":
            count_0 += 1
    if count_0 > count_1:
        return (0,1)
    else:
        return (1,0)

def get_life_support(table):
    possibilities = table
    i=0
    while len(possibilities) >1:
        most = str(get_most_least_commun_bits(possibilities, i)[0])
        possibilities = [ line for line in possibilities if line[i] == most]
        i = i+1
    oxygen_rating = convert_binary_to_digit(possibilities[0])

    possibilities = table
    i=0
    while len(possibilities) >1:
        least = str(get_most_least_commun_bits(possibilities, i)[1])
        possibilities = [ line for line in possibilities if line[i] == least]
        i = i+1
    co2_rating = convert_binary_to_digit(possibilities[0])
    return oxygen_rating * co2_rating

def convert_binary_to_digit(binary_str):
    size = len(binary_str)
    return sum([int(binary_str[size-1-i]) * math.pow(2,i) for i in range(size)])

def get_power_consumption(table):
    gamma = ""
    epsilon = ""
    for i in range(len(table[0])):
        gamma += str(get_most_least_commun_bits(table, i)[0])
        epsilon += str(get_most_least_commun_bits(table, i)[1])
    return convert_binary_to_digit(gamma) * convert_binary_to_digit(epsilon)


if __name__ == '__main__':
    # Part 1
    diagnostic  = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

    #diagnostic = read_file("inputs/input1.txt")
    #print(get_power_consumption(diagnostic))

    # Part 2
    #diagnostic  = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

    diagnostic = read_file("inputs/input1.txt")
    print(get_life_support(diagnostic))
