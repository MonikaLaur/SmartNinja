def extender(input_list):
    input_list.append("new")
    return input_list

if __name__ == '__main__':
    my_list = ["old"]
    extender(my_list)
    print my_list
