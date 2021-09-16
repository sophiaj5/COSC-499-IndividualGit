def customSort(numArray):
    length = len(numArray)
    for i in range(length):
        for j in range(length - i - 1):
            if numArray[j] > numArray[j + 1]:
                numArray[j], numArray[j + 1] = numArray[j + 1], numArray[j]
    return numArray