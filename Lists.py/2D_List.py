# -------------------------- 2D - Lists -------------------------------------

fruits =   ["apple","mango","grapes","orange","banana"]
vegetables=["carrots", "beetroots","onions","califlowers"]
meats =    ["chicken","mutton","Fish"]


groceries = [fruits,vegetables,meats]

for rows in groceries :
    for food in rows:
        print(food, end =", ")
    print()

print()
# Syntax : collection_name[rows][columns]
print(groceries[0])
print(groceries[1])
print(groceries[2])
print()
print(groceries[0][1])
print(groceries[1][1])
print(groceries[2][1])


print()
#  can i find the length of the collection of groceries ?
# yes, but its gives you length of rows only cause its a 2D collection of lists.
print("lenght of groceries is (for 2D it gives rows length) : ",len(groceries))
# for length of the columns , you nned to print like.....
print("length of fruits is : ",len(fruits))
print("length of vegetables is : ",len(vegetables))
print("length of meats is : ",len(meats))