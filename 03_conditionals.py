"""
Python Conditionals
===================
Practice with if, elif, else, comparison operators,
logical operators, and decision-making.
"""

# ============================================================
# 1. AGE CHECK
# ============================================================

age = int(input("Enter age: "))

if age > 18:
    print("You can vote")
else:
    print("You cannot vote")


# ============================================================
# 2. CHECK IF TWO NUMBERS ARE EQUAL
# ============================================================

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a == b:
    print("a and b are equal")
else:
    print("a and b are not equal")


# ============================================================
# 3. POSITIVE OR NEGATIVE
# ============================================================

num = int(input("Enter a number: "))

if num > 0:
    print("num is positive")
else:
    print("num is negative")


# ============================================================
# 4. GREATER THAN 500
# ============================================================

if num > 500:
    print("num is greater than 500")
else:
    print("num is not greater than 500")


# ============================================================
# 5. EVEN OR ODD
# ============================================================

if num % 2 == 0:
    print("num is an even number")
else:
    print("num is an odd number")


# ============================================================
# 6. DIVISIBLE BY 5
# ============================================================

if num % 5 == 0:
    print("num is divisible by 5")
else:
    print("num is not divisible by 5")


# ============================================================
# 7. GREATER OF TWO NUMBERS
# ============================================================

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


# ============================================================
# 8. VOWEL OR CONSONANT
# ============================================================

ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# ============================================================
# 9. PASS OR FAIL
# ============================================================

percentage = float(input("Enter your percentage: "))

if percentage > 33:
    print("Pass")
else:
    print("Fail")


# ============================================================
# 10. NUMBER BETWEEN 100 AND 200
# ============================================================

num = int(input("Enter a number: "))

if 100 < num < 200:
    print(num, "lies between 100 and 200")
else:
    print(num, "does not lie between 100 and 200")


# ============================================================
# 11. LOGIN CHECK
# ============================================================

correct_username = "ladle"
correct_password = "comedy"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")


# ============================================================
# 12. LEAP YEAR
# ============================================================

year = int(input("Enter your year: "))

if (year % 4 == 0) or (year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# ============================================================
# 13. CHECK TRIANGLE BY ANGLES
# ============================================================

angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

if angle1 + angle2 + angle3 == 180:
    print("Yes, it is a triangle")
else:
    print("No, it is not a triangle")


# ============================================================
# 14. PROFIT OR LOSS
# ============================================================

original_amount = float(input("Enter the original amount of product: "))
sold_amount = float(input("Enter the amount at which the product is sold: "))

if original_amount > sold_amount:
    print("LOSS")
else:
    print("PROFIT")


# ============================================================
# 15. DIFFERENCE FROM 51
# ============================================================

num = int(input("Enter a number: "))
difference = num - 51

if num > 51:
    print(difference * 3)
else:
    print(difference)


# ============================================================
# 16. CHECK FOR 30
# ============================================================

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a == 30 or b == 30 or (a + b == 30):
    print(True)
else:
    print(False)


# ============================================================
# 17. DAY OF THE WEEK
# ============================================================

num = int(input("Enter a number between 1 and 7: "))

if num == 1:
    print("MONDAY")
elif num == 2:
    print("TUESDAY")
elif num == 3:
    print("WEDNESDAY")
elif num == 4:
    print("THURSDAY")
elif num == 5:
    print("FRIDAY")
elif num == 6:
    print("SATURDAY")
else:
    print("SUNDAY")


# ============================================================
# 18. MONTH OF THE YEAR
# ============================================================

num = int(input("Enter a number between 1 and 12: "))

if num == 1:
    print("JANUARY")
elif num == 2:
    print("FEBRUARY")
elif num == 3:
    print("MARCH")
elif num == 4:
    print("APRIL")
elif num == 5:
    print("MAY")
elif num == 6:
    print("JUNE")
elif num == 7:
    print("JULY")
elif num == 8:
    print("AUGUST")
elif num == 9:
    print("SEPTEMBER")
elif num == 10:
    print("OCTOBER")
elif num == 11:
    print("NOVEMBER")
else:
    print("DECEMBER")


# ============================================================
# 19. DIVISIBILITY BY 3, 5 AND 8
# ============================================================

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0 and num % 8 == 0:
    print(num, "is divisible by 3, 5 and 8")
elif num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by 3 and 5")
elif num % 5 == 0 and num % 8 == 0:
    print(num, "is divisible by 8 and 5")
elif num % 3 == 0 and num % 8 == 0:
    print(num, "is divisible by 3 and 8")
elif num % 3 == 0:
    print(num, "is divisible by 3")
elif num % 5 == 0:
    print(num, "is divisible by 5")
elif num % 8 == 0:
    print(num, "is divisible by 8")
else:
    print(num, "is not divisible by 3, 5 and 8")


# ============================================================
# 20. GREATEST OF THREE NUMBERS
# ============================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a, "is the greatest number.")
elif b > a and b > c:
    print(b, "is the greatest number.")
else:
    print(c, "is the greatest number.")


# ============================================================
# 21. GRADE CALCULATOR
# ============================================================

marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    print("GRADE : A")
elif 75 <= marks <= 89:
    print("GRADE : B")
elif 50 <= marks <= 74:
    print("GRADE : C")
else:
    print("GRADE : F")
