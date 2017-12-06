# zahlen bis 100

# wenn die zahl gerade print "yu"
# ungerade und grosser als 50 "yo"
# sonst wenn kleiner als 20 "ye
# sonst print die zahl

for number in range(1,101):
    if number %2 == 0:
        print "yu"
    elif number > 50:
        print "yo"
    elif number < 20:
        print "ye"
    else:
        print number 