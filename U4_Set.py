# set is collection of the unorder items
    # collection of unique value 
    # ex-> set (1,2,3) but (1,2,2)is not set

# Each element in the set must be unique and immutable(cannot change)
# we cannot store dicitonary or list in set bcoz they are mutable

# lets create sets 
collection = {1,2,3,4}
print(collection)
print(type(collection))

# - - - - - - - - - -

# if we use same values are repear then set ignore the values
# Let see unorder items ***
collect = {1,1,2,2,2,"kaushik","kaushik","wagh",5}
print(collect) #{1, 2, 5, 'kaushik', 'wagh'}

# length also ignore duplicate value
print("Length : ",len(collect))

# - - - - - - - - - -

# lets create empty set
collection1 = {} # This empty dictionary
collection2 = set() # This empty set

print(type(collection1)) #dict
print(type(collection2)) #set

print("- - - - - - - - - -")
# - - - - - - - - - - - - -
print("Set Methods ")
# Set Methods

box = set()

# 1. Add value in set (add method)
box.add(1)
box.add(2)
box.add(3)
box.add(3) #duplicate value should be ignore
box.add("kaushik") #str
box.add((1,2,3,4)) # tuple
# box.add([2,4,2,5]) # error list cannot be use in set 
print("Add value in set : ",box)

# 2. Remove value in set (remove method)
box.remove(2)
print(box)

# 3. Clear or empties the set (clear method)
box.clear()
print(box)

# 4. remove random values (pop method)
random_val = {"kaushik", "kau", "wag","awgsyfsd","java"}
print(random_val.pop()) #pick any random value all time

# 5. Union method (.union(set2)) use to join two set
set1 = {1,2,3}
set2 = {2,3,4}
print("Union : ", set1.union(set2)) #{1,2,3,4}

# 6. Intersection method (.intersenciton(set2)) combines coomon values and return new
print("Intersection : ", set1.intersection(set2)) #{2, 3}

