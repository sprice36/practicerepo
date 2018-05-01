def theSmallestNumber():
    numbersList = [5,2,6,4,5,6,0,4]
    smallestNumber = numbersList[0]
    for numbers in range(len(numbersList)):
        if (smallestNumber > numbersList[numbers]):
            smallestNumber = numbersList[numbers]
    return smallestNumber