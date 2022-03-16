import math

t = float(input("Enter a tempeture in Fahrenheit :"))
v = float(input("Enter the  wind speed of mph: "))

def windChill(t, v):
    windChillTemp = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)

    print("The wind chill is: ", windChillTemp)


windChill(t, v)