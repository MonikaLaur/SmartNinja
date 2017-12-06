a_list= []
b_list= [1,2,3,4]

print a_list
print b_list

# reference
print b_list[1] #prints index value of b_list, index also starts with 0
b_list[1]=10
print b_list
# print a_list[0] IndexError, because list has no elements


# slice
print b_list[1:3] # [10, 3]
print b_list[1:-1] #[10, 3] --> -1 prints the first number from the end of the list
print b_list[-2:] # [3, 4]
print b_list[::-1] # [4, 3, 10, 1]
print b_list[::-2] # [4, 10]
print b_list[::2] # [1, 3]
# [start : end : iteration rule
# iteration rule < 0 --> reverse direction
# iteration rule = 2 --> every other

#append
b_list.append(5)
print b_list # [1, 10, 3, 4, 5]

#remove
b_list.remove(3) #removes all the 3s from the list
print b_list # [1, 10, 4, 5]

#extend
b_list.extend([0,77,99])
print b_list # [1, 10, 4, 5, 0, 77, 99]
b_list += [100,101]
print b_list # [1, 10, 4, 5, 0, 77, 99, 100, 101]