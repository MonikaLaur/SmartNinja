# print welcome to user

print "Welcome to the calculator"
print "-"*50

while True:

# read user input for operation

    while True:

        operation_symbol = raw_input("Please enter an operation (+,-,*,/): ")
        print "You entered " + operation_symbol
        if operation_symbol in ["+","-","*","/"]:
            break
        else:
            print "Please enter a valif operation symbol, you entered: "+ operation_symbol

# read user input for first value
    while True:
        try:
            first_value = float(raw_input("Please enter first value: "))
            print "You entered " + str(first_value)
            break
        except ValueError:
            print "Please enter a valid number, you entered: " + str(first_value)

    # read user input for second value
    while True:
        try:
            second_value = float(raw_input("Please enter second value: "))
            print "You entered ", str(second_value) # viewed same as in first value , is an example of different way
            break
        except ValueError:
            print "Please enter a valid nuber, you entered: " + str(second_value)

    # calculate
    if operation_symbol == "+":
       print first_value + second_value
    elif operation_symbol =="-":
        print first_value - second_value
    elif operation_symbol == "/":
            if second_value == 0:
                print "division by Zero!?"
            else:
                print first_value / second_value
    elif operation_symbol =="*":
        print first_value * second_value
    else:
        print "You have entered an invalid operation"

    # print result
    entry = raw_input("One more time? (press n to exit)")
    if entry == "n":
        break
