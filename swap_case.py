""" You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. """

def swap_case(s):
    a = s.swapcase()
    return a

if __name__ == '__main__':              #Default
    s = raw_input()
    result = swap_case(s)
    print result

# All test cases valid.