# All functions creates a new string and then returns the answer. Old string remains as it is.

str1 = "i am a CoDeR"

# 1) str.endswith("character to check"): True if string ends with specfied substring, else returns false.
print(str1.endswith("er"))  #o/p: false as its "er". If it was "eR" we would get true

# 2) str.capitalize(): Captializes first character. 
print(str1.capitalize())

# 3) str.replace("old", "new"): Replaces old string with new. 
print(str1.replace("a", "A"))
print(str1.replace("CoDeR", "CoDeRRRRRRRRRRRRRRRRRRRR."))

# 4) str.find("word"): Returns 1st index of the 1st Occurrer
print(str1.find("o"))
# Returns -1 if word doesn't exist

#5) str.count("word"): Counts the no of times a word occurs in a string.
print(str1.count("a")) #o/p: 2

firstName = str(input("Enter FirstName: "))
print("Length is:", len(firstName))
print(str1.count("$"))

 