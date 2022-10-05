# Algorithms -> steps to follow to achieve a task / step by step procedure of accomplishing a given task

# Simple Interest calculation
# 1. Store value of principle
# 2. Store value of rate
# 3. store value of time
principle = 20000
rate = 5
time = 7

interest = (principle*rate*time) / 100

print("The compound interest is:", interest)

# generating a user input
principle = int(input("Enter the principle:"))
rate = int(input("Enter the rate:"))
time = int(input("Enter the time :"))
interest = (principle*rate*time) / 100

print("The compound interest is:", interest)

# code to prompt user to enter amount in dollars then convert to shillings
# exchange rate : 1$ = 176Kshs

# Foreign Exchange Rates
print("Convert to US dollars")
Amount = int(input("Enter the amount you wish to convert:"))
conversion = Amount * 176
print("the conversion is:", conversion)

# code to calculate the volume of a cylinder
# PI * r**2 * H
PI = 3.142
print("Calculate volume of a cylinder")
r = int(input("Enter the radius:"))
H = int(input("Enter the height:"))
volume = PI * r**2 * H
print("The volume of the cylinder is:", volume)

# code to calculate a persons bmi body mass index
# weight(kg), height(m)
# bmi = weight / (height **2)
print("Calculate your BMI")
w = int(input("Enter your mass(kg):"))
h = float(input("Enter your height(metres):"))
bmi = w / (h **2)
print("Your BMI is:", bmi)

print("BASIC CALCULATIONS")