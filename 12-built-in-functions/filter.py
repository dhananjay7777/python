# filter(function, iterable): Returns an iterator that filters elements from the iterable for which the 
# function returns true. It's useful for filtering elements based on a condition.

newList = [1,2,3,4]

def findOdd(item):
   if item % 2 !=0:
      return item
   
print(filter(findOdd, newList)) #o/p: <filter object at 0x000002A3882E5C90>
print(list(filter(findOdd, newList))) #o/p: [1, 3]
print(newList) #o/p: [1,2,3,4] # we don't modify our original list
 
# Retuurns an iterator that contains elements for which the function returned True.
