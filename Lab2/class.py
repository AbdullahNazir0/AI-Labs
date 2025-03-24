# DataTypes:
# Lists, Tuples, Sets, Dictionaries

# Lists:
myList = [1, "String", 3, True, 5]


# Tuples:
myTuple = (1, 2, 3)
# myTuple.pop()

# Sets:
mySet = {1, 2, 1, 1}
print(mySet)
mySet.pop() # Sets dont have an order
print(mySet)

# Dictionaries
myDict = {
    "name": "Abdullah",
    "age": 25,
    "city": "New York"
}
print(myDict)
print(myDict["name"])
myDict["age"] = 26 # Modify
del myDict["city"] # Remove

print(myDict.keys())
print(myDict.values())
print(myDict.items()) # array of key value pairs as tuples
