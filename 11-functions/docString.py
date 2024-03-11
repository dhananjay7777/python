# These are basically comments that are used to define/describe meaning of a function.\
# It is used to provide documentation or a description of what the function, method, class, or module does.

def test(a):
   '''
   This function is used to print value of A.
   '''
   print(a)

test("xD.")
# when we hover over test we will see the docstring.

#1st way to access
print(test.__doc__) #o/p:   This function is used to print value of A.

#2nd way to access
help(test)
#o/p: Help on function test in module __main__:
# test(a)
#  This function is used to print value of A.