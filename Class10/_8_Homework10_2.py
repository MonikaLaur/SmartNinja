import random

print "Welcome to Guess the Secret Number!"
print "-"*70
print "The secret number is a number between 0 and 101"

def main():
    while True:
        secret = random.randint(1, 100)

        guess = int(raw_input("Type in the number you think is the secret number:   "))

        check_guess(secret, guess)

        again = raw_input("Would you like to try again? (press n to exit)")
        if again == "n":
           break

    print "END"
    print "-"*70

def check_guess(secret, guess):
    if secret == guess:
        print "Your guess is correct you WON!"
        return True
    else:
        print "We're sorry, you guessed wrong!"
        return False

if __name__ == '__main__':
    main()
