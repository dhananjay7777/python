#  break statement: break: Terminates the loop it is inside. When break is encountered, the loop immediately
#  ends, and the program continues with the code that follows the loop.

# continue: Skips the rest of the code inside the loop for the current iteration and proceeds to the next 
# iteration of the loop. The loop does not end; it just goes to the next iteration. Basically go back to
# the loop. If any code is after it, it will not be executed.

# pass: Does nothing. It is used when a statement is required syntactically but you want to do nothing. It 
# is often used as a placeholder where code will eventually go, to avoid syntax errors.

x = 0
while x<=3:
   x += 1
   continue
   print(x) #o/p: [empty output]
# as soon as continue is encountered, the control goes back to while and again loop runs. Therefore, print(x)
# is never encountered.

#-------------------------------------------------------------------------------------------------------------
for i in range (1,6): 
   if(i==3):
      continue # skip printing 5
   if i==5:
      break  # Stop loop after reaching 5
   print(i)
else: 
   pass # # This is a placeholder, does nothing
#0/p: 1 2 4