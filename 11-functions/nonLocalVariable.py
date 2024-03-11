#nonlocal keyword is used to indicate that a variable inside a nested function should refer to a variable in
#  the nearest enclosing scope that is not global. This allows you to modify variables in an outer 
# (but not global) scope from within a nested function.

def outer():
   x = "locaLLL."
   def inner():
      nonlocal x # if we do not use this, o/p will be Outer "locaLLL."
      x = "nonLocal." # nonLocal means the x of parent. Therefore we are modifying the parent x.
      print("Inner", x)
   inner()
   print("Outer", x)

outer() #o/p: Inner nonLocal. # nonLocal in inner and outer as we modify the parent x.
#             Outer nonLocal.