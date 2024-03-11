# 
# In Python, enumerate() is a built-in function that adds a counter to an iterable (like a list, tuple, 
# string, etc.) and returns it as an enumerate object.
# The enumerate object contains pairs of index and value, which can be useful for iterating over both the 
# index and value of an iterable simultaneously.


# retuns index and value
for i,val in enumerate("Hellllooooo"):
   print(i,val)
# o/p: 0 H
#      1 e
#      2 l
#      3 l
#      4 l
#      5 l
#      6 o
#      7 o
#      8 o
#      9 o
#      10 o


for i,char in enumerate(range(100)):
   if char==50:
      print(f"Index of 50 is {i}") 
#o/p: Index of 50 is 50