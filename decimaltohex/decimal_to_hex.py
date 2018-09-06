codes = {   
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
    } 

BASE = 16

def convert(input):
    result = ''
    remainders = []
    value = input / BASE

    while value > 0:
        left = int(value)
        right = value - int(value)

        remainder = right * BASE
        remainders.append(int(remainder))
        value = left / BASE
            
    remainders.reverse()
    
    for r in remainders:
        result += codes.get(r)
    
    return result