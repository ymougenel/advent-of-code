#!/usr/bin/env python3
import time
from numpy import arctan
from numpy import pi
import operator

#############################################################################################
# From advent of code puzzle: https://adventofcode.com/2019/day/10
### 1. Get all the asteroid positions
### 2. Find the base location (ie: the one with the higher visibility)
### 3. Calculate radial coordinates for all asteroids: (x_position, y_position, angle, distance from origin)
### 4. Sort coordinates from angle (then distance)
### 5. Destroy asteroids with rotating laser

##############################################################################################


start_time = time.time()
inputFile = open("inputs/input.txt", "r")
# inputFile = open("inputs/example3.txt", "r")
data = inputFile.read().splitlines()
row = len(data)
col = len(data[0])


# Init matrix
def initMatrix(row, col, value=-1):
    M = []
    for i in range(row):
        M.append([value] * col)
    return M


# Print matrix
def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()


# Get Asteroid positions from board
def getAsteroidPositions():
    positions = []
    for i in range(row):
        for j in range(col):
            board[i][j] = data[i][j]
            if data[i][j] == '#' or data[i][j] == '+':
                positions.append((i, j))
    return positions


# Calculate all vectors from positions to origin
def calculateVectors(origin, positions):
    vectors = []
    for position in positions:
        dx = position[0] - origin[0]
        dy = position[1] - origin[1]
        if (dx != 0 or dy != 0):
            vectors.append((dx, dy))
    return vectors


# Calculate the number of asteroid visible from vector origin
def calculateVisiblePositions(vectors):
    totalVisible = 0
    for v in vectors:
        isHidden = False
        for w in vectors:
            if v != w and colludes(v, w):  # V and W aligned
                # W vector is closer -> V is hidden
                if getAbsoluteMax(v[0], w[0]) == v[0] and getAbsoluteMax(v[1], w[1]) == v[1]:
                    isHidden = True
                    break
        if not isHidden:
            totalVisible += 1
    return totalVisible


# Check if 1D vectors are in the same direction
def sameDirection(i, j):
    if i == 0 and j == 0:
        return True
    elif i == 0 or j == 0:
        return False
    else:
        return i / j > 0  # same direction


# Return biggest ratio between two numbers
def getRatio(i, j):
    if abs(i) > abs(j):
        return i / j
    else:
        return j / i


def getAbsoluteMax(i, j):
    if i < 0 and j < 0:
        return min(i, j)
    else:
        return max(i, j)


# Two vectors colludes if they have the same direction and are collinear
def colludes(v1, v2):
    x1 = v1[0]
    x2 = v2[0]
    y1 = v1[1]
    y2 = v2[1]
    if sameDirection(x1, x2) and sameDirection(y1, y2):  # Both vectors in same directions
        if (x1 == 0 and x2 == 0) or (y1 == 0 and y2 == 0):
            return True
        else:
            return x1 / x2 == y1 / y2  # Vectors collinear V1=aV2 => collusion
    else:
        return False


# Find ASteroid location with maximum visibility
def findLocation(positions):
    maxVisible = 0
    finalPosition = []
    for position in positions:
        vectors = calculateVectors(position, positions)
        visible = calculateVisiblePositions(vectors)
        if visible >= maxVisible:
            finalPosition = position
            maxVisible = visible
    print("Found position: " + str(finalPosition) + " with " + str(maxVisible) + " visible asteroids")
    return finalPosition


def calculateAngleBonus(v):
    if v[0] >= 0 and v[1] > 0:
        return 0
    elif v[0] > 0 and v[1] <= 0:
        return pi / 2
    elif v[0] <= 0 and v[1] < 0:
        return pi
    elif v[0] < 0 and v[1] >= 0:
        return 3 * pi / 2


# Get coordinates for each asteroid
# Return a tuple containing:
# * The asteroid x position
# * The asteroid y position
# * The angle (clockwise)
# * The square distance between origin and asteroid
def calculateRadialCoordinates(origin, positions):
    coordonate = []
    for position in positions:
        v = (position[1] - origin[1], origin[0] - position[0])
        angleBonus = calculateAngleBonus(v)
        if v[1] == 0 or v[0] == 0:
            coordonate.append((position[0], position[1], angleBonus, v[0] ** 2 + v[1] ** 2))
        else:
            if v[0] / v[1] > 0:
                coordonate.append(
                    (position[0], position[1], angleBonus + arctan(abs(v[0]) / abs(v[1])), v[0] ** 2 + v[1] ** 2))

            else:
                coordonate.append(
                    (position[0], position[1], angleBonus + arctan(abs(v[1]) / abs(v[0])), v[0] ** 2 + v[1] ** 2))
    return coordonate


# Pick next position to destroy (from angle)
def pickNext(currentPosition, currentAngle, coordonates):
    position = currentPosition
    while position < len(coordonates):
        # Skip all asteroid with same angle
        if (coordonates[position][2] <= currentAngle):
            position += 1
        else:
            return position
    # Full rotation
    return 0


# Pick from coordinates and destroy
def destroyAsteroids(total, board, coordinates):
    position = 0
    destroyed = 0
    while destroyed < total:
        # Destroy current target
        target = coordinates[position]
        coordinates.remove(target)
        destroyed += 1
        print("The " + str(destroyed) + "th asteroid to be vaporized is at  " + str(target[1]) + ", " + str(target[0]))
        board[target[0]][target[1]] = destroyed
        position = pickNext(position, target[2], coordinates)
    return target


board = initMatrix(row, col)

#############################################################################################
### 1. Get all the asteroid positions
positions = getAsteroidPositions()
### 2. Find the base location (ie: the one with the higher visibility)
finalPosition = findLocation(positions)
positions.remove(finalPosition)
print(board[finalPosition[0]][finalPosition[1]])

### 3. Calculate radial coordinates for all asteroids: (x_position, y_position, angle, distance from origin)
res = calculateRadialCoordinates(finalPosition, positions)
### 4. Sort coordinates from angle (then distance)
coordinates = sorted(res, key=operator.itemgetter(2, 3))
# print(coordinates)
### 5. Destroy asteroids with rotating laser
destroyAsteroids(200, board, coordinates)

##############################################################################################

print("--- %s seconds ---" % (time.time() - start_time))
