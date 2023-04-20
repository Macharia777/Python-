#nested loops exe
#Archibald Macharia

#let's create a BMI calculator which the user will enter the height and weight

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = round(weight / (height * height), 2)
if BMI < 18.5:
 print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI > 18.5 and BMI < 25:
 print(f"Your BMI is {BMI}, you are normal")
elif BMI > 25 and BMI < 30:
 print(f"Your BMI is {BMI}, you are overweight")
elif BMI > 30 and BMI < 35:
 print(f"Your BMI is {BMI}, you are obese")
else:
 print("You are clinically obese")

