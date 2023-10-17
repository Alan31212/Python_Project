# TSU-CHENG, LU
# ITM 513 (02)     06/12/2023
# Lab3 
# Description: This program will prompt a user to enter the pin code, then input the balance and interest. After that it will compute the balance and interest for each of the twelve months in the year

# declare the bank balance and montly rate
def cal_balance(balance, interest):
    monthly_rate = interest / 12 
    new_balance = balance     
    total_interest = 0
   #using a looping statement to display the running balance for each of the twelve months in the year.  
    for month in range(1, 13):
        interest_earned = new_balance * monthly_rate
        new_balance += interest_earned
        total_interest += interest_earned
        print(f'Month: {month} Interest Amt: {interest_earned:.2f} New Monthly bal:  ${new_balance:.2f}')
    return new_balance, total_interest

# setting PIN code and PIN verification
pin = "1234"

for count in range(1, 4):
    pin_entered = input(f'please enter your PIN number({count}/3): ')
    if pin_entered == pin:
        print('you are in!!')
        break
    else:
        print('invalid PIN - try again!')

if pin_entered != pin:
    print('You already input the wrong PIN number for 3 times, please try it later.')
    exit()

#Prompt the user for bank balance and interest rate
balance = float(input('Enter an initial bank balance: '))
interest = float(input('Include annual interest rate (as a decimal: '))

#summary the total dollars accumulated plus the total interest accumulated
final_balance, final_interest= cal_balance(balance, interest)

print(f'\nFianl Balance after twelve months: {final_balance:.2f}')
print(f'Total interest accumulated: {final_interest:.2f}')