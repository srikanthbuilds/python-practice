def factorial(num):
    num = int(num)
    if num <= 1:
        return 1
    return num * factorial(num-1)
result_factorial = factorial(3)
print(f"Factorial : {result_factorial}")
