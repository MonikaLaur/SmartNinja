while True:
    print 1
    break # if there would be no break the loop would go on forever until the labtop freezes/absturzt

print "Finished"

while True:
    entry = raw_input ("Do you want to continue? (y,n)")
    if entry.lower() == "y": # lower looks if the letter is upper or lower case and accepts upper case letters as well.
        print "lets continue"
    elif entry.lower() == "n":
        break

print "finished"