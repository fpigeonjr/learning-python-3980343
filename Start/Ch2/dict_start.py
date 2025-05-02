# Dictionary: a key-value data structure


# dictionaries are accessed via keys
mydict = {
    "one": 1,
    "two": 2,
    3:  "three",
    4.5: ['four', 'point', 'five']
}
print(mydict)
print(mydict['one'])
print(mydict[3])

# you can also set dictionary data by creating a new key
mydict["seven"] = 7
print(mydict['seven'])

# Trying to access a nonexistent key will produce an error
print(mydict['blah'])


# To avoid this, you can use the "in" operator to see if a key exists
print("two" in mydict)
print("blah" in mydict)


# You can retrieve all of the keys and values from a dictionary
print(mydict.keys())
print(mydict.values())

# You can also iterate over all the items in a dictionary
for key, val in mydict.items():
    print(key, val)
