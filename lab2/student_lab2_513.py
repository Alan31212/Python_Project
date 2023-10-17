# TSU-CHENG, LU
# ITM 513 (02)     06/08/2023
# Lab2 
# Description: This program will prompt a user to enter your weight and height. Then it will compute your BMI and identify you BMI status

#get the individual's weight and height
weight = float(input('your weight please ->'))
height = float(input('your height please ->'))

#compute the BMI
BMI = weight * 703/ height**2

if BMI < 18.5:
    print('the person is Underweight')
elif (BMI >= 18.5 and BMI <= 24.9):
    print('the person is Normal')
elif (BMI >= 25.0 and BMI <= 29.9):
    print('the person is Overweight')
else:
    print('the person is Obese') 

#show the BMI
print('BMI = ', BMI)
print('have a good healthy day')
