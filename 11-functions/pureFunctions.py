# A pure function is a function that, given the same input, will always return the same output and does not
#  have any observable side effects. This means that a pure function will not modify any external state or
#  cause any other changes that can be observed outside the function. 

def multiply_by2(li):
   newList = []
   for item in li:
      newList.append(item*2)
   return newList
   # return print(newList) This will have side effects as it interacts with outside world i.e. print statement
   # we give control to print and we don't know what print is going to do

li1 = [2,3,6]
print(multiply_by2(li1)) #o/p: [4, 6, 12]