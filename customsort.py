#this program will sort the numbers in the given list
def customSort(numArray):
    length = len(numArray) #getting the length of the list
    for i in range(length):
        for j in range(length - i - 1):
            if numArray[j] > numArray[j + 1]:
                numArray[j], numArray[j + 1] = numArray[j + 1], numArray[j]
    return numArray