# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
print("the length of the list is:",len( mylist))

# to access a member of a sequence type, use []
print(mylist[2])
print(mylist[-1])
mylist[0] = 10
print(mylist)
# add a list to another list
another_list = [6, 7, 8]
mylist = mylist + another_list # combine arrays together
print(mylist)
# use slices to get parts of a sequence
print(mylist[1:4]) #start, end, step amount
# parametors are optional
print(mylist[::2]) #start, end, step amount

# you can use slices to reverse a sequence
print(mylist[::-1]) #start, end, step amount


# Tuples are like lists, but they are immutable
mytupple = (0, 1, 2, "three")
print(mytupple)
print(mytupple[0])

# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 4, 2, 'five'}
print(myset) # will be unique only shows one 2
# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in mylist)
print(3 in mytupple)
print(5 in myset)
