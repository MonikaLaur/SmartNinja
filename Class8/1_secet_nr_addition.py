
print "Welcome to Guess the Secret Number!"
print "-"*70

secret = int(129)

is_not_found = True

while is_not_found:
    guess = int(raw_input("Type in the number you think is the secret number "))
    is_not_found = guess != secret
    if not is_not_found:
        print "Your guess is correct, secret number is 129, you WON!"
    else:
        print "We're sorry, you guessed wrong!"

