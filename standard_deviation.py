'''
Calculates the standard deviation of an array. Takes one line of input:
    arrayX = a space separated list of values for which you want to find the standard deviation
and returns the standard deviation as a floating point number rounded to one decimal place.
Disclaimer: I'm no mathematician.
'''
import math

arrayX = [int(x) for x in input().split()] 
mean = sum(arrayX) / len(arrayX)
thingy = sum([(i - mean)*(i - mean) for i in arrayX])

print(round(math.sqrt(thingy / len(arrayX)), 1))