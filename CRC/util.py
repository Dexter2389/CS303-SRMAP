import re


def xor(a, b):
    '''
    XOR operation

    Arguments:
    a = string of 1s and 0s
    b = string of 1s and 0s

    Returns:
    stringyfied result of xor(a, b)
    '''

    if re.match('^[0-1]*$', a) and re.match('^[0-1]*$', b):
        pass
    else:
        return ("Invalid input string.")

    result = []

    # Traverse all bits
    # If bits are same, then append 0 else append 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append("0")
        else:
            result.append("1")

    return "".join(result)


def mod2div(divident, divisor):
    '''
    Perform Modulo-2 Division

    Arguments:

    Return:
    '''
    pick = len(divisor)
    temp = divident[0: pick]

    while pick < len(divident):
        if temp[0] == "1":
            temp = xor(divisor, temp) + divident[pick]
        else:
            temp = xor("0"*pick, temp) + divident[pick]

        pick += 1

    if temp[0] == "1":
        temp = xor(divisor, temp)
    else:
        temp = xor("0"*pick, temp)

    checkword = temp
    return checkword


def dataCapsulation(data, key):
    '''
    Arguments:

    Return:
    '''

    l_key = len(key)

    append_data = data + "0"*(l_key-1)
    remainder = mod2div(append_data, key)

    return remainder
