def fibonacci_series(num):
    num = int(num)
    a = 0
    b = 1
    for i in range(num):
        print(a)
        c = a+b
        a = b
        b = c
fibonacci_series(5)