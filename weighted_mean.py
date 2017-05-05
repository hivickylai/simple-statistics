'''
A simple weighted mean calculator that takes two lines of input:
    values = a list of space separated values for which you want to find the weighted mean
    weights = a list of space separated numbers representing the weight to apply to each corresponding item of the values list
and returns the weighted mean as a floating point number.
'''

values = list(map(int, input().split()))
weights = list(map(int, input().split()))

output = sum([x[0] * x[1] for x in zip(values, weights)]) / sum(weights)

print(round(output, 1))