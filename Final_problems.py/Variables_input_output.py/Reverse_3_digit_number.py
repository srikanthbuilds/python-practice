print("--- Reversing 3 - digit number programe ---")
N = int(input("Enter a number  to reverse : "))
if len(str(N)) > 3:
    print("The number has more than 3 digits!")
else:
    rev = (N % 10) * 100 + (N // 10 % 10) * 10 + (N // 100)
    print(f"Reversed number            : {rev}")
