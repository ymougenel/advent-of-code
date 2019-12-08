#!/usr/bin/env python3

# inputFile=open("inputTest.txt", "r")
# WIDE=3
# TALL=2
inputFile=open("input.txt", "r")
WIDE=25
TALL=6
encodedImages=inputFile.read()


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

# Return image with fewest zeros
def findFewestZero(images):
    minZeroCount=countZeros(images[0])
    minZeroImage=images[0]
    mink=0
    for k in range(1, len(images)):
        currentImage = images[k]
        zerosNb = countZeros(currentImage)
        if zerosNb < minZeroCount:
            minZeroCount = zerosNb
            minZeroImage = currentImage
            mink=k
    return minZeroImage

# Test images curruption (the number of 1 digits multiplied by the number of 2 digits)
def testImageCurruption(image):
    countOne=0;
    countTwo=0;
    for i in range(len(image)):
        for j in range(len(image[0])):
            if (image[i][j] == '1'):
                countOne+=1
            elif image[i][j] == '2':
                countTwo+=1
    return countOne * countTwo

# Decode images
def recoverLayers(encodedInput):
    layers=[]
    nb_images = len(encodedInput) // WIDE // TALL
    for k in range(0, nb_images):
        M=initMatrix(TALL, WIDE)
        for i in range(0, TALL):
            for j in range(0, WIDE):
                M[i][j]=encodedInput[cursor(i,j,k)]
        layers.append(M)
    return layers


decodedImages = recoverLayers(encodedImages)

# for image in decodedImages:
#     printMatrix(image)
#     print()
fewestZeroImage=findFewestZero(decodedImages)
print(testImageCurruption(fewestZeroImage))
