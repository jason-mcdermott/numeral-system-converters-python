map = {   
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

base = 16

def convert(input):
    result = ''
    remainders = []
    value = input / base

    while value > 0:
        left = int(value)
        right = value - int(value)

        remainder = right * base
        remainders.append(int(remainder))
        value = left / base
            
    remainders.reverse()
    
    for r in remainders:
        result += map.get(r)
    
    return result