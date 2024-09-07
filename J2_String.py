# Three ways to write string
# str1 = "This is String" # MOSTLY USED
# str2 = 'kaushik wagh'
# str3 = """is SRE engineer"""

# str4 = "this is a string.\ntwo creative"

# - - - - - - - - - - - - - - - - - - - -

# Basic Operations 
# 1. Concatenation :- Use to add two string
Str1 = "Kaushik"
Str2 = "Wagh"
final_str = Str1 + Str2
print(final_str)

# - - - - - - - - - - - - - - - - - - - -

# 2. Length of Str
len1 = len(Str1)
len2 = len(Str2)
print(len1)
print(len2)

# - - - - - - - - - - - - - - - - - - - -

# 3. Indexing
    # Start with 0 1 2 3 4 5 
str_index = "Kaushik wagh"
print(str_index[2]) #u

# - - - - - - - - - - - - - - - - - - - -

# 4. Slicing
    # to break string 
str_slice = "kaushik wagh"
print(str_slice[1:9]) #aushik w

print(str_slice[:2]) #From Start index
print(str_slice[1:len(str_slice)]) #till last index
print(str_slice[1:]) #till last index

# - - - - - - - - - - - - - - - - - - - -

# 5. Negative index 
    # Reverse counting of string
    # 
str_reverse = "KAUSHIK WAGH"
print(str_reverse[-9:-1])

# - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - -

# String Functions
str_Fun = "i am a coder"
print(str_Fun.endswith("er")) # True
print(str_Fun.capitalize()) # Capital first letter
print(str_Fun.replace("i","my")) # replace
print(str_Fun.find("coder")) # find letter index starting from
print(str_Fun.count("am")) # count of letter

# - - - - - - - - - - - - - - - - - - - -

