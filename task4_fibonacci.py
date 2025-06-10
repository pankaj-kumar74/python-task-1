# Task 4: Fibonacci Sequence
n = int(input("Enter how many Fibonacci numbers to generate: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print("Fibonacci Sequence:", fib[:n])
