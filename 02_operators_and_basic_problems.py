"""
Python Operators & Basic Problems
=================================
Practice with arithmetic operators, area calculations,
simple interest, conversions, ASCII values, swapping,
digit operations, and bank-note calculation.
"""

import math

# 1. Arithmetic operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)
print("Square of a =", a * a)
print("Square of b =", b * b)
print("Cube of a =", a * a * a)
print("Cube of b =", b * b * b)

# 2. Area of rectangle
length = int(input("Length of rectangle: "))
breadth = int(input("Breadth of rectangle: "))
print("Area of Rectangle =", length * breadth)

# 3. Area of circle
radius = int(input("Radius of circle: "))
print("Area of Circle =", math.pi * radius * radius)

# 4. Area of triangle
base = int(input("Base of triangle: "))
height = int(input("Height of triangle: "))
print("Area of Triangle =", 0.5 * base * height)

# 5. Area of square
side = int(input("Side of a square: "))
print("Area of Square =", side * side)

# 6. Simple interest
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

# 7. Kilogram to gram
weight = float(input("Enter weight in kg: "))
print("Weight in grams =", weight * 1000)

# 8. Gram to kilogram
weight_grams = float(input("Enter weight in grams: "))
print("Weight in kg =", weight_grams / 1000)

# 9. ASCII value of a character
ch = input("Enter a character: ")
print("ASCII value =", ord(ch))
print("Lowercase =", ch.lower())
print("Uppercase =", ch.upper())

# 10. Swap two numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = a
a = b
b = c
print(a, b)

# 11. Sum of digits of a three-digit number
num = int(input("Enter a three digit number: "))
first_digit = num // 100
second_digit = (num // 10) % 10
third_digit = num % 10
print("Sum of digits =", first_digit + second_digit + third_digit)

# 12. Reverse a three-digit number
print(
    "Reverse number =",
    third_digit * 100 + second_digit * 10 + first_digit,
)

# 13. Bank note calculation
amount = int(input("Enter amount: "))
notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for note in notes:
    count = amount // note
    print(note, "=", count)
    amount = amount % note
