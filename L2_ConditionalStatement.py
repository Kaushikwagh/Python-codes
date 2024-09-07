# Conditional Statements 
# if-elif-else

age = 19
if(age >=18):
    print("Can vote and apply for license")
elif(age<18):
    print("You can't vote and apply for license")

# ex 02
light = "green"
if(light == "red"):print("Stop")
elif(light == "yellow"):print("ready")
elif(light == "green") : print("Go")
else : print("Colour doesn't match")

# ex 03
num = 5
if(num>2):print("greter than 2")
elif(num>3):print("greter than 3")

# ex 04
marks = 79
if(marks >= 90): print("Grade 'A'")
elif(marks >= 80): print("Grade 'B'")
elif(marks >= 70): print("Grade 'C'")
else : print("Fail")

# Nesting 
age2 = 98
if(age2 >= 18 ): 
    if(age2>=80): print("Cannot drive")
    else: print("can drive")
else: print("Cannot drive")
