# *args and **kwargs are used in function definitions to handle variable-length arguments.

# 1) *args: The *args parameter allows a function to accept a variable number of positional arguments. 
# These arguments are packed into a tuple, which can be accessed within the function.

# 2) The **kwargs parameter allows a function to accept a variable number of keyword arguments (i.e., 
# arguments specified with a name-value pair). These arguments are packed into a dictionary, which can be 
# accessed within the function.



# def superRR(args): # TypeError: superRR() takes 1 positional argument but 5 were given
def superRR(*args,**kwargs):
   # *args and **kwargs are used in function definitions to handle variable-length arguments.
   total = 0
   for item in kwargs.values():
      total += item
   print(args) #o/p: (1, 2, 3, 4, 5)
   print(kwargs) #o/p: {'num1': 10, 'num2': 20}
   return (sum(args) + total)

print(superRR(1,2,3,4,5,num1=10,num2=20)) #o/p: 45 

# Rule of passing paraemeters: functon(params, *args, default params, *kwargs)
# Eg. def superRR(name, *args,x=10, *kwargs)
      # superRR("xD",1,2,3,4,num1=10,num2=20)