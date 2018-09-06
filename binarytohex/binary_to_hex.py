codes = {   
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '8',
    '1001': '9',
    '1010': 'A',
    '1011': 'B',
    '1100': 'C',
    '1101': 'D',
    '1110': 'E',
    '1111': 'F'
    }

def convert(input):
    result = ''
    nibbles = get_chunks(input, 4)

    for nibble in nibbles:
        result += codes.get(nibble)

    return result

def get_chunks(value, chunksize):
    chunks = []
    i = 0
    while i < len(value):
        if (i + chunksize) > len(value):
            chunks.append(value[i:])
        else:
            chunks.append(value[i:i+chunksize])
        i += chunksize

    return chunks