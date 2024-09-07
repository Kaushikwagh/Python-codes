# Function Types
# 1. Built in function
str = 'kaushik'
print(str)
print(len(str))
print(type(str))
# range(start, end, gap)


# 2. User defined function 
def add(a,b):       #parameters
    return a + b

a = add(4,5)       #function call
print(a)

# Default parameter
def cal_prod(a, b = 2):
    print(a*b)
    return a*b

cal_prod(2)