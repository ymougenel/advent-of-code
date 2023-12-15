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

    # Sort the lists values (based on src)
    seed_to_soil.sort(key=lambda x: x[1])
    soil_to_fertilizer.sort(key=lambda x: x[1])
    fertilizer_to_water.sort(key=lambda x: x[1])
    water_to_light.sort(key=lambda x: x[1])
    light_to_temperature.sort(key=lambda x: x[1])
    temperature_to_humidity.sort(key=lambda x: x[1])
    humidity_to_location.sort(key=lambda x: x[1])


def get_location(seed):
    # Retrieve the value for each list, among with the skipping value
    val, skipping1 = get_value(seed_to_soil, seed)
    val, skipping2 = get_value(soil_to_fertilizer, val)
    val, skipping3 = get_value(fertilizer_to_water, val)
    val, skipping4 = get_value(water_to_light, val)
    val, skipping5 = get_value(light_to_temperature, val)
    val, skipping6 = get_value(temperature_to_humidity, val)
    val, skipping7 = get_value(humidity_to_location, val)
    return val, min(skipping1, skipping2, skipping3, skipping4, skipping5, skipping6, skipping7)


def get_value(lst, key):
    closest = 1
    for dest, src, rg in lst:
        if src <= key < src + rg:
            return dest + key - src, src + rg - key
        if key < src:
            closest = src
    return key, closest


def solve_part1():
    return min([get_location(seed) for seed in seeds])


def solve_part2():
    i = 0
    minimum = math.inf
    while i < len(seeds):
        begin = seeds[i]
        length = seeds[i + 1]
        seed = begin
        while seed < begin + length:
            mini, skipping = get_location(seed)
            minimum = min(minimum, mini)
            seed += skipping
        i += 2
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
    print("Part 2: " + str(solve_part2()))
