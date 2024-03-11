# list and tuple inside dictionary
dictNew = {"srNo": [1,2,3,4], "rollNo": (44,53,21,23)}
print(dictNew) #o/p: {'srNo': [1, 2, 3, 4], 'rollNo': (44, 53, 21, 23)}

# dictionary inside list: accessing value using key inside this
listNew = [
   {"srNo": [1,2,3,4], "rollNo": (44,53,21,23)}, 
   {"srNo": [5,6,7,8], "rollNo": (45,33,11,26)}
   ]
print(listNew) #o/p: [{'srNo': [1, 2, 3, 4], 'rollNo': (44, 53, 21, 23)}, {'srNo': [5, 6, 7, 8], 'rollNo': (45, 33, 11, 26)}]
print(listNew[1]["srNo"][0]) #o/p: 5

# key: It's unique. It cannot change. Therefore list cannot be a key as it can change
myDict = {
   True:23,
   123:123,
   "name": "dQ.",
   (100): "xD."  }
print(myDict) #o/p: {True: 23, 123: 123, 'name': 'dQ.', 100: 'xD.'}