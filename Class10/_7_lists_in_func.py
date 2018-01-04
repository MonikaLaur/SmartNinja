def change_list (a_list):
    a_list.append("new")

if __name__ == '__main__':
    my_list = range(19)
    print my_list
    change_list(my_list)
    print my_list

