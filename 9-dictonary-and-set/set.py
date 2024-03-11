# In Python, a set is an unordered collection of unique elements. It is similar to a mathematical set and has 
# operations like union, intersection, difference, and symmetric difference. 
# Sets are mutable, meaning you can add or remove elements from them, but they cannot contain mutable elements 
# like lists or dictionaries.

# Creating a set
my_set = {1,2,3,4,5,"Hello"}
print(my_set) #o/p: {1, 2, 3, 4, 5, 'Hello'}

# A set cannot have duplicate value
dup_set = {1,1,2,3,3,3,4,4,5}
print(dup_set) #o/p: {1, 2, 3, 4, 5}

# Removing all dulicate values from list
listNew = [11,11,22,33,22,33,44,44,11,22]
newSet = set(listNew)
print(newSet) #o/p: {33, 11, 44, 22} [as its an unoreder collection, values are printed at random]

# Adding elements
my_set.add(10)
print(my_set) #o/p: {1, 2, 3, 4, 5, 'Hello', 10}

# Removing elements
my_set.remove(1)
print(my_set) #o/p: {2, 3, 4, 5, 'Hello', 10}

# Checking membership
if 2 in my_set:
    print("2 is in the set")
#o/p: 2 is in the set

# Iterating over a set
for item in my_set:
    print(item)
#o/p: 2
#     3
#     4
#     5
#  'Hello'
#    10
    