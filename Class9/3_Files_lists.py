my_list = ["butter", "honey", "milk"]

filename = "ingriedients.txt"

with open (filename, "w") as f:
    list_string = ", ".join(my_list)
    f.write(list_string)

with open (filename, "r") as f:
    content = f.read()
    # not finished look at teacers notes

