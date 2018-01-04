
def addition (x,y):
    summe = x + y
    return summe # return --> give me the result when i ask for it

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y


if __name__ == '__main__':
    result = addition(10, 23)
    print result
    result = subtraction(10,2)
    print result
    result = multiplication(3,9)
    print result
    result = division(100,4)
    print result


# print sum(10,23) --> would give the same result