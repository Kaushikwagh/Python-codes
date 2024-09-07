# Loops

# 1. While Loop

count = 1       # Iterator
while count <= 5 : 
    print("hello")
    count += 1 

i = 1
while i<= 5 :
    print("kaushik")
    i += 1

i = 1
while i <= 5 :
    print(i)
    i += 1          # print 1 2 3 4 5 

i = 5
while i >= 1:
    print(i)
    i -= 1          # print 5 4 3 2 1

# - - - - - - - - - - - - - - - - - - -
# Practice While loop

# Q1. Print numbers from 1 to 100
no1 = 1
while no1 <= 100:
    print(no1)
    no1 += 1

# Q2. Print numbers from 100 to 1
no2 = 100
while no2 >= 1:
    print(no2)
    no2 -= 1

# Q3. Print the multiplication table of a number n
n = 4  # You can change this to any number whose table you want to print
i = 1
while i <= 10:
    print(n * i)  # Table of n
    i += 1

# Q4. Print the elements of the following list using a loop:
# [1, 4, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 16, 25, 36, 49, 64, 81, 100]
count = 0
while count < len(nums):
    print(nums[count])
    count += 1

# Q5. Search for a number x in this tuple using loop:
# [1, 4, 16, 25, 36, 49, 64, 81, 100]
nums2 = (1, 4, 16, 25, 36, 49, 64, 81, 100)
No_find = 49
i = 0
found = False
while i < len(nums2):
    if nums2[i] == No_find:
        print("Found at index", i)
        found = True
        break  # Exit the loop once the number is found
    i += 1
if not found:
    print("Number not found in the tuple")
