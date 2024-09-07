# Example 01
def sum(a,b):
    s = a + b
    print(s)
    return s

sum(2,4)
sum(3,5)
sum(10,10)

# - - - - - - -
# Example 02
def add(a,b):       #parameters
    return a + b

a = add(4,5)       #function call
print(a)

# - - - - - - -
# Example 03
def print_hello():
    print("hello")

print_hello()
    
# - - - - - - -
# Example 04 - function dont donot return then -> none
output = print_hello()
print(output)

# - - - - - - -
# Example 05 - Average of 3 numbers
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg

calc_avg(1, 2, 3)

# - - - - - - -
