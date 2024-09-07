# 2. For loop
    #Loop are use for sequential traversal. for traversing list, string, tuples etc.

nums = [1,2,3,4,5]
for val in nums :
    print(val)

veggies = ["Potato","Brijal","Ladyfinger"]
for val in veggies :
    print(val)

# using on tuples
tup = (1,2,3,4,5,6,7,8)
for val in tup:
    print(val)

# Print str
str = "Kaushik"
for char in str:
    print(char)

# - - - - - - - - - - - -

# for loop with else

str = "Kaushik Wagh"
for char in str:
    if char == "k":
        print("Found")
        break
    print(char)
else:
    print("Not Found")

print()
# - - - - - - - - - - - -
# Practice questions

# Q1. Print the elements of the following list using a loop
    # [1,4,9,16,25,36,49,81,100]

list = [1,4,9,16,25,36,49,81,100]
for val in list:
    print(val)

print()

# Q2. Search for a number x in this tuple using loop:
    # [1,4,9,16,25,36,49,81,100]

tupp = (1,4,9,16,25,36,49,81,100)
x = 49
idx = 0

for el in tupp:
    if el == x:
        print("Number found at idx ", idx)
        break
    idx += 1
else:
    print("Number not found in the tuple")

print()

# - - - - - - - - - - - -
print("range() - Function")
# Range funcitons returns a sequence of number, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
print(range(5))
print()

seq = range(3)
print(seq[0])
print(seq[1])
print(seq[2])
# print(seq[3]) not allowed range is size of list 
print()
# - - - - - - - - - - - -

# range (start?, stop, step?(increase))
for i in range(2, 10, 2):
    print(i)

print()

# print even number using range
for i in range(2, 101, 2):
    print(i)

print()

# print odd number using range
for i in range(1, 100, 3):
    print(i)

print()

# - - - - - - - - - - - -
# Pass Statement: - Use to skip loop
for i in range(5):
    pass

print("Some useful work")
# - - - - - - - - - - - -
