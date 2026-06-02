user_tuple = (1,2,3,4,5,6,7,8,9,0,-1,-2,-3,-4,-5,-6,-7,-8,-9)
min = user_tuple[0]
max = user_tuple[0]
for number in user_tuple:
    if number >= max:
        max = number
for number in user_tuple:
    if number <= min:
        min = number
print(f"Min : {min}")
print(f"Max : {max}")