# Task 7: Leap Year Check
year = int(input("Enter a year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Leap Year:", is_leap)
