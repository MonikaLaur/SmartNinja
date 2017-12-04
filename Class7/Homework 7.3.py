
print "Welcome to Guess the Secret Number!"
print "-"*70

while True:
    secret = int(129)

    guess = int(raw_input("Type in the number you think is the secret number "))

    if guess == secret:
        print "Your guess is correct, you WON!"
    else:
        print "We're sorry you guessed wrong!"

    entry = raw_input("Would you like to try again? (press n to exit)")
    if entry == "n":
        break
