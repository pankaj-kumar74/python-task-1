# Task 8: Armstrong Number Check
n = int(input("Enter a number: "))
digits = str(n)
power = len(digits)
armstrong_sum = sum(int(d)**power for d in digits)
print("Armstrong Number:", armstrong_sum == n)
