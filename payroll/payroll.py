# TSU-CHENG, LU
# ITM 513 (02)     06/29/2023
# Lab5 
# Description: This lab will consist of options to users to view, add, modify or delete payroll record data.

from payrollfunction import *
# create the function of main
def main(): 
    file_path = input("Please enter the file path: ")
    if not checkingF(file_path):
        print("File doesn't exist!")
        return
    
    menu()
    choice = int(input("Enter Menu Choice Now! "))
    
    if choice == 1:
        printall()
    elif choice == 2:
        printEmp()
    elif choice == 3:
        addEmp()
    elif choice == 4:
        deleteEmp()
    elif choice == 5:
        modifyEmp()
    elif choice == 6:
        exitApp()
    else: 
        print("Invalid choice. Please try again")
        
main()
