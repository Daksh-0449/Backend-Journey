"""
Python Functions
================
Learning notes and practice covering:
- Defining and calling functions
- Multiple statements
- Parameters
- return
- Positional arguments
- Keyword arguments
- Default arguments
- Variable-length arguments (*args)
"""

# ============================================================
# 1. BASIC FUNCTION
# ============================================================

def welcome():
    print("TODAY I AM GOING TO LEARN FUNCTION")

# welcome()


# ============================================================
# 2. FUNCTION WITH MULTIPLE STATEMENTS
# ============================================================

def details():
    print("Name : Daksh")
    print("Branch : CSE")
    print("College : NIT Agartala")

# details()


# ============================================================
# 3. FUNCTION WITHOUT PARAMETERS
# ============================================================

def square():
    print(5 * 5)

# square()


def table():
    for i in range(1, 11):
        print(2 * i)

# table()


def stars():
    for i in range(1, 6):
        for j in range(1, 6):
            print("*", end=" ")
        print()

# stars()


# ============================================================
# 4. FUNCTIONS WITH PARAMETERS
# ============================================================

def greet(name):
    print("Hello", name)

# greet("Daksh")


def square_number(num):
    print(num * num)

# square_number(5)
# square_number(19)


def add(a, b):
    print(a + b)

# add(10, 30)
# add(5, 6)


def cube(num):
    print(num * num * num)

# cube(34)
# cube(12)


def largest(a, b):
    if a > b:
        print("a is larger than b")
    else:
        print("b is larger than a")

# largest(18, 20)


def area_of_rectangle(length, breadth):
    print("Area =", length * breadth)

# area_of_rectangle(5, 10)


# ============================================================
# 5. RETURN STATEMENT
# ============================================================

# return sends a value back to the caller and exits the function.

def add_num(a, b):
    return a + b


result = add_num(10, 40)
print("Returned result:", result)


def check(n):
    if n % 2 == 0:
        return "even"
    return "odd"


print("5 is", check(5))


# ============================================================
# 6. POSITIONAL ARGUMENTS
# Values are assigned according to their position.
# ============================================================

def introduce(name, age):
    print("Name :", name)
    print("Age :", age)


introduce("Daksh", 20)


# ============================================================
# 7. KEYWORD ARGUMENTS
# Parameter names are specified while calling the function.
# ============================================================

introduce(age=19, name="Daksh")


# ============================================================
# 8. DEFAULT ARGUMENTS
# A parameter can have a default value.
# ============================================================

def greet_user(name="Guest"):
    print("Hello", name)


greet_user()
greet_user("Daksh")


# ============================================================
# 9. VARIABLE-LENGTH ARGUMENTS (*args)
# ============================================================

def add_many(*num):
    print("Sum =", sum(num))


add_many(10, 20)
add_many(1, 2, 3, 4, 5)
