user = {
   "name": "Golem",
   "age":300,
   "can_swim": True
}

# normal iterating
for val in user:
   print(val)  #o/p: name age can_swim

#iterating keys
for val1 in user.keys():
   print(val1) #o/p: name age can_swim

#iterating value
for val2 in user.values():
   print(val2) #o/p: Golem 300 True

#iterating key-value
for val3 in user.items():
   print(val3)  #o/p: ('name', 'Golem')  ('age', 300)  ('can_swim', True)

for x1,x2 in user.items():
   print(x1,x2)
#o/p: name Golem
#     age 300
#     can_swim True

