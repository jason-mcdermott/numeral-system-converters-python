def convert(input):
    assert type(input) is str, "Input must be a string" 

    result = 0
    bits = []

    for i in input:
        assert(i == '1' or i == '0'), "Input must only contain '1' or '0'"
        bits.append(i)

    bits.reverse()

    for idx, val in enumerate(bits):
        if int(val) != 0:
            result += pow(2, idx)

    return result