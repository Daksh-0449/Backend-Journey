"""
Python Tuples
=============
Learning notes and practice covering:
- Tuple creation
- Indexing
- Negative indexing
- Slicing
- Iteration
- Immutability
- Tuple methods: count() and index()
"""

# ============================================================
# 1. TUPLES ARE IMMUTABLE
# Lists are mutable, but tuples are immutable.
# ============================================================

fruits = ("Apple", "Banana", "Mango")

print(fruits)


# ============================================================
# 2. TUPLE INDEXING
# ============================================================

print(fruits[0])
print(fruits[2])
print(fruits[-1])


# ============================================================
# 3. TUPLE SLICING
# ============================================================

print(fruits[1:4])


# ============================================================
# 4. LOOP THROUGH A TUPLE
# ============================================================

for fruit in fruits:
    print(fruit)


# ============================================================
# 5. TUPLES CANNOT BE MODIFIED
# ============================================================

numbers = (10, 20, 30)

# This would raise a TypeError because tuples are immutable:
# numbers[1] = 100


# ============================================================
# 6. TUPLE METHODS
# ============================================================

numbers = (1, 2, 2, 3, 4, 2)

# count() -> returns how many times a value occurs
print("Count of 2:", numbers.count(2))

# index() -> returns the first index of a value
print("First index of 2:", numbers.index(2))
