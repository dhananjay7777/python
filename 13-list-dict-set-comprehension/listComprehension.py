myCharlist = [char for char in "DuKeeeeeYYYYYYYYYYY."]
print(myCharlist) #o/p: ['D', 'u', 'K', 'e', 'e', 'e', 'e', 'e', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', '.']

myList = [num for num in range(0,11)]
print(myList) #o/p: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myList2 = [num*2 for num in range(0,11)]
print(myList2) #o/p: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

myList3 = [num*2 for num in range(0,11) if num % 2 == 0]
print(myList3) #o/p: [0, 4, 8, 12, 16, 20]