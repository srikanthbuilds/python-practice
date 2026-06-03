n = int(input("Enter how many employees do you want to enter : "))
employees = dict()
for employee in range(n):
    print(f"----- Entering details for employee #{employee+1} -----")
    emp_id = input("Enter employee ID : ")
    name = input("Enter name : ")
    role = input("Enter role : ")
    salary = input("Enter salary : ")

    employees[emp_id] = {
        "Name": name,
        "Role": role,
        "Salary": salary
    }
print("----- All employees records -----")
print(employees)
print("---------------------------------")
print("----- Formated employees Details -----")
for emp_id , details in employees.items():
    print(f"Employee Id : {emp_id}")
    print(f"Name        : {details["Name"]}")
    print(f"Role        : {details["Role"]}")
    print(f"Salary      : {details["Salary"]}")
print("--------------------------------------")
