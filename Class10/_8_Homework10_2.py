import random

print "Welcome to Guess the Secret Number!"
print "-"*70
print "The secret number is a number between 0 and 101"

if __name__ == '__main__':
    while True:
        secret = random.randint(1,100)
        guess = int(raw_input("Type in the number you think is the secret number:   "))

        if guess == secret:
            print "Your guess is correct you WON!"
        else:
            print "We're sorry, you guessed wrong!"

        entry = raw_input("Would you like to try again? (press n to exit)")
        if entry == "n":
            break