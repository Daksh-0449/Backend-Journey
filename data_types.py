"""
Python Data Types
=================
Topics covered:
- Strings
- String methods
- String indexing and slicing
- Boolean
- Integer, Float, Complex numbers
- Type casting
- Built-in numeric functions
- Math module
"""

import math


# ============================================================
# 1. STRING DATA TYPE
# ============================================================

first = "daksh"
last = "jain"

print("----- Strings -----")

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!@"
print(fullname)


# Checking the type
print(type(first))
print(isinstance(first, str))


# String constructor
pizza = str("Pepperoni")
print(pizza)
print(type(pizza))
print(isinstance(pizza, str))


# ============================================================
# 2. TYPE CASTING: NUMBER -> STRING
# ============================================================

decade = str(2006)

print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)


# ============================================================
# 3. MULTILINE STRINGS
# ============================================================

multiline = """
Hey, how are you?

I was just checking in.

                            All good?
"""

print(multiline)


# ============================================================
# 4. ESCAPING SPECIAL CHARACTERS
# ============================================================

sentence = (
    "I'm back at work!\tHey!\n\n"
    "Where's this \\ located?"
)

print(sentence)


# ============================================================
# 5. STRING METHODS
# ============================================================

print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("good", "ok"))

# Length of a string
print(len(multiline))

# Removing whitespace
multiline += "                "

print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


# ============================================================
# 6. STRING FORMATTING
# ============================================================

title = "menu".upper()

print(title.center(20, "="))

print("coffee".ljust(18, ".") + "$2".rjust(4))
print("tea".ljust(18, ".") + "$1".rjust(4))
print("muffin".ljust(18, ".") + "$1".rjust(4))
print("cheese cake".ljust(18, ".") + "$3".rjust(4))
print("black coffee".ljust(18, ".") + "$1".rjust(4))


# ============================================================
# 7. STRING INDEXING & SLICING
# ============================================================

print(first[3])       # Indexing
print(first[0])
print(first[-1])

print(first[0:-1])   # Slicing
print(first[0:])


# ============================================================
# 8. STRING METHODS RETURNING BOOLEAN
# ============================================================

print(first.startswith("d"))
print(first.endswith("s"))


# ============================================================
# 9. BOOLEAN DATA TYPE
# ============================================================

my_value = True
x = bool(False)

print(type(x))
print(isinstance(my_value, bool))


# ============================================================
# 10. NUMERIC DATA TYPES
# ============================================================

# Integer
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))


# Float
gpa = 9.35
y = float(9.45)

print(type(gpa))
print(type(y))


# Complex number
comp_value = 5 + 4j

print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


# ============================================================
# 11. BUILT-IN FUNCTIONS FOR NUMBERS
# ============================================================

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))


# ============================================================
# 12. MATH MODULE
# ============================================================

print(math.pi)
print(math.sqrt(729))
print(math.ceil(gpa))
print(math.floor(gpa))


# ============================================================
# 13. TYPE CASTING: STRING -> NUMBER
# ============================================================

zipcode = "100011"
zip_value = int(zipcode)

print(type(zip_value))
print(zip_value)


# ============================================================
# Invalid Type Casting
# ============================================================

# This will raise a ValueError because "New York"
# cannot be converted into an integer.

# zip_value = int("New York")
