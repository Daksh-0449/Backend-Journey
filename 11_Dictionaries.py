# Dictionary Basics
student = {
    "name" : "Daksh", #name --> key & daksh -->value
    "age" : 20 , 
    "cgpa" : 9.35
}

# Accessing a value
print(student["name"])

# Adding a new key-value pair
student["branch"] = "CSE"
print(student)

# Updating a value
student["age"] = 21
print(student["age"])


# Removing items from a dictionary

# del
del student["age"]
print(student)

# If you try to delete a key that does not exist, Python raises a KeyError.


# pop()
# Removes the specified key and returns its value.
removed_value = student.pop("branch")
print(removed_value)
print(student)

# popitem()
# Removes and returns the last inserted key-value pair.
x = student.popitem()
print(x)
print(student)


# clear()
# Removes all key-value pairs from the dictionary.
student.clear()
print(student)



# Checking whether a key exists
student_info = {
    "name" : "Rahul",
    "age" : 20,
    "branch" : "CSE"
}

print("name" in student_info)
print("branch" in student_info)
# The "in" operator checks for keys, not values

# keys() method
print(student_info.keys())

# values() method
print(student_info.values())

# items() method
print(student_info.items())
