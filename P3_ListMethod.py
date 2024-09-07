# List Methods

list = [2,1,3]


# Method 01 :- add at last (Append method)
list.append(4)
print(list)

# Method 02 :- Sort method :- ascending order
list.sort()
print(list)

# Method 03 :- Sort method :- descending order
list.sort(reverse=True)
print(list)

# Method 04 :- reverse list
list.reverse()
print(list)

# Method 05 :- Insert element at any index
# idx, el
list.insert(3,5)
print(list)

# Method 06 :- Remove method use only for first occurrence
list.remove(4)
print(list)

# Method 07 :- pop Use to remove idx at list
list.pop(2)
print(list)
