tup = (1,34,23,6,10,1,3)
#1) tup.index(element): returns index of first occurence element
print(tup.index(1)) #o/p: 0

#2) tup.count(element): count total occurences of an element
print(tup.count(1)) #o/p: 2


#-------------------------------------------------------------------------------------------------------
# Q1. Input 3 movies and store them in a list
movies = []
# mov1  = str(input("Enter first movie name: "))
# movies.append(mov1)
# mov2  = str(input("Enter second movie name: "))
# movies.append(mov3)
# mov3  = str(input("Enter third movie name: "))
# movies.append(mov3)
# OR movies = [mov1,mov2,mov3]

#OR 

movies.append(input("Enter first movie name: "))
movies.append(input("Enter second movie name: "))
movies.append(input("Enter third movie name: "))
print(movies)

#--------------------------------------------------------------------------------------------------

# Q.2: Check if list contains palidrome 
# Only difference in Method 1 and Method 2 is line 34,35 and line 43

list1  = [1,2,3,2,1]
# Method 1
copyLi = []
copyLi = list1
copyLi.reverse() 
if(copyLi == list1):
   print("PalinDrome")
else: 
   print("Not PalinDrome")

# Method 2
# copyList1 = list1.copy()
# copyList1.reverse()
# # if(list1 == copyList1):
#    print(True)
# else:
#    print(False) 