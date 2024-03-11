# Dictionary Comprehension:

# Syntax: {key_expression: value_expression for item in iterable if condition}

# 1) Print square of a number(value) only if they are even
simple_dict = {
   "a": 1,
   "b": 2
}

new_dict = {key : value**2 for key,value in simple_dict.items() if value % 2 == 0}

print(new_dict) #o/p: {'b': 4}

#------------------------------------------------------------------------------------------
# 2) Dictonary with key = number and value = square of that Number

dictxD = {x:x**2 for x in [1,2,3]}
print(dictxD) # o/p: {1: 1, 2: 4, 3: 9}

#------------------------------------------------------------------------------------------------------------------
# Q. Duplicates in a list and return a new list with duplicates
some_list = ['a','b','c','b','d','m','n','n']
duplicates  = list({x for x in some_list if some_list.count(x)>1})
print(duplicates) #o/p: ['b', 'n']

#---------------------------------------------------------------------------------------------------------
z = "hel"[0]
print(z)