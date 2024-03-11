# Set Comprehension: Similar to list just replace [] with {}

# Syntax: {expression for item in iterable if condition}

numbers = {1, 2, 3, 4, 5}
squares = {x**2 for x in numbers if x % 2 == 0} # first we square numbers and then return only those which are even
print(squares)  # Output: {16, 4}
