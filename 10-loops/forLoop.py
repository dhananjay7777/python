# for loop: for loop is used to iterate over a sequence (like a list, tuple, string, or range) or any other 
# iterable object. It executes a block of code repeatedly for each item in the sequence or iterable.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
# for loop iterates over the numbers list, and for each iteration, it assigns the current number to the number 
# variable and then prints it. The loop repeats this process for each number in the list.
    
for x in "DuKE.":
    print(x)

#nested for loop
for x in [1,2,3]:
    for y in ["a", "b", "c"]:
        print(x,y)
#o/p: 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
        
