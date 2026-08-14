"""
Python Loops
============
Practice with while, for, range(), break, continue,
pass, nested loops, factorial, and reversing numbers.
"""

# 1. While loop
i = 1
while i <= 3:
    print(i)
    i += 1

count = 1
while count <= 4:
    print("DAKSH JAIN")
    count += 1

i = 1
while i <= 10:
    print(i)
    i += 1

i = 10
while i >= 1:
    print(i)
    i -= 1

i = 2
while i <= 20:
    print(i)
    i += 2

# 2. For loop
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(2, 11, 2):
    print(i)

for i in range(5):
    print("DAKSH JAIN")

for i in range(1, 10, 1):
    print(i)

for i in range(7, 100, 7):
    print(i)

# 3. Break
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# 4. Continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 5. Pass
for i in range(1, 6):
    if i == 3:
        pass
    print(i)

# 6. More break / continue practice
for i in range(1, 10):
    if i == 7:
        break
    print(i)

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

for i in range(2, 20, 2):
    print(i)

# 7. Nested loops
for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()

for i in range(10):
    for j in range(5):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 8. Sum from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(total)

# 9. Factorial
fact = 1
n = int(input("Enter a number (1-10): "))
for i in range(1, n + 1):
    fact *= i
print(fact)

# 10. Reverse a number
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed number =", rev)

# 11. Club night
print("CLUB N NIGHT")
age = int(input("Enter your age: "))
if age >= 18:
    print("You can enter the club")
else:
    print("Sorry, you are not allowed to enter the club")

# 12. Food menu
print("Order your food from the menu")
menu = ["Pizza - 250", "Burger - 150", "Cold Drink - 70"]
print("Menu:", menu)
choice = input(
    "Enter a number (1 for pizza, 2 for burger, 3 for cold drink) or name: "
)

if choice == "1" or choice.lower() == "pizza":
    print("----- BILL -----")
    print("Item : Pizza")
    print("Price : 250")
elif choice == "2" or choice.lower() == "burger":
    print("----- BILL -----")
    print("Item : Burger")
    print("Price : 150")
elif choice == "3" or choice.lower() == "cold drink":
    print("----- BILL -----")
    print("Item : Cold Drink")
    print("Price : 70")
else:
    print("Invalid choice")
