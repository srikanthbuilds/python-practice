number = 1
prime_number_count = 0
while number <= 100:
    if number%2 != 0 and number%number == 0:
        prime_number_count += 1
        print(number,f"    count - {prime_number_count}")
    number+=1
print(f"From 1 TO 100 numbers, we have '{prime_number_count}' PPRIME numbers.")