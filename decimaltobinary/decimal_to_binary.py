def convert(input):
    assert(type(input) == int), "Input must be an integer"

    BASE = 2
    bins = [1]
    output = []
    tail = bins[-1]

    while input > tail:
        next = tail * BASE
        bins.append(next)
        tail = bins[-1]

    compareTo = input

    bins.reverse()

    for b in bins:
        if b <= compareTo:
            output.append(1)
            compareTo = compareTo - b
        else:
            output.append(0)

    # pad with zero's...
    while len(output) % 4 != 0:
        output.insert(0, 0)

    result = ''.join(map(str,output))

    return result