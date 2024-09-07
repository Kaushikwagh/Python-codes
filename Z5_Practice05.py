# Practices Question

# Q1. print the elements of the following list using a loop:
    # [1,4,9,16,25,36,49,64,81,100]

nums = (1,4,9,16,25,36,49,64,81,100)
x = 49
idx = 0
for el in nums:
    if el == x:
        print("Number found at index: ", idx)
        break
    idx += 1
print("End")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Q2. Range Practice question

    # A. Print numbers from 1 to 100
for i in range(1,101):
    print(i)

print(" - - - - - - - - - - - - ")

    # B. Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)

print(" - - - - - - - - - - - - ")

    # C. Print the multiplication table of a number n. 
n = 10
for i in range(1, 11):
    print(n*i)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Main Question

# Q3. WAP to find the sum of first natural numbers. (Using While)

# Using for loop

# no = 5
# sum = 0
# for i in range(1, no+1):
#     sum += i
# print("Total Sum : ",sum)

# - - - - - - - - - - - - - - - - - 

# Using while loop
no = 5
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1
print("Total Sum: ",sum)

print("- - - - - - - - - - - - ")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Q4. WAP to find the factorial of first n numbers. (Using for)

n = 5
fact = 1

for i in range(1, n + 1): 
    fact *= i
print("Factorial =", fact)
print("- - - - - - - - - - - - ")

print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Extra Question 
print("Extra Question")
print()

# Q5. Print Even Numbers:
for i in range (1, 10):
    if i % 2 == 0:
        print(i)
print()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q6. Sum of Even Numbers:
sum = 0
i = 1
while i <= 10:
    if i%2 == 0:
        sum += i
    i+=1
print("Sum of even no: ",sum)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q7. Multiplication Table:
n = 2
for i in range(1,11):
    # print(n*i)
    print(f"{n} x {i} = {n*i}")

print()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q8. Reverse a Number:
for i in range(9, 0, -1):
    print(i)

print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q9. Factorial of a Number:
factorial = 5
no = 1
for i in range(1, factorial + 1):
    no *= i
print(f"Factorial of {factorial} is {no}")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q10. Check Prime Number:
number = 29
is_prime = True
for i in range(2, int(number**0.5) + 1):
    if number%i == 0 :
        is_prime = False
        break
if is_prime:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q11. Fibonacci Series:
n = 10
a, b = 0, 1
print(a, b, end=" ")
for _ in range(n-2):
    a, b = b, a + b
    print(b, end=" ")
print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q12. Sum of Digits:
num = 1234
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10                  # remove last digit
print(f"Sum of digits: {sum_of_digits}")
print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q13. Palindrome Check
num = 121
original = num
reversed = 0
while num>0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10
if original == reversed:
    print(f"{original} is a Palindrome")
    print(f"{original}: Original Number")
    print(f"{reversed}: Reversed number")
else:
    print(f"{original} is not a Palindrome")
print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q14. Armstring Number Check
number = 153
cubes = 0   # we ban print and check both
temp = number
# logic 
while temp > 0:
    digit = temp % 10
    cubes += digit ** 3
    temp //=10
if number == cubes: print(f"{number} is an Armstrong")
else: print(f"{number} is not an Armstrong")
print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q15. Count vowels in a String
string = 'kaushik wagh'
vowels = 'aeiou'
count = 0
for char in string:
    if char.lower() in vowels:
        count += 1
print(f"Number of vowels in '{string}' is : {count}")
print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q16. Print Pattern
n = 5
for i in range(1, n+1):
    for i in range(1, i+1):
        print("*", end=" ")
    print()
print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Extra Practice

number = 222
count = 0
while number > 0:
    digit = number % 10
    count += digit
    number //= 10
print(count)
print()


# - - - - - - -

num = 123451231
original_num = num              # using only to add in print
check = 2
count = 0

while num > 0:
    digit = num % 10
    if digit == check:
        count += 1
    num = num // 10

print(f"The Count of '{check}' number in '{original_num}' is : {count}")
print()


# - - - - - - -


num = 121
original = num
reversed = 0
while num>0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10
if original == reversed:
    print(f"{original} is a Palindrome")
    print(f"{original}: Original Number")
    print(f"{reversed}: Reversed number")
else:
    print(f"{original} is not a Palindrome")
print()

# - - - - - - 

a = 1221
a_original = a
revers = 0
while a>0:
    digit = a % 10
    revers = revers * 10 * digit
    



