set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

# 1) set1.difference(set2): Prints all elements unqiue in set 1.It doesn't modify the orginal set, it just prints
# the difference.
print(set1.difference(set2)) #o/p: {1, 2, 3}

# 2) set1.discard(element): Removes an element from set1.
# set1.discard(1)
set1.discard(6) # discarding an element which is not present.
print(set1) #o/p: {2, 3, 4, 5}

#3) set1.difference_update(set2): Remove all elements of another set from this set. It modifies the original array
# unlike set1.difference() method
# set1.difference_update(set2)
print(set1) #o/p: {1, 2, 3}

# 4) set1.intersection(set2): Common elements in both sets.
print(set1.intersection(set2)) #o/p: {4, 5} 

#5) set1.isdisjoint(set2): Returns True if two sets do not have anything in common. False if they have common
setA = {1,2,3,4,5}
setB = {4,5,6,7,8,9,10}
print(setA.isdisjoint(setB)) # o/p: False

#6) set1.union(set2): Combines both sets and removes the dupicates
print(setA.union(setB)) #o/p: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#7) set1.issubset(set2): returns True if set1 contains all the elements of set2 and doesn't have any extra elements
# Entire set1 is inside set2
setOne = {1,2,3,5}
setTwo = {1,2,3,4}
print(setOne.issubset(setTwo)) #o/p: False [because of 5 in setOne]

# 8) set1.issuperset(set2): returns True if set2 has all elements of set1 and doesn't have any extra elements
print(setOne.issuperset(setTwo)) #o/p: False [because of 4 in setTwo]
