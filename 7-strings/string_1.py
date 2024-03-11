#3 ways to write string
#1
str1 = "Hey it's me"
#2
str2 = 'Heyyy it"s me'
#3
str3="""Hehheheheheh it's me"""
print(str1)
print(str2)
print(str3)

#operations on string
#1) Concatenation (+): combine 2 or more strings
concatStr = str1 +" "+ str2
print(concatStr)

#2) Length of string (len(str))
print(len(str1)) #o/p: 11

#------------------------------------------------------------------------------------------------------
# Indexing: Gives index to each character in string. We can access character just like arrays
strInd = "ABCDEFGHIJ"
#        ||||||||||
 #index: 0123456789

#accesing 1st character (A)
print(strInd[0]) #o/p: A

# str[3] = "X" #This does not work

#----------------------------------------------------------------------------------------------------------
# Slicing: Accessing part of string

s = "Hello, World!"
print(s[7:])  # O/P: "World!" If the end index is not provided, it defaults to the end of the string.
print(s[:5])  # O/P: "Hello" If the start index is not provided, it defaults to the beginning of the string
print(s[7:12])  # O/P: "World"

# Negative Index
strNeg = "Apple"
#       -5-4-3-2-1         
print(strNeg[-3:-1]) #O/p: pl

#---------------------------------------------------------------------------------------------------------
# Reversing a string
print(s[::-1])  # Output: "!dlroW ,olleH"


