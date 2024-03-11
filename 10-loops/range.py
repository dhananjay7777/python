# The range() method in Python is used to generate a sequence of numbers. It's often used in for loops to 
# iterate over a sequence of numbers.

#The range() method can take one, two, or three arguments:

# range(stop): Generates a sequence from 0 to stop - 1.
# range(start, stop): Generates a sequence from start to stop - 1.
# range(start, stop, step): Generates a sequence from start to stop - 1, incrementing by step.

# Print numbers from 0 to 4
for num in range(5):
    print(num)

# Print numbers from 1 to 5
for num in range(1, 6):
    print(num)

# Print even numbers from 0 to 10
for num in range(0, 11, 2):
    print(num)

# negative range from 10 to 0
for _ in range(10,0,-1):
   print(_)

# quick way to create list
for x in range(2):
   print(list(range(1,10)))
#o/p: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]