# WAP to check if a number entered by the user is odd or even.
number = 9

if(number % 2 == 0):print("Even")
else:print("Odd")


# WAP to find the greatest of 3 numbers entered by the user.
user1 = 4
user2 = 5
user3 = 2

if(user1>=user2 and  user1>=user3):
    print("First number is largest", user1)
elif(user2>=user3):
    print("Second number is largest", user2)
else:
    print("Third number is largest", user3)

# WAP to check if a number is a multiple of 7 or Not
    # to check multiple reminder should 0(no%7 == 0)

num = 21
if(num%7 == 0):print(num, ": Is Multiple Of Seven")
else: print("Not multiple")