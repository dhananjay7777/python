# In Python, a while loop is used to repeat a block of code as long as a specified condition is true. It's like 
# a for loop, but instead of iterating over a sequence, it continues looping as long as a certain condition 
# remains true.

# Here's a simple explanation of how a while loop works:

# You have a condition that you want to check.
# If the condition is true, the code inside the while loop is executed.
# After the code inside the loop is executed, the condition is checked again.
# If the condition is still true, the code inside the loop is executed again. This process continues until 
# the condition becomes false.

count = 0
while count<=5:
   print(count)
   count += 1
 #o/p: 0
# 1
# 2
# 3
# 4
# 5
#------------------------------------------------------------------------------------------------------
# while-else: else is executed if while loop is false
x = 0
while x<=3:
   print(x)
   x+=1
   break
else:
   print("xD")
#o/p: 0 
# after break, the loop breaks and as while-else is part of one single block, else in not executed.

#--------------------------------------------------------------------------------------------------------
while True:
   x = input("saY something: ")
   if(x == "bye"):
      break