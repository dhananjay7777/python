# In Python, the term "scope" refers to the region of a program where a particular variable is accessible.

a = 1 #global scope

def parent():
   a = 10 # local scope
   def confusion():
      return a # enclosing scope- scope of parent
   return confusion()

print(parent()) #o/p: 10
print(a) #o/p: 1
   
# Priority: local -> enclosing -> global -> built-in scope. Check in the following order for availability of 
# variable

# 1) Local scope: Variables defined within a function are considered to be in the local scope. These variables 
# are only accessible within the function.

#2) Enclosing scope: This refers to the scope of the enclosing function, in the case of nested functions. 
# Variables in the enclosing scope are accessible within the inner function.

# 3) Global Scope: Variables defined at the top level of a module or explicitly declared as global are considered to be 
# in the global scope. These variables are accessible from anywhere within the module.

# 4) Built-in scope: This refers to the scope of built-in functions and variables that are available in Python without
#  the need for import. Examples include print(), len(), and TypeError.
#------------------------------------------------------------------------------------------------------------
# global keyword: 
total = 0

def count(total):
   total += 1
   return total
print(count(count(count(total)))) #o/p: 3
