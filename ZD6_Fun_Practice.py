# 1. WAP to print the length of a list. (list is the parameter)
def length(list):
    print(len(list))

details = ["kaushik", "wagh", "is", "Software","Engineer"]
cities = ["Bangalore", "Ch.Shambhaji Nagar","Pune","Mumbai"]

length(details)
length(cities)

# 2. WAP  to print the elements of a list in a single line. (list is the parameter)

# print(cities[0], end=" ")
# print(cities[1], end=" ")

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(details)
print()
print_list(cities)
print()

# 3. WAP to find the factorial of n. (n is the parameter)
# ex- n! = 1*2*..n

n = 12
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)