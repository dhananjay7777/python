# reduce(function, iterable[, initializer]): Applies the function of two arguments cumulatively to the items 
# of the iterable, from left to right, so as to reduce the iterable to a single value. It's useful for 
# performing computations on a list and returning a single result.

from functools import reduce

myList = [1,2,3]

def accumulator(acc,item): # item is each value in myList list, acc = 0 from intial value passed in line 19
   print(acc,item)
   return acc + item

# acc(current pass) = (acc + item) of previous pass
# first pass: acc=0 item = 1
# second pass: acc=(0+1)=1 item = 2
# third pass: acc=(1+2)=3 item = 3
# fourth pass: acc = (3+3) = 6

print(reduce(accumulator,myList,0)) #0 is the intial value of acc in line 9
#o/p: 0 1
#     1 2
#     3 3
#     6
print(myList) #o/p: [1, 2, 3]