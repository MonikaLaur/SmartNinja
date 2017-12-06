# Number Between 1 and 100

# User enters number between 1 and 100

# Program prints fizz if number is divisible by 3

# Program prints fizz if number is divisible by 5

# Program prints fizzbuzz if number is divisible by 3 and 5

print "Welcome to FizzBuzz Game"
print "-"*70

user = int(raw_input("Please enter a number between 1 and 100:  "))

limit = (1 < user <= 101)

while limit:
    for number in range (1, user+1):
        if number %3 == 0 and number %5 == 0:
            print "fizzbuzz"
        elif number %3 == 0:
            print "fizz"
        elif number %5 == 0:
            print "buzz"
        else:
            print number
    break
else:
    print "The number you entered is not in range, please enter a valid number!"