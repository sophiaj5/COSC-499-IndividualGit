#this is a program to find the biggest number in a list

def findMaxNum(numArray):
    if type(numArray) == list:
        return max(numArray)
    else:
        raise ValueError("Was expecting a list")


numbers = [13, 7, 16, 28, 2]
print("The max number is :" , findMaxNum(numbers))