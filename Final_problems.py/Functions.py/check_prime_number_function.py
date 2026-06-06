def primecheck(num):
        num = int(num)
        if num <=1 :
                print(f"{num} is NOT a PRIME NUMBER.")
        else:   
                if num == 2:
                        print(f"{num} is a PRIME NUMBER!")
                elif num%2 != 0 and num%num ==0:
                        print(f"{num} is a PRIME NUMBER!")
                else:
                        print(f"{num} is NOT a PRIME NUMBER!")
primecheck(13)