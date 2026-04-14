"""
-> Typecasting =  it is a process of converting a data type to another datatype,
  examples -  int(),float(),str(),char()

"""
name = "Srikanth"
age = 18
bank_balance = 1000.98
is_student  = True 


""" bank_balance = bool(bank_balance)
print(bank_balance) """

# int to float conversion !
age = float(age)
print(age)

# float to int conversion !
bank_balance  = int(bank_balance)
print(bank_balance)

# to find stored data types !

print(type(name))
print(type(age))
print(type(bank_balance))
print(type(is_student))