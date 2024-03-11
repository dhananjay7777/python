# String formatting
name = "xyZ"
age =23
print(f"hi {name}. Your age is {age}") #o/p: hi xyZ. Your age is 23
#========================================================================================================

# In Python, a dictionary is a collection of key-value pairs. It's a data structure that allows you to store 
# and retrieve values by using a key. 
# Dictionaries are mutable, meaning they can be changed after they are created. 
dict = {"name": "DJ", "age": 10 }

#accesing values: dict_name['key']
print(dict['age'])

#changing value: my_dict['key'] = 'new_value'
dict['name'] = "dK."
print(dict) #o/p: {'name': 'dK.', 'age': 10}

# Adding new key-value pairs: my_dict['new_key'] = 'value'
dict["city"] = "ngp"
print(dict) #o/p: {'name': 'dK.', 'age': 10, 'city': 'ngp'}

# Removing key-value pairs: del my_dict['key']
del dict["name"]
print(dict) #o/p: {'age': 10, 'city': 'ngp'}

#----------------------------------------------------------------------------------------------------------
