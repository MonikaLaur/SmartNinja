print "Welcome to Unit Converter!"
print "here you can convert Kilometers into Miles"
print "="*70

km = raw_input("Please enter kilometer value:  ")
km = float(km)

total = km*0.621371

print ("%.4f" % total)+ "  Miles (rounded up to 4 decimal points)"
