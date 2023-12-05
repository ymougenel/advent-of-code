#!/usr/bin/env python3
import math
import time

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines() if line != ""]


def parse_almanac(data):
    global seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location
    current = None
    for line in data:
        if line.startswith("seeds:"):
            seeds = list(map(int, line.split(":")[1].split()))
        elif line.startswith("seed-to-soil"):
            current = seed_to_soil
        elif line.startswith("soil-to-fertilizer"):
            current = soil_to_fertilizer
        elif line.startswith("fertilizer-to-water"):
            current = fertilizer_to_water
        elif line.startswith("water-to-light"):
            current = water_to_light
        elif line.startswith("light-to-temperature"):
            current = light_to_temperature
        elif line.startswith("temperature-to-humidity"):
            current = temperature_to_humidity
        elif line.startswith("humidity-to-location"):
            current = humidity_to_location
        else:
            dest, src, rg = list(map(int, line.split()))
            current.append((dest, src, rg))


def get_location(seed):
    val = get_value(seed_to_soil, seed)
    val = get_value(soil_to_fertilizer, val)
    val = get_value(fertilizer_to_water, val)
    val = get_value(water_to_light, val)
    val = get_value(light_to_temperature, val)
    val = get_value(temperature_to_humidity, val)
    val = get_value(humidity_to_location, val)
    return val


def get_value(lst, key):
    for dest, src, rg in lst:
        if src <= key < src + rg:
            return dest + key - src
    return key


def solve_part1():
    return min([get_location(seed) for seed in seeds])


def solve_part2():
    i = 0
    minimum = math.inf
    while i < len(seeds):
        begin = seeds[i]
        length = seeds[i+1]
        for seed in range(begin,begin+length):
            minimum = min(minimum, get_location(seed))
        i += 2
        print(i)
    return minimum


if __name__ == '__main__':
    start_time = time.time()
    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    parse_almanac(data)
    print("Part 1: " + str(solve_part1()))
    print("Solved in : ", (time.time() - start_time))

    # Part 2
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/input.txt")
    print("Part 2: " + str(solve_part2()))
