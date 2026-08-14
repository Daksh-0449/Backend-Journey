"""
Python Match-Case
=================
A simple example of Python's match-case statement.
"""

day = int(input("Enter a day number (1-7): "))

match day:
    case 1:
        print("MONDAY")
    case 2:
        print("TUESDAY")
    case 3:
        print("WEDNESDAY")
    case 4:
        print("THURSDAY")
    case 5:
        print("FRIDAY")
    case 6:
        print("SATURDAY")
    case 7:
        print("SUNDAY")
    case _:
        print("INVALID DAY")
