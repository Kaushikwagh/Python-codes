# Nested Dictionaries
student = {
    "name" : "kaushik",
    "marks" : {
        "Phy" : 89,
        "Che" : 98,
        "Math" : 80
    }
}
print(student)
print(student["marks"])
print(student["marks"]["Phy"])

# - - - - - - - - - - - - - - -
# Methods of dictionary

# 1. Print all key (myDict.keys())
print(student.keys())
print("Keys : ",student.keys()) # this type casting
print("Length : ",len(student.keys())) # to print length

# 2. Print all values (myDict.values())
print(student.values())
print("Values : ",list(student.values()))

# 3. Print all (key, val) pairs as tuples (myDict.items())
print("Print as tuples : ",list(student.items()))

# 4. Print key according to value (myDict.get("key"))
print(list(student.get("marks")))

# 5. update method to add
student.update({"City" : "Bangalore"})
print(student["City"])

# 6. override method in dict
new_student = {"name" : "Wagh"}
student.update(new_student)
print(student["name"])  # wagh