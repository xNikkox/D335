# As long as x is greater than 0
# Output x modulo 2 (remainder is either 0 or 1)
# Assign x with x divided by 2
x = int(input())


def binary(xx):    # function to convert integer to binary
    while xx > 0:
        xx = xx // 2
        # bin() converts integer to binary string and [2:] removes the 0b prefix
        binary_string = bin(xx)[2:]
        # reversed() reverses the string
        reversed_binary = ''.join(reversed(binary_string))
        return reversed_binary


print(binary(x))
