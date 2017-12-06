print "Welcome to Unit Converter!"
print "here you can convert Kilometers into Miles"
print "="*70

while True:
    km = raw_input("Please enter kilometer value:  ")
    km = float(km)

    total = km*0.621371

    print ("%.4f" % total)+ "  Miles (rounded up to 4 decimal points)"

    entry = raw_input("Would you like to convert another value? (press n to exit)")
    if entry == "n":
        print "Thank you for using Unit Converter!"
        break