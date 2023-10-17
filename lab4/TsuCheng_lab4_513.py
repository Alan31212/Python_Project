# TSU-CHENG, LU
# ITM 513 (02)     06/24/2023
# Lab4 
# Description: This program will prompt a user to enter the credit card number, then it will check the number is valid or invalid


# Define the card number is valid or not
def isValid(number):
    return (sumOfDoubleEvenPlace(number) + sumofOddPlace(number)) % 10 == 0 

# doubling every second digit from right to left and sum it
def sumOfDoubleEvenPlace(number):
    total = 0 
    num = str(number)
    for i in range(len(num) -2, -1, -2):
        total += getDigit(int(num[i]) * 2)
    return total

# Add all digits in the odd places from right to left in the card number 
def sumofOddPlace(number):
    total = 0
    num = str(number)
    for i in range(len(num) -1, -1, -2):
        total += int(num[i])
    return total

# if the number is a single digits, then return the digit. Otherwise, return number as the sum of the two digits
def getDigit(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

# checking the digit d is a prefix for variable number or not
def prefixMatched(number, d):
    return getPrefix(number, len(str(d))) == d

# returning the number of digits in variable d
def getSize(d):
    return len(str(d))

# returning the first k number but if the number is less than k, return number
def getPrefix(number, k):
    num = str(number)
    if len(num) < k:
        return number
    else:
        return int(num[:k])

#input the credit card number
card_number = int(input("Credit card number: "))

#Depending the card number with isValid definition, then shows the results
if isValid(card_number):
    print('Valid credit card number')
else:
    print('invalid number')