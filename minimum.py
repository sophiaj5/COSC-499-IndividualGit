#this is a program to find the smallest number in a list

def findMinNum(numArray):
    if type(numArray) == list:
        numArray.sort()
        return numArray[0]
    else:
        raise ValueError("Was expecting a list")

numbers = [13, 7, 16, 28, 2]
print("This is the smallest number:", findMinNum(numbers))