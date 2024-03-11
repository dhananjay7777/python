# 1: String and Numeric Value: Basically used to repeat text.
a,b=2,3
txt = "@"
print(2*txt*3) #o/p: @@@@@@ [6(2*3) times @]

#---------------------------------------------------------------------------------------------------------

#2: String can operate with string using "+". Also called CONCATENATION
c = "2"
d = "a"
print(c+d*4) #o/p: 2aaaa [c: 1 time and d: 4 times]
print((c+d)*4) #o/p: 2a2a2a2a [c and d together: 4 times]

#---------------------------------------------------------------------------------------------------------

#3: Numeric values with arithemetic operators
print(2*3+4) #o/p: 10 [as multiplication has higher precedence than addition 2*3=6 and then 6+4 = 10]

#---------------------------------------------------------------------------------------------------------

#4: Float with interger will result in FLOAT
print(2*3.5) #o/p: 7.0 [and not 7]
print(2-1.5) #o/p: 0.5

#---------------------------------------------------------------------------------------------------------

#5: Result of division of 2 intergers will be FLOAT
print(2/1) #o/p: 2.0

#---------------------------------------------------------------------------------------------------------'

#6: Interger Division (//): First it will carry out division and roundoff(round-down) the value. [0.5 -> 0]. Basically,
# it will floor the value i.e round down.Then it will convert the interger value obtained into float. [0 -> 0.0]
print(1.5//3, 1.5/3) #o/p: 0.0 0.5

#-------------------------------------------------------------------------------------------------------------

#7: Remainder in negative only when denominator is negative.
print(5%2)  #o/p:1
print(-5%2)  #o/p:1
print(5%-2)  #o/p:-1