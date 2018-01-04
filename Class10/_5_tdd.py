def square_numbers(x):
    """
    :param x: number to square
    :type x: int or float
    :return: the square number
    :rtype: int or float
    """
    return x**2

# param , type, and rtype are fixed restructured text words
# param is a parameter, like a comment of what it is
# type describes the data type



def check_square_numbers():
    assert square_numbers(9) == 81
    assert square_numbers(-3) == 9

def cube_numbers(x):
    return x**3

def check_cube_numbers():
    assert cube_numbers(3)==27
    assert cube_numbers(4)==64

if __name__ == '__main__':
    check_square_numbers()
    check_cube_numbers()
    print "Test completed successfully"


# if __name__ == '__main__': --> always written at the end of the code; always called the same
