# map(function, iterable): Applies the function to every item in the iterable and returns a new iterable with 
# the results. It's useful for applying a function to every element in a list.

my_list = [1,2,3,4]

def multiplyBy2(item):
   return item * 2

print(map(multiplyBy2, my_list)) #o/p: <map object at 0x00000125742E5870>
print(list(map(multiplyBy2, my_list))) #o/p: [2, 4, 6, 8]
print(my_list) #o/p: [1,2,3,4] # we don't modify our original list
# we are not calling the function. 'map' is going to call the function for us.

