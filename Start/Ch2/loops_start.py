x = 0

# define a while loop
while x < 5:
    print(x)
    x= x + 1

# another example
answer = input("Should I stop?")
while answer != "yes":
    print(answer)
    answer = input("Should I stop?")

# define a for loop
days = ['M', 'T', 'W', 'Th', 'F']
for d in days:
    print(d)

# use the break and continue statements
days = ['M', 'T', 'W', 'Th', 'F']
for d in days:
    if(d == "W"):
        break # terminates loop
    if(d == "Th"):
        continue # skips this iteration
    print(d)

# using the enumerate() function to get an index and an item
for i, d in enumerate(days):
    print(i, d) # 0 M, 1 T, etc
