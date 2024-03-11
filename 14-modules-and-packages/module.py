# In Python, a module is a file containing Python code. It can define functions, classes, and variables, and
#  can also include runnable code. 
# Modules allow you to logically organize your Python code into reusable components.

import utility #importing module 
import shopping.shopping_cart #importing a package


print(utility) #o/p: <module 'utility' from 'j:\\Data Science\\python\\14-modules\\utility.py'>

# using function in utility.py file
print(utility.mul(2,3)) #o/p: 6
print(shopping.shopping_cart.add_item(10)) #o/p: [10]

# or 
# from shopping.shopping_cart import add_item
# print(add_item(10))