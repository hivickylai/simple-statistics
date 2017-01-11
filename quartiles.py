'''
A simple quartiles calculator that takes one line of input:
    array = a space separated list of values
and returns the first, second, and third quartiles as integers.
'''

array = sorted([int(x) for x in input().split()])

def median(values):
    values = sorted(values)
    if len(values)%2 == 0:
        return (values[(len(values)//2)-1] + values[(len(values)//2)]) / 2
    else:
        return values[(len(values)//2)]

if len(array)%2 == 0:
    lowhalf = array[0:(len(sorted(array))//2)]
    uphalf = array[(len(sorted(array))//2):]
else:
    lowhalf = array[0:(len(sorted(array))//2)]
    uphalf = array[(len(sorted(array))//2)+1:]

print('array:', array)
print('lowhalf:', lowhalf)
print('uphalf:', uphalf)
print(int(median(lowhalf)))
print(int(median(array)))
print(int(median(uphalf)))