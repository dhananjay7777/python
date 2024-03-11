marks = [69.3,99.8,100,99.9,99.97]
print(marks)
print(type(marks))  #o/p: <class 'list'>
print(len(marks)) #o/p: 5

#accessing paricular element: similar to array
print(marks[2]) #o/p:100 

#we can store elements of diff. data types together
student = ["kD", 78.8, "Nagpur", 100]

#list are mutuable i.e we can reassign a value in list.
student[0] = "dB"
print(student) #o/p: ['dB', 78.8, 'Nagpur', 100]

# We can also do slicing in list similar to string
sli = [1,2,3,4,5]
print(sli[::-1]) #o/p: [5, 4, 3, 2, 1]

