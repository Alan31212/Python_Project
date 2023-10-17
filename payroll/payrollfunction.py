import os
# create a checking path 
def checkingF(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

# create menu options to process payroll
def menu():
    pstr = "Choose from the following payroll choices\n"
    pstr += "(1) A gross PR payroll report for all employees\n"
    pstr += "(2) A gross PR payroll report for a single employee by name\n"
    pstr += "(3) Add an employee record\n"
    pstr += "(4) Delete an employee record\n"
    pstr += "(5) Modify an employee record\n"
    pstr += "(6) Exit Program"
    print(pstr)

# add an employee record          
def addEmp():
    empFile = open("employees.txt", "a")
    FN = input("Enter the first name of the employee: ")
    LN = input("Enter the Last name of the employee: ")
    RP = input("Enter the rate of pay: ")
    HW = input("Enter the hours worked: ")
    empFile.write(f"{FN} {LN} {RP} {HW}\n")
    empFile.close()
    print("record added!")

# delete an employee record 
def deleteEmp():
    empFile = open("employees.txt", "r")
    tempFile = open("temp.txt", "w")
    name = input("Enter the name of employee to delete: ")
    deleted = False
    for line in empFile:
        if name not in line:
            tempFile.write(line)
        else:
            deleted = True
    empFile.close()
    tempFile.close()
    
    if deleted:
        os.remove("employees.txt")
        os.rename("temp.txt", "employees.txt")
        print("Employee record deleted")
    else:
        os.remove("temp.txt")
        print("Employee not found")

# Modify an employee record        
def modifyEmp(): 
    empFile = open("employees.txt", "r")
    tempFile = open("temp.txt", "w")
    name = input("Enter the name of employee to modify: ")
    modified = False
    for line in empFile:
        if name in line:
            firstname, lastname, rate, hours = line.strip().split(" ")
            newRP = float(input(f"Enter the new rate of pay: "))
            newHW = float(input(f"Enter the new number of hours worked: "))
            line = f"{firstname} {lastname} {newRP} {newHW}\n"
            modified = True
        tempFile.write(line)
    empFile.close()
    tempFile.close()
    
    if modified:
        os.remove("employees.txt") 
        os.rename("temp.txt", "employees.txt")
        print("Employee record modified")
    else:
        os.remove("temp.txt")
        print("Emplyee not found")

# Exit program
def exitApp():
    print("Exiting......")
    exit()

# display a gross payroll report for all employees     
def printall():
    empFile = open("employees.txt", "r")
    for line in empFile:
        line = line.split(" ")
        rate = float(line[2])
        hours = float(line[3])
        answer = line[0] + " " + line[1]
        print(answer, rate, hours, "and gross pay: $%4.2f" % (rate * hours))

# display a gross payroll report for just one select employee   
def printEmp():
    name = input("Enter in a name to search employee ")
    empFile = open("employees.txt", "r")
    for line in empFile:
        line = line.split(" ")
        rate = float(line[2])
        hours = float(line[3])
        if (name == line[0] + " " + line[1]):
            print(name, "$%4.2f" % (rate * hours))
            break
    else:
        print("Employee not found")    
    empFile.close() 