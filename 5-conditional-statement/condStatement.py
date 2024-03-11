# 1) if-else
light = input("Enter Light: ")
if(light.lower() == "red"):  #Covert input to lowercase
   print("Stop")
elif(light.lower() == "yellow"):
   print("Look!!!")
elif(light.lower() == "green" ):
   print("Go")
else:
   print("light is brokeNNN.")
#Indentation
#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
#Other programming languages often use curly-brackets for this purpose.
   
#----------------------------------------------------------------------------------------------------

#2) Ternary Operator: Single Line If
   
# Syntax 1: <var> = <val1> if<condition> else<val2>
   
food  = input("Enter Food: ") 
eat = "yeSSSSSS" if food.lower() == "cake" else "nOOOOO"
print(eat)

# Syntax 2: <val1> if<condition> else<val2>
print("sweet") if food.lower() == "cake" or food.lower() == "jalebi" else print("not sweet")
#if food is cake or jalebi print "sweet", else print "not sweet"

# Syntax 3: <var> = (false_val, true_val) [<condition>]
age = int(input("enter Age : "))
vote = ("No", "Yes") [age>=18]
print(vote)

sal = int(input("Enter salary : "))
tax = sal*(0.2,0.1) [sal<=50000]
print(tax)
