import _2_addition_func as CALC

def check_addition():
    assert CALC.addition(10,20)==30

def check_subtraction():
    assert CALC.subtraction(10,20)==-10

def check_multiplication():
    assert CALC.multiplication(10,10)==100

def check_division():
    assert CALC.division(50,5)==10

if __name__ == '__main__':
    # print CALC.addition(10,-23)
    check_addition()
    check_subtraction()
    check_multiplication()
    check_division()
    print "Passed all tests"

# assert checks if the function works properly if not will return assertion error