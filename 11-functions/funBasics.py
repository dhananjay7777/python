# In Python, a function is a block of reusable code that performs a specific task. Functions provide a way to
#  modularize your code, making it easier to read, understand, and maintain.

# Here's a simple explanation of how functions work:

# 1.Define a Function: To create a function, you use the def keyword followed by the function name and 
# parentheses ( ), which may include parameters (inputs) the function will take. The function body is 
# indented below the def statement.

# 2.Call a Function: To use a function, you "call" it by using its name followed by parentheses ( ). If the 
# function takes parameters, you provide them inside the parentheses.

# 3.Return Values: Functions can return values using the return keyword. This allows the function to send 
# data back to the caller. No code is executed after return statement inside the function.

def add_num(a,b): # a,b: parameters- used when we define the function
   sum = a + b
   return sum

result = add_num(10,5) # 10,5: arguments- used when we call/invoke the function
print(result) #o/p: 15
print(add_num) #o/p: <function add_num at 0x00000224F0CEA2A0> [location of function]
#--------------------------------------------------------------------------------------------------------
# nested function: 
# we define a function. Inside that function we define another function(child). Inside child function we perform 
# subtraction and return the subtraction. In the parent function we return the child function by passing parameters
# received by parent.
def sub_num(n1,n2):
   def main_sub(num1,num2):
      return num1-num2
   return main_sub(n1,n2)

res = sub_num(10,5)
print(res)  #o/p: 5