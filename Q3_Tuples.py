# Tuples in python
    # a in built- datatype 
    # create immutable sequences of values.
    # similar to list [] and tuples ()

tup = (87,64, 33, 95, 76)
print(tup)
print(type(tup))

print(tup[0])

# tup[0] = 98 cannot change value

# - - - - - - - - - - - - - - - - -

# Slicing in tuples
# similar as all slicing method
a =(1,2,3,4,5)
print(a[1:3])

# - - - - - - - - - - - - - - - - -

# Methods in tuple

# 1. To find number
b = (2, 1, 3, 1)
print(b.index(3))

# 2. To count of number
print(b.count(1))