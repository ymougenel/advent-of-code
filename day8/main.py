#!/usr/bin/env python3
from PIL import Image

# inputFile=open("inputTestColor.txt", "r")
# WIDE=2
# TALL=2
inputFile=open("input.txt", "r")
WIDE=25
TALL=6
encodedImage=inputFile.read()


# Next pixel index
def cursor(i,j,k):
    res = (k* WIDE * TALL) + i*WIDE + j
    return res

# Init matrix
def initMatrix(row, col, value = -1):
    M = []
    for i in range(row):
        M.append([value] * col)
    return M

# Count zeros from matrix values
def countZeros(M):
    count=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == '0':
                count+=1
    return count

# Print matrix
def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()

# Return layer with fewest zeros
def findFewestZero(layers):
    minZeroCount=countZeros(layers[0])
    minZeroLayer=layers[0]
    for k in range(1, len(layers)):
        currentLayer = layers[k]
        zerosNb = countZeros(currentLayer)
        if zerosNb < minZeroCount:
            minZeroCount = zerosNb
            minZeroLayer = currentLayer
    return minZeroLayer

# Test layers corruption (the number of 1 digits multiplied by the number of 2 digits)
def testLayerCorruption(layer):
    countOne=0;
    countTwo=0;
    for i in range(len(layer)):
        for j in range(len(layer[0])):
            if (layer[i][j] == '1'):
                countOne+=1
            elif layer[i][j] == '2':
                countTwo+=1
    return countOne * countTwo

# Decode layers
def recoverLayers(encodedInput):
    layers=[]
    nb_layers = len(encodedInput) // WIDE // TALL
    for k in range(0, nb_layers):
        M=initMatrix(TALL, WIDE)
        for i in range(0, TALL):
            for j in range(0, WIDE):
                M[i][j]=encodedInput[cursor(i,j,k)]
        layers.append(M)
    return layers

def reconstructImage(layers, image):
    for i in range (TALL):
        for j in range (WIDE):
            for k in range(0, len(layers)):
                if layers[k][i][j] != '2':
                    image[i, j] = int(layers[k][i][j])
                    break;

decodedLayers = recoverLayers(encodedImage)
fewestZeroLayer=findFewestZero(decodedLayers)
print(testLayerCorruption(fewestZeroLayer))

image = Image.new('1', (TALL, WIDE)) # 1 for 1bit black & white (https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#modes)
pixels = image.load()
reconstructImage(decodedLayers, pixels)

image.save("output.jpeg")