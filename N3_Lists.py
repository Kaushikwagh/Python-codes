# Lists in python
    # A built-in data type that stores set of values
    # it can store elements of different types (integer, float, string, etc.)

marks1 = 92.5
marks2 = 45.5
marks3 = 64.6
marks4 = 54.9
marks5 = 75.3
# to store all this in single list we use list- data type
# this is build-in data type

marks = [92.5, 45.5, 64.6, 54.9, 75.3]
print(marks)
print(type(marks))

# Printing using index
print("At index 0 :",marks[0]) # At index 0
print("At index 1 :",marks[1]) # At index 1

# To print length of list
print("Length of list :",len(marks))

# Multiple type we can add list 
student = ["kaushik", "23", "Bangalore"] #str, int, str
print(student)

# String -> immutable (Can't be change)
# list   -> mutable (Can be change)

# ex : - str
# str = "hello"
# print(str[0])
# str[0] = "y"

# ex: - list
list = ["Kaushik","Wagh"]
print("Before list :",list)
list[0] = "Ravindra"
print("After list :",list)

