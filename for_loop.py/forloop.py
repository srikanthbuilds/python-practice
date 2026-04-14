# for loop : it executes the code by number of iterations !!
# syntax : for variable in range(start,stop(n-1),step):
#              // code

# To print 1 to 10 numbers using for loop !!
for i in range(1,11):
    if i == 5:
        continue # it will skip the current iteration and move to the next iteration !!
    elif i == 9:
        break
    print(i)