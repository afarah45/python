#This program calculates the your Body Mass Index(BMI)

# get height and weight from user
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

#calculate BMI and round it to whole number
bmi = round(weight / height **2)

#print results
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weigth.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, your are slightly overweght.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
