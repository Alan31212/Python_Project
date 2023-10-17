# TSU-CHENG, LU
# ITM 513 (02)     06/08/2023
# Lab1 
# Description: This program will prompt a user to enter the appliance name, cost per hw - hr, and annual hours. Then it will convert the total cost, average, variance, and standard diviation

# declare variable as a float type to accumulate total charges
totalCost = 0.0 
# declare a variable for the appliance name
appName = ""
# declare a variable for the cost per KW - hr
costPerKW1 = 0.0
costPerKW2 = 0.0
costPerKW3 = 0.0
costPerKW4 = 0.0
costPerKW5 = 0.0
costPerKW6 = 0.0
# declare a variable for the annual usage
annualUsage = 0.0
# declare a variable for number of cost items
costItems = 6
# declare a variable for totalKwhr
totalKwhr = 0
# declare a variable for variance
variancePerKW = 0.0000

#first appliance
print ("[ please enter the requested data ]")
print ("Please enter the first appliance name:")
appName = input()
print ("Please enter the cost_per_kwh per KW/HR of the appliance (in cents):")
costPerKW1 = float(input())
print ("Please enter the annual hours used:")
annualUsage1 = float(input())
totalCost = (costPerKW1 * annualUsage1)
totalKwhr = costPerKW1

#second appliance
print ("Please enter the second appliance name:")
appName = input()
print ("Please enter the cost_per_kwh per KW/HR of the appliance (in cents):")
costPerKW2 = float(input())
print ("Please enter the annual hours used:")
annualUsage2 = float(input())
totalCost += (costPerKW2 * annualUsage2)
totalKwhr += costPerKW2 

#third appliance
print ("Please enter the third appliance name:")
appName = input()
print ("Please enter the cost_per_kwh per KW/HR of the appliance (in cents):")
costPerKW3 = float(input())
print ("Please enter the annual hours used:")
annualUsage3 = float(input())
totalCost += (costPerKW3 * annualUsage3)
totalKwhr += costPerKW3 

#fourth appliance
print ("Please enter the fourth appliance name:")
appName = input()
print ("Please enter the cost_per_kwh per KW/HR of the appliance (in cents):")
costPerKW4 = float(input())
print ("Please enter the annual hours used:")
annualUsage4 = float(input())
totalCost += (costPerKW4 * annualUsage4)
totalKwhr += costPerKW4 

#fifth appliance
print ("Please enter the fifth appliance name:")
appName = input()
print ("Please enter the cost_per_kwh per KW/HR of the appliance (in cents):")
costPerKW5 = float(input())
print ("Please enter the annual hours used:")
annualUsage5 = float(input())
totalCost += (costPerKW5 * annualUsage5)
totalKwhr += costPerKW5

#sixth appliance
print ("Please enter the sixth appliance name:")
appName = input()
print ("Please enter the cost_per_kwh per KW/HR of the appliance (in cents):")
costPerKW6 = float(input())
print ("Please enter the annual hours used:")
annualUsage6 = float(input())
totalCost += (costPerKW6 * annualUsage6)
totalKwhr += costPerKW6 

#calculate the average, variance, and standard deviation
average = totalKwhr / costItems
    #var = sum((average - cost) ** 2 for cost in costItems)/ len(costItems)
    #stdDev = var ** .5

#print the outcome
print("Total Annual Cost $%.2f" %(totalCost))
print("%-10s: $%.2f" % ("Average", average))
    #print("%-10s: $%.4f" % ("Var", var))
    #print("%-10s: $%.4f" % ("stdDev", stdDev))



