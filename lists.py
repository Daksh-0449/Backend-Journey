"""
Python Lists
============
Learning notes and practice covering:
- Creating lists
- Indexing
- Mutability
- len()
- Iteration
- Slicing
- List methods
- Nested lists
- List comprehension
"""

# ============================================================
# 1. CREATING A LIST
# Lists can store different datatypes.
# ============================================================

data = ["Daksh", 19, 85.5, True]
print(data)


# ============================================================
# 2. LIST INDEXING
# ============================================================

num = [10, 20, 30, 40, 50]

# 0 -> 10
# 1 -> 20
# 2 -> 30
# 3 -> 40
# 4 -> 50

print(num[0])
print(num[4])


# ============================================================
# 3. LISTS ARE MUTABLE
# ============================================================

num[1] = 100
print(num)


# ============================================================
# 4. LENGTH OF A LIST
# ============================================================

print("Length:", len(num))


# ============================================================
# 5. LOOP THROUGH A LIST
# ============================================================

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# ============================================================
# 6. LIST SLICING
# ============================================================

print(num[1:4])


# ============================================================
# 7. LIST METHODS
# ============================================================

fruits = ["Apple", "banana"]

# append()
fruits.append("Mango")
print("After append:", fruits)

# insert()
fruits.insert(1, "Grapes")
print("After insert:", fruits)

# extend()
more_fruits = ["Pineapple", "Watermelon"]
fruits.extend(more_fruits)
print("After extend:", fruits)

# remove()
fruits.remove("banana")
print("After remove:", fruits)

# pop()
num = [10, 20, 30, 40]
num.pop(2)
print("After pop:", num)

# clear()
num.clear()
print("After clear:", num)

# sort()
numbers = [5, 2, 8, 1]
numbers.sort()
print("After sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# count()
print("Count of 2:", numbers.count(2))

# index()
print("Index of Mango:", fruits.index("Mango"))


# ============================================================
# 8. NESTED LIST
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix)
print(matrix[0])
print(matrix[1][1])


# Print all elements
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# ============================================================
# 9. LIST COMPREHENSION
# ============================================================

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)


# Nested list containing student marks
marks = [
    ["Daksh", 85],
    ["Rohit", 90],
    ["Amit", 75],
]

for student in marks:
    for value in student:
        print(value, end=" ")
    print()

print(marks[1][1])


# Basic list comprehension
number = [i for i in range(1, 11)]
print(number)

squares = [i * i for i in range(1, 11)]
print(squares)
