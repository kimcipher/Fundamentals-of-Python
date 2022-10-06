print("BMI VERSION 2.0")

name = str(input("Please enter your surname:"))
w = int(input("Enter your mass(kg):"))
h = float(input("Enter your height(metres):"))
bmi = w / (h **2)

if bmi < 18.5:
    print(name,"you are underweight")
elif bmi > 18.5 and bmi <= 22.9:
    print(name,"you are normal")
elif bmi > 22.9 and bmi <= 24.9:
    print(name, "you are overweight")
elif bmi > 24.9 and bmi <= 29.9:
    print(name, "you are pre-obese")
elif bmi > 29.9 and bmi <= 34.9:
    print(name, "you are obese-classI")
elif bmi > 34.9 and bmi <= 39.9:
    print(name, "you are obese-classII")
elif bmi >= 40.0:
    print(name, "you are obese-classIII")

else:
    print("ERROR!!")