prime_num_count = 0
for number in range(1,101):
    if number%2 !=0 and number%number == 0:
        prime_num_count += 1
        print(number,f"  count - {prime_num_count}") 

print(f"From 1 TO 100 , we have {prime_num_count} PRIME numbers.")