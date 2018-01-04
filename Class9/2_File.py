text = "This text should be in a nice file"

filename = "my_text.txt"

# a : append ---> will add at the end

# w : write ---> will overwrite

# r : read

with open (filename, "w") as f:
    f.write(text)

print "done"

with open (filename, "r") as f:
    content = f.read(text)
    print content

with open(filename, "a") as f:
    f.append(text)

