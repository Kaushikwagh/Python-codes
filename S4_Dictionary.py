# Dictionary in python
    # Dictionary are use to store data values in key:value pairs
    # They are unordered, mutable and dont allow duplicate keys

info = {
    # "key" : "value",
    "name" : "kaushik",
    "role" : "SRE",
    "age" : 23,
    "company" : "Cisco",
    "Select" : True,
    "Skills" : ["Java","Python","JavaScript",],
    "Certifications" : ("AWS","MERN","JS1","JS2"),
    1 : "Yes"
}
print(type(info))
print(info)
print("- - - - - - -")
print(info["name"])
print(info["role"])
print(info["age"])
print(info["company"])
print(info["Select"])
print(info["Skills"])
print(info["Certifications"])
print(info[1])
print("- - - - - - -")

print(len(info)) # use check length of dist
print("- - - - - - -")

# to add more key value pair in same
info["surname"] = "wagh"
print(info["surname"])
print("- - - - - - -")

 
# to create null dist
null_dist = {}
print(null_dist)

# to add data in null dist
null_dist["name"] = "kaushik"
print(null_dist)

# to remove we use del
del null_dist["name"] 
print(null_dist)
print("- - - - - - -")
