import random

points = 0
capitals = {"France": "Paris",
            "Iceland": "Reykjavik",
            "Denmark": "Copenhagen",
            "Lithuania": "Vilnius",
            "Canada": "Ottawa",
            "Austria": "Vienna"}

current_country = random.choice(capitals.keys())

guess = raw_input("Enter the capital of "+current_country +"  ")

if guess==capitals[current_country]:
    print "congratulations you guessed correct!"
else:
    print "sorry you're wrong!",
