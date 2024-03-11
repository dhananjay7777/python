user = {'basket':123, 'greet': 'hello'}

# 1) dict.get(key, default value=None): The get() method in Python is used to retrieve the value associated 
# with a specified key in a dictionary.
# It takes the key as an argument and returns the corresponding value if the key is found in the dictionary. 
# If the key is not found, it returns a default value (which you can specify) or None if no default value is provided.

# Syntax: value = my_dict.get(key, default=None)
# 'my_dict' is the dictionary you want to look up.
# 'key' is the key you want to retrieve the value for.
# 'default' (optional) is the value to return if the key is not found in the dictionary. If not provided, None is returned by default

print(user.get('age')) #o/p: None [key is not found so it prints default value none]
print(user.get('name', "No Name")) #o/p: No Name i.e [key is not found so it prints default value we specfied i.e No Name]

#-------------------------------------------------------------------------------------------------

# 2) dict(key-value pairs): Another way to create dictonary

user2 = dict(name="JohnJohn")
print(user2) #o/p: {'name': 'JohnJohn'}

#-----------------------------------------------------------------------------------------------------

# 3) dictionary.copy(): The copy() method returns a copy of the specified dictionary.

us = user.copy()
print(user.clear()) #o/p: None [clear method doesn't return anything]
print(us) #o/p: {'basket': 123, 'greet': 'hello'}
print(user) #o/p: {} [as we have cleared user now we have an empty dictionary]

#---------------------------------------------------------------------------------------------------------

# 4) dictionary.pop(keyname, defaultvalue): The pop() method removes the specified item from the dictionary.

print(us.pop('greet')) #o/p: hello [pop returns the value which it has removed]

#----------------------------------------------------------------------------------------------------------

# 5) dictionary.update(iterable): The update() method inserts the specified items to the dictionary.
# The specified items can be a dictionary, or an iterable object with key value pairs.
# If there is already an item with same key, it replaces the old one with new.

us.update({'name': "hellFF"}) 
print(us) #o/p: {'basket': 123, 'name': 'hellFF'}
us.update({'name': 'dukeFFFFFFFFFFFFFFFF.'})
print(us) #o/p: {'basket': 123, 'name': 'dukeFFFFFFFFFFFFFFFF.'}

#------------------------------------------------------------------------------------------------------------

# 6) dictionary.keys(): The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
print(us.keys()) #o/p: dict_keys(['basket', 'name']
print(list(us.keys())) #o/p: ['basket', 'name']

# Iterating over keys
for key in us:
    print(key)
#o/p: basket
#     name
#-----------------------------------------------------------------------------------------------------------

# 7) dictionary.values(): The values() method returns a view object. The view object contains the values of the dictionary, as a list.
print(us.values()) #o/p: dict_values([123, 'dukeFFFFFFFFFFFFFFFF.'])

#iterating over values
for values in us.values():
   print(values)
#o/p: 123
#     dukeFFFFFFFFFFFFFFFF.   

#-----------------------------------------------------------------------------------------------------------'
 
#8) dictionary.items(): The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
print(us.items()) #o/p:dict_items([('basket', 123), ('name', 'dukeFFFFFFFFFFFFFFFF.')])

#iterating over key-value pairs
for key,value in us.items():
    print(key,value)
#o/p: basket 123
#     name dukeFFFFFFFFFFFFFFFF. 

