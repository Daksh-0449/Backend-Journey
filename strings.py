"""
Python Strings
==============
Learning notes and practice covering:
- String creation
- Indexing
- Iteration
- Length
- Slicing
- String methods
- Formatting
- Escape characters
"""

# ============================================================
# 1. STRING CREATION
# ============================================================

name = "Daksh Jain"
city = "Udaipur"
message = """Hello, how are you?"""

print(name)


# ============================================================
# 2. STRING INDEXING
# ============================================================

print(city[0])
print(city[2])
print(city[4])


# ============================================================
# 3. ACCESS EVERY CHARACTER
# ============================================================

for ch in city:
    print(ch)


# ============================================================
# 4. LENGTH OF A STRING
# ============================================================

print(len(name))
print(len(city))


# ============================================================
# 5. STRING SLICING
# Syntax: string[start:stop:step]
# ============================================================

text = "python"

print(text[1:5])
print(text[-6:5])
print(text[:5])
print(text[2:])
print(text[-3:1])
print(text[::2])


# Reverse a string
print(text[::-1])


# More slicing practice
word = "Engineering"
print(word[:4])

text = "programming"
print(text[6:])

lulu = "computer"
print(lulu[::2])

shabd = "python"
print(shabd[::-1])


# ============================================================
# 6. STRING METHODS
# ============================================================

name = "Daksh"

# upper()
print(name.upper())

# lower()
print(name.lower())

# title()
text = "hello guyss"
print(text.title())

# strip()
word = "  python   "
print(word.strip())

# replace()
sentence = "i like panda"
print(sentence.replace("panda", "minion"))

# find()
print(name.find("s"))
# If the substring is not found, find() returns -1.

# count()
print(name.count("a"))

# startswith()
print(name.startswith("d"))

# endswith()
print(name.endswith("h"))

# split()
print(sentence.split())

# join()
words = ["hello", "world", "war"]
print(" ".join(words))


# ============================================================
# 7. MORE STRING METHODS
# ============================================================

print(name.capitalize())
print(name.swapcase())
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.isspace())


# ============================================================
# 8. STRING FORMATTING
# ============================================================

name = "DAKSH"
age = 19

print(f"My name is {name} and I am {age} years old")


# ============================================================
# 9. ESCAPE CHARACTERS
# ============================================================

# \n  -> new line
# \t  -> tab
# \"  -> double quote
