# List, set, and dictionary comprehensions are concise ways to create lists, sets, and dictionaries in Python,
# respectively. They allow you to write compact and readable code for creating these data structures based on
# existing iterables (like lists, tuples, or ranges) or other data structures.


# List Comprehension:

# Syntax: [expression for item in iterable if condition]


# 1) Creating a list of chracters
myCharlist = [char for char in "DuKeeeeeYYYYYY."]
print(myCharlist) #o/p: ['D', 'u', 'K', 'e', 'e', 'e', 'e', 'e', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', '.']


#2) Creating a list from number 0 to 10
myList = [num for num in range(0,11)]
print(myList) #o/p: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 3) Creating a list which has 2 times each number from 0 to 10
myList2 = [num*2 for num in range(0,11)]
print(myList2) #o/p: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# 4) Creating a list which has 2 times each number from 0 to 10 and they are even after multiplication
myList3 = [num*2 for num in range(0,11) if num % 2 == 0]
print(myList3) #o/p: [0, 4, 8, 12, 16, 20]