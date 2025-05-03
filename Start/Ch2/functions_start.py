# define a basic function
def hello():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you,", name)

hello()

# function that takes parameters
def helloName(greeting):
    name = input("What is your name? ")
    print(greeting, name)

helloName('Was up')

# function that returns a value
def cube(x):
    return x * x * x

print(cube(3))

# function with default value for an parameter
def helloName(greeting = 'Nice to meet you', name = None):
    if (name == None):
        name = input("What is your name? ")
    print(greeting, name)

helloName("Was happening")
helloName(name="Frank", greeting="Was up") # allows you to change the order

# function with variable number of parameters
def multi_add(start, *args):
    result = start
    for x in args:
        result += x
    return result
print(multi_add(100, 2, 3, 4))
