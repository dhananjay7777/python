# Immutable sequence of chracters

tup = (1,2,3,55,66,87)
print(type(tup)) #o/p: <class 'tuple'>

# accessing elements: Similar to list
print(tup[1]) #o/p: 2

# empty tuple
tupEm = ()

# tuple with one element: We store it with comma as if we don't the type will change and will not be tuple
tupSing = (1,)
print(type(tupSing)) #o/p: <class 'tuple'>

tupOne = (1)
print(type(tupOne)) #o/p: <class 'int'>

# SLICING SIMILAR TO LIST/STRING
print(tup[1:]) # o/p: (2, 3, 55, 66, 87)
