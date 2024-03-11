# all list methods directly modify the original list 

list = [2,1,5,3]

# 1) list.append(value): adds one element to end of list
list.append(4)
print(list) #o/p: [1, 2, 3, 4]

#2) list.sort(): sort list in ascending order
list.sort()
print(list.sort()) #o/p: None [as it is changing the original list, it doesn't return anything]
print(list) #o/p: [1, 2, 3, 4, 5]

# sorting list is descending order
listAlpha = ["a","f","z","y","p"]
listAlpha.sort(reverse=True) 
print(listAlpha) #o/p: ['z', 'y', 'p', 'f', 'a'] 

# 3) list.reverse(): reverses list
listAlpha.reverse()
print(listAlpha) #o/p: ['a', 'f', 'p', 'y', 'z'] (reverses based on above output of line 15)

# 4) list.insert(index,element): Insert element at index
list.insert(0, 10)
print(list) #o/p: [10, 1, 2, 3, 4, 5]

# 5) list.remove(element): remove first occurence of element
list.remove(3)
print(list) #o/p: [10, 1, 2, 4, 5]

# 6) list.pop(index): removes element at index
list.pop(1)
print(list) #o/p: [10, 2, 4, 5] 