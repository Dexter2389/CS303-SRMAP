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


def decodeData(codeword, key):
    '''
    Arguments:

    Return:
    '''

    l_key = len(key)

    append_data = codeword + "0"*(l_key-1)
    remainder = mod2div(append_data, key)

    print("Remainder after decoding: " + remainder)

    temp = "0" * (len(key) - 1)
    if remainder == temp:
        print("Data recieved successfully without errors")
    else:
        print("Error")

    return remainder

def encodeData(data, key):
    '''
    Arguments:

    Return:
    '''

    print("Raw data to send: ", data)

    l_key = len(key)

    append_data = data + "0"*(l_key-1)
    remainder = mod2div(append_data, key)

    codeword = data + remainder
    print("Encoded data ready to send: " + codeword)

    return codeword

if __name__ == "__main__":

    input_string = input("Enter data you want to send:\n---> ")
    data = ("".join(format(ord(x), 'b') for x in input_string))
    key = "1001"
    codeword = encodeData(data, key)
    decodeData(codeword, key)
