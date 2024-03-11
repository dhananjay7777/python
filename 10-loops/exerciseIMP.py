picture = [
   [0,0,0,1,0,0,0],
   [0,0,1,1,1,0,0],
   [0,1,1,1,1,1,0],
   [1,1,1,1,1,1,1],
   [0,0,0,1,0,0,0],
   [0,0,0,1,0,0,0]
]

# outer for; for 6 list inside the picture list
# inner for; for 0's and 1's inside each list
# end=""; lets each print statement print on same line. Therefore after each list is over, we go to new 
# line using line 19.

for row in picture:
   for pixel in row:
      if pixel == 1: # when 1 is encountered inside list items, print '*'
         print("*",end="")
      else: 
         print(" ",end="")
   print("") # for a new line after every row i.e after every of 6 lists

#    *   
#   ***  
#  ***** 
# *******
#    *   
#    *  
#-----------------------------------------------------------------------------------------------------
# Q.2. Find Duplicates
newList = ["a","b","c","b","d","m","n","n"]
duplicates = []
for val in newList:
   if newList.count(val) > 1:
      if val not in duplicates:
         duplicates.append(val)
print(duplicates) #o/P: ['b', 'n']

# Method 2: 13-list-dict-set-comprehension -> dictComprehension.py
