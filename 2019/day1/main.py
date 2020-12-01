#!/usr/bin/env python3
from functools import reduce

inputFile = open("inputs.txt", "r")
data = inputFile.read().splitlines()


# fuel required for a module
def calculateFuel(mass):
    return int(mass) // 3 - 2

# The fuel has a mass -> it requires fuel
def calculateTotalFuel(fuel):
    fuelMass = calculateFuel(fuel)
    if fuelMass <= 0:
        return 0
    else:
        return fuelMass + calculateTotalFuel(fuelMass)


# Part 1
fuelList = map(calculateFuel, data)
totalFuel = reduce(lambda x, y: x + y, fuelList)  # Add all fuelList values
print("Part 1: "+ str(totalFuel))

# Part 2
fuelList = map(calculateFuel, data)
fuelRequired = map(lambda x: x + calculateTotalFuel(x), fuelList) # For each module, calculate fuel for mass(module + fuel)
fuelRequired = reduce(lambda x, y: x + y, fuelRequired)  # Add all values
print("Part 2: "+ str(fuelRequired))
