import itertools

map = {   
    '0': 0,
    '1': 1, 
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15 
    } 

base = 16

def convert(input):
    ints = []
    result = 0

    for c in input:
        ints.append(map.get(c))

    ints.reverse()

    for idx, val in enumerate(ints):
        if(val != 0):
            result += ints[idx] * pow(base, idx)

    return result


