# zip(*iterables): Returns an iterator that aggregates elements from each of the iterables. It stops when the
#  shortest input iterable is exhausted. It's useful for parallel iteration.


new_list = ["x","y"] 
my_list = [1,2,3]
your_list = [10,20,30]

print(zip(my_list, your_list, new_list)) #o/p: <zip object at 0x00000196EBB83B00>
print(list(zip(my_list, your_list, new_list))) #o/p: [(1, 10, 'x'), (2, 20, 'y')] # order in which we zip i.e
# first my_list then your_list and so on
# as there is only "x" and "y" we do not get (3,30)

print(new_list) #o/p: ['x', 'y']
# again we don't modify the original list