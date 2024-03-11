# 1) Implicit type conversion: Python converts automatically
# int + float = float
num_int = 123
num_float = 1.23
total = num_int + num_float
print(total) #o/p: 124.23

#2) Explicit Type Conversion: You can explicitly convert a value from one type to another using built-in 
# functions like int(), float(), str()
num_int = 123
num_str = "456"
num_sum = num_int + int(num_str)  # Explicit conversion of str to int
print(num_sum) # o/p: 579


# Type Conversion Errors: It's important to note that not all types can be converted to each other. 
# For example, trying to convert a string that contains non-numeric characters to an integer will raise a 
# ValueError.

a = int(input("Enter A: "))
b = int(input("Enter B: "))

print("true") if a>=b else print("false")