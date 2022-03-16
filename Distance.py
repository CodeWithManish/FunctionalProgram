import math
x1 = int(input("Enter the value of x1: "))
x2 = int(input("Enter the value of x2: "))
y1 = int(input("Enter the value of y1: "))
y2 = int(input("Enter the value of y2: "))


def calculateDistance():

    dist = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

    print("The Euclidean Distance between points is: ", dist)
calculateDistance()