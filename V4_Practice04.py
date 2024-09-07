# Q1. store following word meanings in a python distionary:
    # table : "a piece of furniture", "list of facts & figures"
    # cat : "a small animal"
store = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
# print(type(dict))
print("Q1. Store : ",store)

# - - - - - - - - - - - - - - - - -

# Q2. You are given a list of sub for students. assume on classroom is required for 1 subject. How many classrooms are needed by all students.
    # "python", "java", "C++", "python", "javascript"
    # "java", "python", "java", "C++", "C"

    # let assume -> py - 1 class, java - 1, C++ - 1, c - 1, js - 1, total classroom 5
subject = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}

print("Q2. Answer, Total Classroom : ", len(subject))

# - - - - - - - - - - - - - - - - -

# Q3. WAP to enter marks of 3 subjects form the user and store them in a dictionary. start with an emply dictionary and add on by one. use subject name as key and marks as value.

# marks = {}

# sub1 = int(input("Enter Phy : "))
# marks.update({"Phy" : sub1})

# sub2 = int(input("Enter Math : "))
# marks.update({"Math" : sub2})

# sub3 = int(input("Enter Chem : "))
# marks.update({"Chem" : sub3})

# print(marks)

# - - - - - - - - - - - - - - - - -

# Q4. Figure out a way to store 9 & 9.0 as separate values in the set.
    # (You can take help of built - in data types)

value = {
    ("float", 9.0),
    ("int", 9)
}
print(value)