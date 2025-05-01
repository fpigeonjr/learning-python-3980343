# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True 

# We can display the content of a variable using the print() function
# print(myint)
# print(mystr)


# Operators are used to perform operations on variables
# print(myint + myfloat)
# print(myint * myfloat)
# print(myint / myfloat)
# print(myint % 3) # modulo operator, remainder 1 / 3 = 1

# another_str = "This is another string"
# print(mystr + another_str)
# print("nom " * 3)
# Logical and comparison operators 
print(myint == 10) 
print(myint != 30) 
print(myint > 20) 
print(myint < 5 and  myint <= 25) # && in JS
print(myint < 5 or  myint <= 25) # || in JS
print(not (myint < 5 or  myint <= 25)) # flip the Boolean


# re-declaring a variable works
myint = "redeclare to a string" # not a const, more like a let
print(myint)