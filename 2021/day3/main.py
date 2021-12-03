import math
diagnostic  = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

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

def convert_binary_to_digit(binary_str):
    size = len(binary_str)
    return sum([int(binary_str[size-1-i]) * math.pow(2,i) for i in range(size)])

def get_power_consumption(table):
    gamma = ""
    epsilon = ""
    for i in range(5):
        gamma += str(get_most_least_commun_bits(table, i)[0])
        epsilon += str(get_most_least_commun_bits(table, i)[1])
    return convert_binary_to_digit(gamma) * convert_binary_to_digit(epsilon)
    
print(get_power_consumption(diagnostic))
